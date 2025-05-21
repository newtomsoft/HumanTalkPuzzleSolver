import time

from ortools.sat.python import cp_model

_ = 0


# noinspection DuplicatedCode
def solve_sudoku(initial_grid: list[list]) -> None:
    start_time = time.time()
    model = cp_model.CpModel()

    line_size = len(initial_grid)
    cell_size = int(line_size ** 0.5)
    line = list(range(0, line_size))
    cell = list(range(0, cell_size))

    print("initial grid:")
    for i in line:
        print([initial_grid[i][j] for j in line])

    grid = {}
    for i in line:
        for j in line:
            grid[(i, j)] = model.new_int_var(1, line_size, "grid %i %i" % (i, j))

    for i in line:
        model.add_all_different(grid[(i, j)] for j in line)

    for j in line:
        model.add_all_different(grid[(i, j)] for i in line)

    for i in cell:
        for j in cell:
            one_cell = []
            for di in cell:
                for dj in cell:
                    one_cell.append(grid[(i * cell_size + di, j * cell_size + dj)])

            model.add_all_different(one_cell)

    for i in line:
        for j in line:
            if initial_grid[i][j]:
                model.add(grid[(i, j)] == initial_grid[i][j])

    solver = cp_model.CpSolver()
    status = solver.solve(model)
    if status == cp_model.OPTIMAL:
        end_time = time.time()
        print(f"solution ortools in {end_time - start_time}s :")
        for i in line:
            print([int(solver.value(grid[(i, j)])) for j in line])
