from unittest import TestCase, skip


class MinesweeperSolverBrutForce:
    def __init__(self, grid: list[list]):
        self._grid = grid
        self.rows_number = len(grid)
        self.columns_number = len(grid[0])
        self._solution = [[0 for _ in range(self.columns_number)] for _ in range(self.rows_number)]

    def get_solution(self):
        # Create a list of unknown cells (cells with value _)
        unknown_cells = []
        for r in range(self.rows_number):
            for c in range(self.columns_number):
                if self._grid[r][c] == _:
                    unknown_cells.append((r, c))

        # Start with all cells set to 0 (no mines)
        self._solution = [[0 for _ in range(self.columns_number)] for _ in range(self.rows_number)]

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

        # Try placing a mine (1)
        self._solution[r][c] = 1
        if self._is_valid_partial_solution() and self._solve(unknown_cells, index + 1):
            return True

        # Try not placing a mine (0)
        self._solution[r][c] = 0
        if self._is_valid_partial_solution() and self._solve(unknown_cells, index + 1):
            return True

        # Neither option worked, backtrack
        return False

    def _is_valid_partial_solution(self):
        """Check if the current partial solution is valid for all known cells."""
        for r in range(self.rows_number):
            for c in range(self.columns_number):
                if self._grid[r][c] != _:  # Only check cells with known values
                    # A cell with a known value cannot have a mine
                    if self._solution[r][c] == 1:
                        return False

                    # Count mines around this cell
                    mines_count = self._count_mines_around(r, c)

                    # If the count exceeds the grid value, it's invalid
                    if mines_count > self._grid[r][c]:
                        return False
        return True

    def _is_valid_solution(self):
        """Check if the complete solution is valid."""
        for r in range(self.rows_number):
            for c in range(self.columns_number):
                if self._grid[r][c] != _:  # Only check cells with known values
                    # A cell with a known value cannot have a mine
                    if self._solution[r][c] == 1:
                        return False

                    # Count mines around this cell
                    mines_count = self._count_mines_around(r, c)

                    # The count must match the grid value
                    if mines_count != self._grid[r][c]:
                        return False
        return True

    def _count_mines_around(self, r, c):
        """Count the number of mines around a cell."""
        count = 0
        for dr in [_, 0, 1]:
            for dc in [_, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.rows_number and 0 <= nc < self.columns_number:
                    count += self._solution[nr][nc]
        return count


_ = -1


class Test(TestCase):
    def test_solution_basic_grid(self):
        grid = [
            [_, _, _],
            [_, 1, 1],
            [_, 1, _]
        ]
        game_solver = MinesweeperSolverBrutForce(grid)
        solution = game_solver.get_solution()
        expected_solution = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 1]
        ]
        self.assertEqual(expected_solution, solution)

    def test_solution_5x5_16(self):
        grid = [
            [_, _, _, 1, _],
            [1, _, 3, _, 3],
            [2, _, _, _, _],
            [_, 1, _, 4, 4],
            [_, _, _, _, _],
        ]
        game_solver = MinesweeperSolverBrutForce(grid)
        solution = game_solver.get_solution()
        expected_solution = [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1]
        ]
        self.assertEqual(expected_solution, solution)

    def test_solution_7x7_easy_30(self):
        grid = [
            [_, 1, _, _, 1, 1, _],
            [_, _, 2, 1, _, _, 0],
            [3, _, _, _, 3, 3, _],
            [2, _, 2, _, _, _, _],
            [1, _, _, _, 2, _, _],
            [_, 1, 2, _, 1, 2, _],
            [1, _, _, _, _, _, 1]
        ]
        game_solver = MinesweeperSolverBrutForce(grid)
        solution = game_solver.get_solution()
        expected_solution = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 1, 0, 0, 0]
        ]
        self.assertEqual(expected_solution, solution)

    @skip("2mn for this test")
    def test_solution_7x7_32(self):
        grid = [
            [_, 2, _, _, _, _, _],
            [_, _, 3, _, 2, 2, _],
            [2, _, _, _, 2, _, _],
            [_, 1, 2, _, _, 1, _],
            [_, _, _, _, 3, _, 2],
            [_, 2, _, _, _, _, 2],
            [2, _, 2, 1, _, _, 1],
        ]
        game_solver = MinesweeperSolverBrutForce(grid)
        solution = game_solver.get_solution()
        expected_solution = [
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 1],
            [0, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 1, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(expected_solution, solution)

    @skip("7 years for this test ?")
    def test_solution_10x10_64(self):
        grid = [
            [_, 1, _, _, _, _, 2, _, _, _],
            [1, 2, _, 2, _, 2, _, 1, 1, 1],
            [0, _, _, _, _, _, 1, _, _, _],
            [1, _, 1, _, 1, 1, _, _, 2, _],
            [_, _, _, _, 2, _, _, _, 4, _],
            [_, _, _, _, 4, _, _, _, _, 2],
            [2, _, 4, 4, _, _, _, 4, 4, _],
            [1, _, 3, _, _, _, _, _, _, _],
            [_, _, 3, _, 3, _, _, 1, 2, 2],
            [_, 0, _, _, _, 1, 1, _, _, 1]
        ]
        game_solver = MinesweeperSolverBrutForce(grid)
        solution = game_solver.get_solution()
        expected_solution = [
            [1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
            [1, 0, 1, 1, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        ]
        self.assertEqual(expected_solution, solution)
