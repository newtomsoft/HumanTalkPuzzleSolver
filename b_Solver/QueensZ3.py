from z3 import Solver, Distinct, Int, sat

def solve_queens_z3(n=4):
    solver = Solver()
    queens = [Int(f'R{i}') for i in range(n)]

    for queen in queens:
        solver.add(queen >= 0, queen < n)

    solver.add(Distinct(queens))

    for i in range(n):
        for j in range(i + 1, n):
            solver.add(queens[i] != queens[j] + (j - i))
            solver.add(queens[i] != queens[j] - (j - i))

    if solver.check() == sat:
        model = solver.model()
        for i in range(n):
            print(f"{str(queens[i])} C{model[queens[i]].as_long()}")


solve_queens_z3(4)