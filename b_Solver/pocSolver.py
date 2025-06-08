import math

from z3 import Solver, sat, Ints
from ortools.linear_solver import pywraplp

# ---- Z3 Solver ----
# Créer des variables entières
x, y = Ints('x, y')


# Créer un solveur
solver = Solver()

# Ajouter des contraintes au solveur
solver.add(x + y == 10)
solver.add(x - y == 4)

# Vérifier si le système a une solution
if solver.check() == sat:
    # Obtenir le modèle qui satisfait les contraintes
    model = solver.model()
    print(f"Solution avec z3: x = {model[x]}, y = {model[y]}")
else:
    print("Pas de solution trouvée avec z3.")


# ---- Or-Tools ----
# Créer un solveur utilisant GLOP (solveur linéaire de Google)
solver = pywraplp.Solver.CreateSolver("GLOP")

# Créer des variables de décision
x = solver.IntVar(-solver.infinity(), solver.infinity(), "x")
y = solver.IntVar(-solver.infinity(), solver.infinity(), "y")

# Ajouter des contraintes au solveur
solver.Add(x + y == 10)
solver.Add(x - y == 4)

# Résoudre le problème
status = solver.Solve()

# Vérifier si le système a une solution
if status == pywraplp.Solver.OPTIMAL:
    print(f"Solution avec Or-Tools: x = {int(x.solution_value())}, y = {int(y.solution_value())}")
else:
    print("Pas de solution trouvée avec Or-Tools.")
