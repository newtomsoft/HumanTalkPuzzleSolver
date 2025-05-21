from d_Puzzle import sudokuSolverOrtools, sudokuSolverZ3

_ = 0

grid9x9 = [
    [_, 6, _, _, 5, _, _, 2, _],
    [_, _, _, 3, _, _, _, 9, _],
    [7, _, _, 6, _, _, _, 1, _],
    [_, _, 6, _, 3, _, 4, _, _],
    [_, _, 4, _, 7, _, 1, _, _],
    [_, _, 5, _, 9, _, 8, _, _],
    [_, 4, _, _, _, 1, _, _, 6],
    [_, 3, _, _, _, 8, _, _, _],
    [_, 2, _, _, 4, _, _, 5, _],
]

sudokuSolverOrtools.solve_sudoku(grid9x9)
sudokuSolverZ3.solve_sudoku(grid9x9)

