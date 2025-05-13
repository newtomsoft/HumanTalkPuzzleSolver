from unittest import TestCase

import z3


class TentsSolverZ3:
    tree_value = -1

    def __init__(self, grid: list[list], tents_numbers_by_column_row):
        self._grid = grid
        self.tents_numbers_by_column_row: dict[str, list[int]] = tents_numbers_by_column_row
        self.rows_number = len(grid)
        self.columns_number = len(grid[0])
        self.columns_tents_numbers = self.tents_numbers_by_column_row['column']
        self.rows_tents_numbers = self.tents_numbers_by_column_row['row']
        self._solver = z3.Solver()
        self._grid_z3 = None

    def get_solution(self):
        self._grid_z3 = [[z3.Bool(f"grid_{r}_{c}") for c in range(self.columns_number)] for r in range(self.rows_number)]
        self._add_constraints()
        if self._solver.check() == z3.unsat:
            return [[]]
        model = self._solver.model()
        grid = [[1 if z3.is_true(model.evaluate(self._grid_z3[r][c])) else 0 for c in range(self.columns_number)] for r in range(self.rows_number)]
        return grid

    def _add_constraints(self):
        self._add_sum_constraints()
        self.add_free_if_no_tent_near_constraint()
        self.add_no_adjacent_tent_constraint()
        self.add_free_over_tree_constraint()
        self.add_one_tent_for_each_tree_constraint()

    def _add_sum_constraints(self):
        constraints = []
        for i, row in enumerate(self._grid_z3):
            constraints.append(z3.Sum([z3.If(cell, 1, 0) for cell in row]) == self.rows_tents_numbers[i])
        for i, column in enumerate(zip(*self._grid_z3)):
            constraints.append(z3.Sum([z3.If(cell, 1, 0) for cell in column]) == self.columns_tents_numbers[i])
        self._solver.add(constraints)

    def add_free_if_no_tent_near_constraint(self):
        for r in range(self.rows_number):
            for c in range(self.columns_number):
                if all(neighbor_value != TentsSolverZ3.tree_value for neighbor_value in self._get_neighbors_values(self._grid, r, c)):
                    self._solver.add(z3.Not(self._grid_z3[r][c]))

    def add_no_adjacent_tent_constraint(self):
        for r in range(self.rows_number):
            for c in range(self.columns_number):
                if r > 0:
                    self._solver.add(z3.Implies(self._grid_z3[r][c], z3.Not(self._grid_z3[r - 1][c])))
                    if c > 0:
                        self._solver.add(z3.Implies(self._grid_z3[r][c], z3.Not(self._grid_z3[r][c - 1])))
                        self._solver.add(z3.Implies(self._grid_z3[r][c], z3.Not(self._grid_z3[r - 1][c - 1])))
                    if c < self.columns_number - 1:
                        self._solver.add(z3.Implies(self._grid_z3[r][c], z3.Not(self._grid_z3[r][c + 1])))
                        self._solver.add(z3.Implies(self._grid_z3[r][c], z3.Not(self._grid_z3[r - 1][c + 1])))

                if r < self.rows_number - 1:
                    self._solver.add(z3.Implies(self._grid_z3[r][c], z3.Not(self._grid_z3[r + 1][c])))
                    if c > 0:
                        self._solver.add(z3.Implies(self._grid_z3[r][c], z3.Not(self._grid_z3[r][c - 1])))
                        self._solver.add(z3.Implies(self._grid_z3[r][c], z3.Not(self._grid_z3[r + 1][c - 1])))
                    if c < self.columns_number - 1:
                        self._solver.add(z3.Implies(self._grid_z3[r][c], z3.Not(self._grid_z3[r][c + 1])))
                        self._solver.add(z3.Implies(self._grid_z3[r][c], z3.Not(self._grid_z3[r + 1][c + 1])))

    def add_free_over_tree_constraint(self):
        for r in range(self.rows_number):
            for c in range(self.columns_number):
                if self._grid[r][c] == TentsSolverZ3.tree_value:
                    self._solver.add(z3.Not(self._grid_z3[r][c]))

    def add_one_tent_for_each_tree_constraint(self):
        for r in range(self.rows_number):
            for c in range(self.columns_number):
                if self._grid[r][c] == TentsSolverZ3.tree_value:
                    grid_z3_neighbors_values = self._get_neighbors_values(self._grid_z3, r, c)
                    self._solver.add(z3.Or(grid_z3_neighbors_values))

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


T = TentsSolverZ3.tree_value
_ = 0


class TentsSolverZ3Tests(TestCase):
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
        game_solver = TentsSolverZ3(grid, tents_numbers_by_column_row)
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
        game_solver = TentsSolverZ3(grid, tents_numbers_by_column_row)
        solution = game_solver.get_solution()
        self.assertEqual(expected_solution, solution)
