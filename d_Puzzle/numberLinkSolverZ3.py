from unittest import TestCase

from z3 import Solver, Int, sat, If, And, Or, Sum

_ = -1


class NumberLinkSolverZ3:
    def __init__(self, grid: list[list]):
        self._grid = grid
        self.rows_number = len(grid)
        self.columns_number = len(grid[0])
        self._solver = Solver()
        self._grid_z3 = None

    def get_solution(self):
        self._grid_z3 = {}
        for r in range(self.rows_number):
            for c in range(self.columns_number):
                self._grid_z3[(r, c)] = Int(f"cell{r}_{c}")
                self._solver.add(self._grid_z3[(r, c)] >= 0)
                self._solver.add(self._grid_z3[(r, c)] <= max(self.rows_number, self.columns_number))

        self._add_constraints()

        if self._solver.check() == sat:
            model = self._solver.model()
            return [[model.evaluate(self._grid_z3[(r, c)]).as_long() for c in range(self.columns_number)] for r in range(self.rows_number)]
        else:
            return [[]]

    def _add_constraints(self):
        self._add_initial_constraints()
        self._add_neighbors_count_constraints()

    def _add_initial_constraints(self):
        for r in range(self.rows_number):
            for c in range(self.columns_number):
                value = self._grid[r][c]
                if value >= 0:
                    self._solver.add(self._grid_z3[(r, c)] == value)

    def _add_neighbors_count_constraints(self):
        for r in range(self.rows_number):
            for c in range(self.columns_number):
                neighbors_positions = []
                if r > 0:
                    neighbors_positions.append((r - 1, c))
                if r < self.rows_number - 1:
                    neighbors_positions.append((r + 1, c))
                if c > 0:
                    neighbors_positions.append((r, c - 1))
                if c < self.columns_number - 1:
                    neighbors_positions.append((r, c + 1))

                same_value_neighbors = []
                for neighbor_pos in neighbors_positions:
                    same_value = self._grid_z3[(r, c)] == self._grid_z3[neighbor_pos]
                    same_value_neighbors.append(same_value)

                if self._grid[r][c] >= 0:
                    self._solver.add(Sum(same_value_neighbors) == 1)
                else:
                    self._solver.add(Sum(same_value_neighbors) == 2)


# noinspection PyShadowingNames
class Test(TestCase):
    def test_solution_basic_grid(self):
        grid = [
            [1, 2, _],
            [_, 3, 2],
            [1, _, 3]
        ]
        game_solver = NumberLinkSolverZ3(grid)
        solution = game_solver.get_solution()
        expected_solution = [
            [1, 2, 2],
            [1, 3, 2],
            [1, 3, 3],
        ]
        self.assertEqual(expected_solution, solution)

    def test_solution_15x15(self):
        grid = [
            [_, _, _, _, _, _, _, _, 3, 4, 9, _, _, _, _],
            [_, _, _, _, 3, _, 5, 6, _, _, _, _, 7, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, 6, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, 9, _, _],
            [_, _, _, _, 4, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, 7, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, 10, _, 8, _, _],
            [_, _, _, 1, 2, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, 5, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, 8, _, _, _, _, _, _],
            [_, _, _, 2, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, 1, _, _, _, _, _, _, _, 10, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
        ]
        game_solver = NumberLinkSolverZ3(grid)
        solution = game_solver.get_solution()
        expected_solution = [
            [6, 6, 6, 6, 6, 6, 6, 6, 3, 4, 9, 6, 6, 6, 6],
            [6, 3, 3, 3, 3, 5, 5, 6, 3, 4, 9, 6, 7, 7, 6],
            [6, 3, 5, 5, 5, 5, 3, 3, 3, 4, 9, 6, 6, 7, 6],
            [6, 3, 5, 3, 3, 3, 3, 4, 4, 4, 9, 9, 9, 7, 6],
            [6, 3, 5, 3, 4, 4, 4, 4, 7, 7, 7, 7, 7, 7, 6],
            [6, 3, 5, 3, 3, 3, 3, 3, 7, 3, 3, 3, 3, 3, 6],
            [6, 3, 5, 1, 1, 1, 1, 3, 3, 3, 10, 10, 8, 3, 6],
            [6, 3, 5, 1, 2, 2, 1, 1, 1, 1, 1, 10, 8, 3, 6],
            [6, 3, 5, 5, 5, 2, 2, 2, 2, 2, 1, 10, 8, 3, 6],
            [6, 3, 8, 8, 8, 8, 8, 8, 8, 2, 1, 10, 8, 3, 6],
            [6, 3, 8, 2, 2, 2, 2, 2, 2, 2, 1, 10, 8, 3, 6],
            [6, 3, 8, 1, 1, 1, 1, 1, 1, 1, 1, 10, 8, 3, 6],
            [6, 3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 3, 6],
            [6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 6],
            [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        ]
        self.assertEqual(expected_solution, solution)
