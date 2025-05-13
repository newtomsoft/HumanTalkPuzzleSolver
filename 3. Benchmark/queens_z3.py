import time
from z3 import *


class NQueenSolutionPrinter:
    def __init__(self, queens, solver, board_size):
        self._queens = queens
        self._solver = solver
        self._board_size = board_size
        self.__solution_count = 0
        self.__start_time = time.time()

    @property
    def solution_count(self) -> int:
        return self.__solution_count

    def print_solution(self, model):
        self.__solution_count += 1
        # self.print_board(model)
        # print()

    def print_board(self, model):
        for i in range(self._board_size):
            row_display = []
            for j in range(self._board_size):
                if model.evaluate(self._queens[i][j]):
                    row_display.append("Q")
                else:
                    row_display.append("·")
            print(" ".join(row_display))


def main(board_size: int) -> None:
    # Start timer
    start_time = time.time()
    
    # Create a Z3 solver
    solver = Solver()

    # Create a matrix of boolean variables
    # queens[i][j] is True if there is a queen at row i, column j
    queens = []
    for i in range(board_size):
        row = []
        for j in range(board_size):
            row.append(Bool(f"x_{i}_{j}"))
        queens.append(row)

    # Each row has exactly one queen
    for i in range(board_size):
        solver.add(PbEq([(queens[i][j], 1) for j in range(board_size)], 1))

    # Each column has exactly one queen
    for j in range(board_size):
        solver.add(PbEq([(queens[i][j], 1) for i in range(board_size)], 1))

    # No two queens can be on the same diagonal
    # Diagonal 1 (top-left to bottom-right)
    for d in range(-(board_size - 1), board_size):
        diagonal_vars = []
        for i in range(board_size):
            j = i - d
            if 0 <= j < board_size:
                diagonal_vars.append(queens[i][j])
        if len(diagonal_vars) > 1:
            solver.add(PbLe([(var, 1) for var in diagonal_vars], 1))

    # Diagonal 2 (top-right to bottom-left)
    for d in range(2 * board_size - 1):
        diagonal_vars = []
        for i in range(board_size):
            j = d - i
            if 0 <= j < board_size:
                diagonal_vars.append(queens[i][j])
        if len(diagonal_vars) > 1:
            solver.add(PbLe([(var, 1) for var in diagonal_vars], 1))

    # Create solution printer
    solution_printer = NQueenSolutionPrinter(queens, solver, board_size)

    # Find all solutions
    solution_count = 0
    while solver.check() == sat:
        model = solver.model()
        solution_printer.print_solution(model)
        solution_count += 1

        # Add a constraint to exclude the current solution
        block = []
        for i in range(board_size):
            for j in range(board_size):
                if model.evaluate(queens[i][j]):
                    block.append(Not(queens[i][j]))
        solver.add(Or(block))

    # Statistics
    end_time = time.time()
    print("\nStatistics")
    print(f"  wall time      : {end_time - start_time} s")
    print(f"  solutions found: {solution_count}")


if __name__ == "__main__":
    size = 11
    main(size)
