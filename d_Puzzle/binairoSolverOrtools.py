from unittest import TestCase

from ortools.sat.python import cp_model


# noinspection DuplicatedCode
class BinairoSolverORTools:
    def __init__(self, grid: list[list]):
        self._grid = grid
        self.rows_number = len(grid)
        self.columns_number = len(grid[0])
        self._model = cp_model.CpModel()
        self._grid_ortools = None

    def get_solution(self) -> list[list]:
        self._grid_ortools = [[self._model.new_bool_var(f"cell{r}_{c}") for c in range(self.columns_number)] for r in range(self.rows_number)]
        self._add_constraints()

        solver = cp_model.CpSolver()
        status = solver.solve(self._model)

        if status != cp_model.OPTIMAL and status != cp_model.FEASIBLE:
            return [[]]

        return [[solver.value(self._grid_ortools[r][c]) for c in range(self.columns_number)] for r in range(self.rows_number)]

    def _add_constraints(self):
        self._add_initial_constraints()
        self._add_half_true_false_by_line_constraints()
        self._add_not_same_3_adjacent_constraints()
        self._add_unique_line_constraints()

    def _add_initial_constraints(self):
        for r in range(self.rows_number):
            for c in range(self.columns_number):
                if self._grid[r][c] == 1:
                    self._model.add(self._grid_ortools[r][c] == 1)
                    continue
                if self._grid[r][c] == 0:
                    self._model.add(self._grid_ortools[r][c] == 0)
                    continue

    def _add_half_true_false_by_line_constraints(self):
        half_columns = self.columns_number // 2
        half_rows = self.rows_number // 2
        for row in range(self.rows_number):
            self._model.add(sum([self._grid_ortools[row][col] for col in range(self.columns_number)]) == half_columns)
        for col in range(self.columns_number):
            self._model.add(sum([self._grid_ortools[row][col] for row in range(self.rows_number)]) == half_rows)

    def _add_not_same_3_adjacent_constraints(self):
        for row in range(self.rows_number):
            for col in range(self.columns_number - 2):
                self._model.add(self._grid_ortools[row][col] + self._grid_ortools[row][col + 1] + self._grid_ortools[row][col + 2] != 0)
                self._model.add(self._grid_ortools[row][col] + self._grid_ortools[row][col + 1] + self._grid_ortools[row][col + 2] != 3)

        for col in range(self.columns_number):
            for row in range(self.rows_number - 2):
                self._model.add(self._grid_ortools[row][col] + self._grid_ortools[row + 1][col] + self._grid_ortools[row + 2][col] != 0)
                self._model.add(self._grid_ortools[row][col] + self._grid_ortools[row + 1][col] + self._grid_ortools[row + 2][col] != 3)

    def _add_unique_line_constraints(self):
        for row0 in range(1, self.rows_number):
            for row1 in range(row0):
                diff_vars = []
                for col in range(self.columns_number):
                    diff_var = self._model.new_bool_var(f"row_diff_{row0}_{row1}_{col}")
                    self._model.add(self._grid_ortools[row0][col] != self._grid_ortools[row1][col]).OnlyEnforceIf(diff_var)
                    self._model.add(self._grid_ortools[row0][col] == self._grid_ortools[row1][col]).OnlyEnforceIf(diff_var.Not())
                    diff_vars.append(diff_var)
                self._model.add(sum(diff_vars) >= 1)

        for col0 in range(1, self.columns_number):
            for col1 in range(col0):
                diff_vars = []
                for row in range(self.rows_number):
                    diff_var = self._model.new_bool_var(f"col_diff_{col0}_{col1}_{row}")
                    self._model.add(self._grid_ortools[row][col0] != self._grid_ortools[row][col1]).OnlyEnforceIf(diff_var)
                    self._model.add(self._grid_ortools[row][col0] == self._grid_ortools[row][col1]).OnlyEnforceIf(diff_var.Not())
                    diff_vars.append(diff_var)
                self._model.add(sum(diff_vars) >= 1)


_ = -1


# noinspection DuplicatedCode
class BinairoSolverORToolsTests(TestCase):
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
        game_solver = BinairoSolverORTools(grid)
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
        game_solver = BinairoSolverORTools(grid)
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
        game_solver = BinairoSolverORTools(grid)
        solution = game_solver.get_solution()
        self.assertEqual(expected_grid, solution)
