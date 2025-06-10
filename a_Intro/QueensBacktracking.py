import time


def solve_queens_backtracking(n=4):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
               abs(board[i] - col) == abs(i - row):
                return False
        return True

    def backtrack(row, board):
        if row == n:
            return board.copy()

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solution = backtrack(row + 1, board)
                if solution is not None:
                    return solution
                board[row] = -1
        return None

    board = [-1] * n
    solution = backtrack(0, board)
    for row, col in enumerate(solution):
        print(f" R{row} C{col}")

start_time = time.time()
solve_queens_backtracking(20)
end_time = time.time()
print(f"Temps d'exécution : {end_time - start_time:.3f} secondes")
