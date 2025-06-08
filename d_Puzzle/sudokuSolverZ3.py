import time

from z3 import Solver, Int, sat, Distinct

_ = 0


def solve_sudoku(initial_grid: list[list]) -> None:
    start_time = time.time()
    line_size = len(initial_grid)
    sub_square_size = int(line_size ** 0.5)
    line = list(range(0, line_size))
    in_sub_square = list(range(0, sub_square_size))

    print("initial grid:")
    for i in line:
        print([initial_grid[i][j] for j in line])

    solver = Solver()
    grid_z3 = {}
    for i in line:
        for j in line:
            grid_z3[(i, j)] = Int(f"cell{i}_{j}")
            solver.add(grid_z3[(i, j)] >= 1, grid_z3[(i, j)] <= line_size)

    for i in line:
        solver.add(Distinct([grid_z3[(i, j)] for j in line]))

    for j in line:
        solver.add(Distinct([grid_z3[(i, j)] for i in line]))

    for i in in_sub_square:
        for j in in_sub_square:
            one_cell = []
            for di in in_sub_square:
                for dj in in_sub_square:
                    one_cell.append(grid_z3[(i * sub_square_size + di, j * sub_square_size + dj)])
            solver.add(Distinct(one_cell))

    for i in line:
        for j in line:
            if initial_grid[i][j]:
                solver.add(grid_z3[(i, j)] == initial_grid[i][j])

    if solver.check() == sat:
        end_time = time.time()
        model = solver.model()
        print(f"solution z3 in {end_time - start_time}s :")
        for i in line:
            print([model.evaluate(grid_z3[(i, j)]).as_long() for j in line])
    else:
        print("No solution found")
