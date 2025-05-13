import sys
import time
from ortools.sat.python import cp_model


class NQueenSolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, queens: list[list]):
        super().__init__()
        self._queens = queens
        self.__solution_count = 0
        self.__start_time = time.time()
        self._board_size = len(queens)

    @property
    def solution_count(self) -> int:
        return self.__solution_count

    def on_solution_callback(self):
        self.__solution_count += 1
        # self.print_board()
        # print()

    def print_board(self):
        for i in range(self._board_size):
            row_display = []
            for j in range(self._board_size):
                if self.value(self._queens[i][j]):
                    row_display.append("Q")
                else:
                    row_display.append("·")
            print(" ".join(row_display))


def main(board_size: int) -> None:
    model = cp_model.CpModel()

    # Create a matrix of boolean variables
    # queens[i][j] is True if there is a queen at row i, column j
    queens = []
    for i in range(board_size):
        row = []
        for j in range(board_size):
            row.append(model.new_bool_var(f"x_{i}_{j}"))
        queens.append(row)

    # Each row has exactly one queen
    for i in range(board_size):
        model.add(sum(queens[i][j] for j in range(board_size)) == 1)

    # Each column has exactly one queen
    for j in range(board_size):
        model.add(sum(queens[i][j] for i in range(board_size)) == 1)

    # No two queens can be on the same diagonal
    # Diagonal 1 (top-left to bottom-right)
    for d in range(-(board_size - 1), board_size):
        diagonal_vars = []
        for i in range(board_size):
            j = i - d
            if 0 <= j < board_size:
                diagonal_vars.append(queens[i][j])
        if len(diagonal_vars) > 1:
            model.add(sum(diagonal_vars) <= 1)

    # Diagonal 2 (top-right to bottom-left)
    for d in range(2 * board_size - 1):
        diagonal_vars = []
        for i in range(board_size):
            j = d - i
            if 0 <= j < board_size:
                diagonal_vars.append(queens[i][j])
        if len(diagonal_vars) > 1:
            model.add(sum(diagonal_vars) <= 1)

    solver = cp_model.CpSolver()
    solution_printer = NQueenSolutionPrinter(queens)
    solver.parameters.enumerate_all_solutions = True
    solver.solve(model, solution_printer)

    # Statistics.
    print("\nStatistics")
    print(f"  branches       : {solver.num_branches}")
    print(f"  wall time      : {solver.wall_time} s")
    print(f"  solutions found: {solution_printer.solution_count}")


if __name__ == "__main__":
    size = 10
    main(size)
