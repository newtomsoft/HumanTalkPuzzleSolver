from unittest import TestCase

from ortools.sat.python import cp_model


# noinspection DuplicatedCode
class TentsSolverORTools:
    tree_value = -1

    def __init__(self, grid: list[list], tents_numbers_by_column_row):
        self._grid = grid
        self.tents_numbers_by_column_row: dict[str, list[int]] = tents_numbers_by_column_row
        self.rows_number = len(grid)
        self.columns_number = len(grid[0])
        self.columns_tents_numbers = self.tents_numbers_by_column_row['column']
        self.rows_tents_numbers = self.tents_numbers_by_column_row['row']
        self._model = cp_model.CpModel()
        self._solver = cp_model.CpSolver()
        self._grid_ortools = None

    def get_solution(self):
        self._grid_ortools = [[self._model.NewBoolVar(f"grid_{r}_{c}") for c in range(self.columns_number)] for r in range(self.rows_number)]
        self._add_constraints()

        status = self._solver.Solve(self._model)
        if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
            grid = [[1 if self._solver.Value(self._grid_ortools[r][c]) else 0 for c in range(self.columns_number)] for r in range(self.rows_number)]
            return grid
        else:
            return [[]]

    def _add_constraints(self):
        self._add_sum_constraints()
        self.add_free_if_no_tent_near_constraint()
        self.add_no_adjacent_tent_constraint()
        self.add_free_over_tree_constraint()
        self.add_one_tent_for_each_tree_constraint()

    def _add_sum_constraints(self):
        for i in range(self.rows_number):
            self._model.Add(sum(self._grid_ortools[i]) == self.rows_tents_numbers[i])

        for j in range(self.columns_number):
            column_sum = sum(self._grid_ortools[i][j] for i in range(self.rows_number))
            self._model.Add(column_sum == self.columns_tents_numbers[j])

    def add_free_if_no_tent_near_constraint(self):
        for r in range(self.rows_number):
            for c in range(self.columns_number):
                if all(neighbor_value != TentsSolverORTools.tree_value for neighbor_value in self._get_neighbors_values(self._grid, r, c)):
                    self._model.Add(self._grid_ortools[r][c] == 0)

    def add_no_adjacent_tent_constraint(self):
        for r in range(self.rows_number):
            for c in range(self.columns_number):
                # Check all 8 adjacent cells
                adjacent_cells = []

                # Horizontal and vertical adjacents
                if r > 0:
                    adjacent_cells.append(self._grid_ortools[r - 1][c])
                if r < self.rows_number - 1:
                    adjacent_cells.append(self._grid_ortools[r + 1][c])
                if c > 0:
                    adjacent_cells.append(self._grid_ortools[r][c - 1])
                if c < self.columns_number - 1:
                    adjacent_cells.append(self._grid_ortools[r][c + 1])

                # Diagonal adjacents
                if r > 0 and c > 0:
                    adjacent_cells.append(self._grid_ortools[r - 1][c - 1])
                if r > 0 and c < self.columns_number - 1:
                    adjacent_cells.append(self._grid_ortools[r - 1][c + 1])
                if r < self.rows_number - 1 and c > 0:
                    adjacent_cells.append(self._grid_ortools[r + 1][c - 1])
                if r < self.rows_number - 1 and c < self.columns_number - 1:
                    adjacent_cells.append(self._grid_ortools[r + 1][c + 1])

                # If this cell is a tent, all adjacent cells cannot be tents
                for adjacent_cell in adjacent_cells:
                    self._model.AddImplication(self._grid_ortools[r][c], adjacent_cell.Not())

    def add_free_over_tree_constraint(self):
        for r in range(self.rows_number):
            for c in range(self.columns_number):
                if self._grid[r][c] == TentsSolverORTools.tree_value:
                    self._model.Add(self._grid_ortools[r][c] == 0)

    def add_one_tent_for_each_tree_constraint(self):
        for r in range(self.rows_number):
            for c in range(self.columns_number):
                if self._grid[r][c] == TentsSolverORTools.tree_value:
                    grid_ortools_neighbors = self._get_neighbors_values(self._grid_ortools, r, c)
                    self._model.AddBoolOr(grid_ortools_neighbors)

    def _get_neighbors_values(self, grid, r, c):
        neighbors_values = []
        if r > 0:
            neighbors_values.append(grid[r - 1][c])
        if r < self.rows_number - 1:
            neighbors_values.append(grid[r + 1][c])
        if c > 0:
            neighbors_values.append(grid[r][c - 1])
        if c < self.columns_number - 1:
            neighbors_values.append(grid[r][c + 1])
        return neighbors_values


T = TentsSolverORTools.tree_value
_ = 0


# noinspection DuplicatedCode
class TentsSolverORToolsTests(TestCase):
    def test_solution_6x6(self):
        grid = [
            [_, _, _, T, _, _],
            [T, _, _, _, _, _],
            [_, _, _, _, T, _],
            [_, T, T, _, _, _],
            [_, _, _, _, _, T],
            [_, T, _, _, _, _]
        ]
        tents_numbers_by_column_row = {'column': [2, 1, 1, 1, 1, 1], 'row': [2, 1, 1, 1, 0, 2]}
        expected_solution = [
            [1, _, 1, _, _, _],
            [_, _, _, _, 1, _],
            [_, 1, _, _, _, _],
            [_, _, _, 1, _, _],
            [_, _, _, _, _, _],
            [1, _, _, _, _, 1]
        ]
        game_solver = TentsSolverORTools(grid, tents_numbers_by_column_row)
        solution = game_solver.get_solution()
        self.assertEqual(expected_solution, solution)

    def test_solution_10x10(self):
        grid = [
            [_, _, _, _, _, _, _, _, _, _],
            [T, _, T, _, _, T, _, T, _, _],
            [T, T, _, _, T, _, _, _, _, T],
            [_, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, T, _, T],
            [_, T, _, T, T, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _],
            [_, _, T, T, _, T, _, _, _, T],
            [_, T, _, _, _, _, _, T, _, _],
            [_, _, _, _, _, _, _, T, _, _]
        ]
        tents_numbers_by_column_row = {'column': [3, 2, 3, 1, 2, 1, 2, 1, 3, 2], 'row': [2, 3, 1, 3, 1, 3, 1, 2, 2, 2]}
        expected_solution = [
            [1, _, 1, _, _, _, _, _, _, _],
            [_, _, _, _, 1, _, 1, _, 1, _],
            [_, _, 1, _, _, _, _, _, _, _],
            [1, _, _, _, _, _, _, 1, _, 1],
            [_, _, _, _, 1, _, _, _, _, _],
            [1, _, 1, _, _, _, _, _, _, 1],
            [_, _, _, _, _, 1, _, _, _, _],
            [_, 1, _, _, _, _, _, _, 1, _],
            [_, _, _, 1, _, _, 1, _, _, _],
            [_, 1, _, _, _, _, _, _, 1, _]
        ]
        game_solver = TentsSolverORTools(grid, tents_numbers_by_column_row)
        solution = game_solver.get_solution()
        self.assertEqual(expected_solution, solution)
