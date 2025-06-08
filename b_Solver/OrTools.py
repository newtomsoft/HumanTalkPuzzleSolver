import sys
import time
from ortools.sat.python import cp_model


class SolutionCallBack(cp_model.CpSolverSolutionCallback):
    def __init__(self, solver: cp_model.CpSolver, variables):
        super().__init__()
        self._variables = variables
        self._solver = solver
        self._solution_count = 0
        self._start_time = time.time()

    @property
    def solution_count(self) -> int:
        return self._solution_count

    def on_solution_callback(self):
        self._solution_count += 1
        self.print_solution()

    def print_solution(self):
        print("Solution trouvée:")
        for var_name, var in self._variables.items():
            print(f"{var_name} = {self.value(var)}")
        print("---")


def main() -> None:
    model = cp_model.CpModel()

    a = model.new_bool_var("A")
    b = model.new_bool_var("B")
    c = model.new_bool_var("C")

    model.AddBoolOr([a, b])  # (A ∨ B)
    model.AddBoolOr([~a, c])  # (¬A ∨ C)
    model.AddBoolOr([~b, ~c])  # (¬B ∨ ¬C)

    solver = cp_model.CpSolver()
    variables = {"A": a, "B": b, "C": c}
    status = solver.solve(model)

    for var_name, var in variables.items():
        print(f"{var_name} = {solver.value(var)}")

    # Statistiques
    print("\nStatistiques")
    print(f"  status         : {solver.StatusName(status)}")
    print(f"  branches       : {solver.num_branches}")
    print(f"  wall time      : {solver.wall_time:.3f} s")


if __name__ == "__main__":
    main()