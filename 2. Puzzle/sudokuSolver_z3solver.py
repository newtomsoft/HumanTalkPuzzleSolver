from z3 import Solver, Int, sat, Distinct


def solve_sudoku() -> None:
    solver = Solver()

    cell_size = 3
    line_size = cell_size**2
    line = list(range(0, line_size))
    cell = list(range(0, cell_size))

    initial_grid = [
        [0, 6, 0, 0, 5, 0, 0, 2, 0],
        [0, 0, 0, 3, 0, 0, 0, 9, 0],
        [7, 0, 0, 6, 0, 0, 0, 1, 0],
        [0, 0, 6, 0, 3, 0, 4, 0, 0],
        [0, 0, 4, 0, 7, 0, 1, 0, 0],
        [0, 0, 5, 0, 9, 0, 8, 0, 0],
        [0, 4, 0, 0, 0, 1, 0, 0, 6],
        [0, 3, 0, 0, 0, 8, 0, 0, 0],
        [0, 2, 0, 0, 4, 0, 0, 5, 0],
    ]

    # Create variables for each cell
    grid = {}
    for i in line:
        for j in line:
            grid[(i, j)] = Int(f"cell{i}_{j}")
            # Each cell contains a value between 1 and 9
            solver.add(grid[(i, j)] >= 1, grid[(i, j)] <= line_size)

    # AllDifferent on rows
    for i in line:
        solver.add(Distinct([grid[(i, j)] for j in line]))

    # AllDifferent on columns
    for j in line:
        solver.add(Distinct([grid[(i, j)] for i in line]))

    # AllDifferent on cells
    for i in cell:
        for j in cell:
            one_cell = []
            for di in cell:
                for dj in cell:
                    one_cell.append(grid[(i * cell_size + di, j * cell_size + dj)])
            solver.add(Distinct(one_cell))

    # Initial values
    for i in line:
        for j in line:
            if initial_grid[i][j]:
                solver.add(grid[(i, j)] == initial_grid[i][j])

    # Solve and print out the solution
    if solver.check() == sat:
        model = solver.model()
        for i in line:
            print([model.evaluate(grid[(i, j)]).as_long() for j in line])
    else:
        print("No solution found")


solve_sudoku()
