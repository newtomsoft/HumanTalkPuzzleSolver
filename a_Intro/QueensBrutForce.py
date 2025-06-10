from itertools import permutations

def brut_force_queens(n=4):
    for perm in permutations(range(n)):
        if is_valid_solution(perm):
            for row, col in enumerate(perm):
                print(f"R{row} C{col}")
            return
    print("Aucune solution trouvée.")

def is_valid_solution(solution):
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            if abs(solution[i] - solution[j]) == abs(i - j):
                return False
    return True

brut_force_queens(4)