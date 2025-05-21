import sys
import time
from ortools.sat.python import cp_model


class PocOrTools(cp_model.CpSolverSolutionCallback):
    def __init__(self, solver: cp_model.CpSolver, x, y):
        super().__init__()
        self._x = x
        self._y = y
        self._solver = solver
        self.__solution_count = 0
        self.__start_time = time.time()

    @property
    def solution_count(self) -> int:
        return self.__solution_count

    def on_solution_callback(self):
        self.__solution_count += 1
        self.print_solution()

    def print_solution(self):
        print(self.value(self._x))
        print(self.value(self._y))


def main() -> None:
    model = cp_model.CpModel()

    x = model.new_bool_var("x")
    y = model.new_bool_var("y")

    model.AddBoolOr([x, y])

    solver = cp_model.CpSolver()
    solution_printer = PocOrTools(solver, x, y)
    solver.parameters.enumerate_all_solutions = True
    solver.solve(model, solution_printer)

    # Statistics.
    print("\nStatistics")
    print(f"  branches       : {solver.num_branches}")
    print(f"  wall time      : {solver.wall_time} s")
    print(f"  solutions found: {solution_printer.solution_count}")


if __name__ == "__main__":
    main()
