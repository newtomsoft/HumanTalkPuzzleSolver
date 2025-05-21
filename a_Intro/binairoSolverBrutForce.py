from unittest import TestCase, skip


# noinspection DuplicatedCode
class BinairoSolverBrutForce:
    def __init__(self, grid: list[list]):
        self._grid = grid
        self.rows_number = len(grid)
        self.columns_number = len(grid[0])
        self._solution = [[cell if cell != -1 else None for cell in row] for row in grid]

    def get_solution(self):
        # Create a list of unknown cells (cells with value -1)
        unknown_cells = []
        for r in range(self.rows_number):
            for c in range(self.columns_number):
                if self._grid[r][c] == -1:
                    unknown_cells.append((r, c))

        # Try to solve using backtracking
        if self._solve(unknown_cells, 0):
            return self._solution
        else:
            return [[]]

    def _solve(self, unknown_cells, index):
        # Base case: all unknown cells have been assigned
        if index >= len(unknown_cells):
            return self._is_valid_solution()

        r, c = unknown_cells[index]

        # Try placing a 0
        self._solution[r][c] = 0
        if self._is_valid_partial_solution(r, c) and self._solve(unknown_cells, index + 1):
            return True

        # Try placing a 1
        self._solution[r][c] = 1
        if self._is_valid_partial_solution(r, c) and self._solve(unknown_cells, index + 1):
            return True

        # Neither option worked, backtrack
        self._solution[r][c] = None
        return False

    def _is_valid_partial_solution(self, row, col):
        """Check if the current partial solution is valid after placing a value at (row, col)."""
        # Check for more than two adjacent same digits horizontally
        if col >= 2:
            if (self._solution[row][col] is not None and
                    self._solution[row][col - 1] is not None and
                    self._solution[row][col - 2] is not None and
                    self._solution[row][col] == self._solution[row][col - 1] == self._solution[row][col - 2]):
                return False

        # Check for more than two adjacent same digits vertically
        if row >= 2:
            if (self._solution[row][col] is not None and
                    self._solution[row - 1][col] is not None and
                    self._solution[row - 2][col] is not None and
                    self._solution[row][col] == self._solution[row - 1][col] == self._solution[row - 2][col]):
                return False

        # Check if the row has too many 0s or 1s
        row_values = [cell for cell in self._solution[row] if cell is not None]
        if row_values.count(0) > self.columns_number // 2 or row_values.count(1) > self.columns_number // 2:
            return False

        # Check if the column has too many 0s or 1s
        col_values = [self._solution[r][col] for r in range(self.rows_number) if self._solution[r][col] is not None]
        if col_values.count(0) > self.rows_number // 2 or col_values.count(1) > self.rows_number // 2:
            return False

        # Check for duplicate rows
        for r in range(self.rows_number):
            if r != row and all(self._solution[r][c] is not None and self._solution[row][c] is not None for c in range(self.columns_number)):
                if all(self._solution[r][c] == self._solution[row][c] for c in range(self.columns_number)):
                    return False

        # Check for duplicate columns
        for c in range(self.columns_number):
            if c != col and all(self._solution[r][c] is not None and self._solution[r][col] is not None for r in range(self.rows_number)):
                if all(self._solution[r][c] == self._solution[r][col] for r in range(self.rows_number)):
                    return False

        return True

    def _is_valid_solution(self):
        """Check if the complete solution is valid."""
        # Check for more than two adjacent same digits horizontally
        for row in range(self.rows_number):
            for col in range(self.columns_number - 2):
                if self._solution[row][col] == self._solution[row][col + 1] == self._solution[row][col + 2]:
                    return False

        # Check for more than two adjacent same digits vertically
        for col in range(self.columns_number):
            for row in range(self.rows_number - 2):
                if self._solution[row][col] == self._solution[row + 1][col] == self._solution[row + 2][col]:
                    return False

        # Check if each row has equal number of 0s and 1s
        for row in self._solution:
            if row.count(0) != row.count(1):
                return False

        # Check if each column has equal number of 0s and 1s
        for col in range(self.columns_number):
            column = [self._solution[row][col] for row in range(self.rows_number)]
            if column.count(0) != column.count(1):
                return False

        # Check for duplicate rows
        for i in range(self.rows_number):
            for j in range(i + 1, self.rows_number):
                if self._solution[i] == self._solution[j]:
                    return False

        # Check for duplicate columns
        for i in range(self.columns_number):
            col_i = [self._solution[row][i] for row in range(self.rows_number)]
            for j in range(i + 1, self.columns_number):
                col_j = [self._solution[row][j] for row in range(self.rows_number)]
                if col_i == col_j:
                    return False

        return True


_ = -1


# noinspection DuplicatedCode
class BinairoSolverBrutForceTests(TestCase):
    def test_solution_8x8(self):
        grid = [
            [_, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, 1, _],
            [_, _, _, _, 1, _, _, 1],
            [1, _, _, _, _, _, _, _],
            [_, _, _, 1, _, 1, _, 0],
            [1, _, _, _, _, _, _, _],
            [1, _, _, 0, 0, _, _, _],
            [_, _, 0, 0, _, _, 0, _],
        ]
        expected_grid = [
            [1, 0, 1, 1, 0, 0, 1, 0],
            [0, 1, 1, 0, 0, 1, 1, 0],
            [0, 1, 0, 1, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 1],
            [0, 1, 0, 1, 0, 1, 1, 0],
            [1, 0, 0, 1, 1, 0, 1, 0],
            [1, 0, 1, 0, 0, 1, 0, 1],
            [0, 1, 0, 0, 1, 1, 0, 1],
        ]
        game_solver = BinairoSolverBrutForce(grid)
        solution = game_solver.get_solution()
        self.assertEqual(expected_grid, solution)

    def test_solution_10x10(self):
        grid = [
            [0, 0, 1, 0, 1, 0, 1, _, _, 1],
            [_, _, 0, 1, 0, 1, _, _, 1, 0],
            [_, _, 1, 0, 1, 0, 0, 1, 0, 1],
            [_, _, 0, 1, _, _, 1, 0, 1, 0],
            [1, _, _, 0, _, _, _, _, _, 0],
            [_, 0, _, _, 1, _, _, 1, 0, 1],
            [_, _, _, _, _, 1, _, 0, 1, 0],
            [_, 1, _, _, _, _, _, 0, 1, 0],
            [0, _, _, _, _, _, _, 1, 0, 1],
            [_, _, _, _, 1, _, _, _, _, 1],
        ]
        expected_grid = [
            [0, 0, 1, 0, 1, 0, 1, 1, 0, 1],
            [1, 1, 0, 1, 0, 1, 0, 0, 1, 0],
            [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
            [1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
            [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
            [0, 1, 1, 0, 0, 1, 1, 0, 1, 0],
            [1, 1, 0, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 1, 0, 1, 0, 0, 1],
        ]
        game_solver = BinairoSolverBrutForce(grid)
        solution = game_solver.get_solution()
        self.assertEqual(expected_grid, solution)

    @skip("too long")
    def test_solution_20x20(self):
        grid = [
            [_, _, _, _, 0, 1, _, _, 0, 0, _, _, _, _, _, _, 0, _, _, 0],
            [_, 0, _, 1, _, _, _, _, _, 1, _, _, _, 1, _, _, 1, 1, _, _],
            [_, 0, _, _, 0, _, _, _, _, _, _, 0, _, _, _, _, _, 0, _, _],
            [_, _, _, _, 1, _, _, 0, _, _, _, _, 1, _, _, _, _, _, _, _],
            [_, _, 1, _, _, _, _, 0, _, _, _, 1, _, _, _, _, 0, _, _, _],
            [_, _, _, 0, _, _, _, _, _, _, _, _, 0, _, _, _, _, 1, _, _],
            [_, 0, 1, _, _, _, _, _, _, _, 0, _, _, 1, _, _, 1, 1, _, 0],
            [_, _, _, 1, _, _, _, _, _, 1, _, _, _, _, _, 0, _, _, _, _],
            [1, _, _, _, 0, _, _, _, _, 1, _, _, _, 0, _, _, _, _, 1, _],
            [_, 1, _, _, _, _, 0, 0, _, _, _, _, 1, _, _, _, _, _, _, _],
            [_, _, _, 0, _, _, _, _, 0, _, _, _, _, _, _, 0, 0, _, _, _],
            [_, _, _, 0, _, 0, _, _, _, _, 1, 0, _, _, 0, _, _, _, _, 0],
            [_, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, 1, 1],
            [0, _, _, _, _, 1, _, 1, _, _, 0, _, _, _, _, 0, _, _, _, _],
            [_, _, _, _, _, _, _, 1, _, _, 0, _, 0, 1, _, _, _, _, _, 1],
            [_, 1, _, _, _, 1, _, _, _, _, _, 1, _, _, 0, _, _, _, 1, _],
            [1, 1, _, _, _, _, _, _, 0, _, _, _, _, _, _, _, 1, _, _, 1],
            [_, _, _, _, _, 1, _, _, _, 1, _, _, _, _, _, _, _, _, 1, _],
            [_, _, 1, _, 0, _, _, _, _, 1, _, _, _, 0, _, _, _, _, _, _],
            [_, _, 1, _, _, _, 1, _, 0, _, _, _, _, 1, _, _, 0, _, _, _]
        ]
        expected_grid = [
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0],
            [1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1],
            [0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0],
            [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0],
            [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1],
            [0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
            [1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0],
            [1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
            [0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1],
            [0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
        ]
        game_solver = BinairoSolverBrutForce(grid)
        solution = game_solver.get_solution()
        self.assertEqual(expected_grid, solution)
