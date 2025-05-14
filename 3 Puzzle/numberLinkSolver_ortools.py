from unittest import TestCase

from ortools.sat.python import cp_model

_ = -1


class NumberLinkSolverORTools:
    def __init__(self, grid: list[list]):
        self._grid = grid
        self.rows_number = len(grid)
        self.columns_number = len(grid[0])
        self._model = cp_model.CpModel()
        self._solver = cp_model.CpSolver()
        self._grid_ortools = None
        self._previous_solution_constraints = []

    def get_solution(self):
        self._grid_ortools = [[self._model.NewIntVar(0, max(self.rows_number, self.columns_number), f"cell{r}_{c}") for c in range(self.columns_number)] for r in range(self.rows_number)]
        self._add_constraints()

        status = self._solver.Solve(self._model)
        if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
            return [[(self._solver.Value(self._grid_ortools[r][c])) for c in range(self.columns_number)] for r in range(self.rows_number)]
        else:
            return [[]]

    def _add_constraints(self):
        self._add_initial_constraints()
        self._add_neighbors_count_constraints()

    def _add_initial_constraints(self):
        for r in range(self.rows_number):
            for c in range(self.columns_number):
                value = self._grid[r][c]
                if value >= 1:
                    self._model.Add(self._grid_ortools[r][c] == value)
                else:
                    self._model.Add(self._grid_ortools[r][c] >= 1)

    def _add_neighbors_count_constraints(self):
        for r in range(self.rows_number):
            for c in range(self.columns_number):
                neighbors_values = []
                if r > 0:
                    neighbors_values.append(self._grid_ortools[r - 1][c])
                if r < self.rows_number - 1:
                    neighbors_values.append(self._grid_ortools[r + 1][c])
                if c > 0:
                    neighbors_values.append(self._grid_ortools[r][c - 1])
                if c < self.columns_number - 1:
                    neighbors_values.append(self._grid_ortools[r][c + 1])

                same_value_neighbors = []
                for index, neighbor_value in enumerate(neighbors_values):
                    same_value = self._model.NewBoolVar(f"same_value_{index}_{neighbor_value}")
                    self._model.Add(self._grid_ortools[r][c] == neighbor_value).OnlyEnforceIf(same_value)
                    self._model.Add(self._grid_ortools[r][c] != neighbor_value).OnlyEnforceIf(same_value.Not())
                    same_value_neighbors.append(same_value)

                if self._grid[r][c] >= 1:
                    self._model.Add(sum(same_value_neighbors) == 1)
                else:
                    self._model.Add(sum(same_value_neighbors) == 2)


class Test(TestCase):
    def test_solution_basic_grid(self):
        grid = [
            [1, 2, _],
            [_, 3, 2],
            [1, _, 3]
        ]
        game_solver = NumberLinkSolverORTools(grid)
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
        game_solver = NumberLinkSolverORTools(grid)
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
