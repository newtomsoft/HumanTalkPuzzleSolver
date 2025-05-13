from unittest import TestCase

from ortools.sat.python import cp_model


class MinesweeperSolverORTools:
    def __init__(self, grid: list[list]):
        self._grid_ortools = None
        self._grid = grid
        self.rows_number = len(grid)
        self.columns_number = len(grid[0])
        self._model = cp_model.CpModel()
        self._solver = cp_model.CpSolver()

    def get_solution(self):
        self._grid_ortools = [[self._model.NewBoolVar(f"cell_{r}_{c}") for c in range(self.columns_number)] for r in range(self.rows_number)]
        self._add_sum_constraints()

        status = self._solver.Solve(self._model)
        if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
            return [[self._solver.Value(self._grid_ortools[r][c]) for c in range(self.columns_number)] for r in range(self.rows_number)]
        else:
            return [[]]

    def _add_sum_constraints(self):
        for r in range(self.rows_number):
            for c in range(self.columns_number):
                if self._grid[r][c] == -1:
                    continue
                self._model.Add(self._grid_ortools[r][c] == 0)
                neighbors_values = self._get_neighbors_values(self._grid_ortools, r, c)
                self._model.Add(sum(neighbors_values) == self._grid[r][c])

    def _get_neighbors_values(self, grid, r, c):
        neighbors_values = []
        if r > 0:
            neighbors_values.append(grid[r - 1][c])
            if c > 0:
                neighbors_values.append(grid[r - 1][c - 1])
            if c < self.columns_number - 1:
                neighbors_values.append(grid[r - 1][c + 1])
        if r < self.rows_number - 1:
            neighbors_values.append(grid[r + 1][c])
            if c > 0:
                neighbors_values.append(grid[r + 1][c - 1])
            if c < self.columns_number - 1:
                neighbors_values.append(grid[r + 1][c + 1])
        if c > 0:
            neighbors_values.append(grid[r][c - 1])
        if c < self.columns_number - 1:
            neighbors_values.append(grid[r][c + 1])
        return neighbors_values


_ = -1


class MinesweeperSolverTests(TestCase):
    def test_solution_basic_grid(self):
        grid = [
            [_, _, _],
            [_, 1, 1],
            [_, 1, _]
        ]
        game_solver = MinesweeperSolverORTools(grid)
        solution = game_solver.get_solution()
        expected_solution = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 1]
        ]
        self.assertEqual(expected_solution, solution)

    def test_solution_10x10(self):
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
        game_solver = MinesweeperSolverORTools(grid)
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