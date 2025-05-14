from unittest import TestCase

from z3 import Not, unsat, Bool, Solver, And, is_true, Or


class BinairoSolverZ3:
    def __init__(self, grid: list[list]):
        self._grid = grid
        self.rows_number = len(grid)
        self.columns_number = len(grid[0])
        self._solver = Solver()
        self._grid_z3 = None

    def get_solution(self) -> list[list]:
        self._grid_z3 = [[Bool(f"cell{r}_{c}") for c in range(self.columns_number)] for r in range(self.rows_number)]
        self._add_constraints()

        if self._solver.check() == unsat:
            return [[]]

        model = self._solver.model()
        return [[is_true(model.eval(self._grid_z3[r][c])) for c in range(self.columns_number)] for r in range(self.rows_number)]

    def _add_constraints(self):
        self._add_initial_constraints()
        self._add_half_true_false_by_line_constraints()
        self._add_not_same_3_adjacent_constraints()
        self._add_unique_line_constraints()

    def _add_initial_constraints(self):
        for r in range(self.rows_number):
            for c in range(self.columns_number):
                if self._grid[r][c] == 1:
                    self._solver.add(self._grid_z3[r][c])
                    continue
                if self._grid[r][c] == 0:
                    self._solver.add(Not(self._grid_z3[r][c]))
                    continue

    def _add_half_true_false_by_line_constraints(self):
        half_columns = self.columns_number // 2
        half_rows = self.rows_number // 2
        for row_z3 in self._grid_z3:
            self._solver.add(sum([row_z3[col] for col in range(self.columns_number)]) == half_columns)
        for column_z3 in zip(*self._grid_z3):
            self._solver.add(sum([column_z3[row] for row in range(self.rows_number)]) == half_rows)

    def _add_not_same_3_adjacent_constraints(self):
        for row in range(self.rows_number):
            for col in range(self.columns_number - 2):
                self._solver.add(Or(self._grid_z3[row][col] != self._grid_z3[row][col + 1], self._grid_z3[row][col + 1] != self._grid_z3[row][col + 2]))
        for col in range(self.columns_number):
            for row in range(self.rows_number - 2):
                self._solver.add(Or(self._grid_z3[row][col] != self._grid_z3[row + 1][col], self._grid_z3[row + 1][col] != self._grid_z3[row + 2][col]))

    def _add_unique_line_constraints(self):
        for row0 in range(1, self.rows_number):
            for row1 in range(row0):
                self._solver.add(Not(And([self._grid_z3[row0][col] == self._grid_z3[row1][col] for col in range(self.columns_number)])))
        for col0 in range(1, self.columns_number):
            for col1 in range(col0):
                self._solver.add(Not(And([self._grid_z3[row][col0] == self._grid_z3[row][col1] for row in range(self.rows_number)])))


_ = -1


# noinspection DuplicatedCode
class BinairoSolverZ3Tests(TestCase):
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
        game_solver = BinairoSolverZ3(grid)
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
        game_solver = BinairoSolverZ3(grid)
        solution = game_solver.get_solution()
        self.assertEqual(expected_grid, solution)

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
        game_solver = BinairoSolverZ3(grid)
        solution = game_solver.get_solution()
        self.assertEqual(expected_grid, solution)
