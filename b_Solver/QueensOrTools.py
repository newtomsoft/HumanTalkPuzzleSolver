import time

from ortools.sat.python import cp_model

def queens_solver(n=4) -> None:
    model = cp_model.CpModel()
    queens = [model.NewIntVar(0, n - 1, f'R{i}')
              for i in range(n)]

    model.AddAllDifferent(queens)

    for i in range(n):
        for j in range(i + 1, n):
            model.Add(queens[i] != queens[j] + (j - i))
            model.Add(queens[i] != queens[j] - (j - i))

    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if (status == cp_model.OPTIMAL
            or status == cp_model.FEASIBLE):
        for queen in queens:
            print(f"{queen.name} C{solver.value(queen)}")

    # Statistiques
    print("\nStatistiques")
    print(f"  status         : {solver.StatusName(status)}")
    print(f"  branches       : {solver.num_branches}")
    print(f"  wall time      : {solver.wall_time:.3f} s")


start_time = time.time()
queens_solver(20)
end_time = time.time()
print(f"Temps d'exécution : {end_time - start_time:.3f} secondes")
