from z3 import Int, Solver, sat

# Créer les variables
x = Int('x')
y = Int('y')

# Créer le solveur
solver = Solver()

# Ajouter des contraintes
solver.add(x ** 2 + y ** 3 > 10000000)
solver.add(x ** 2 - 3 * y ** 3 == 0)
solver.add(x > 1)
solver.add(y > 1)

# Vérifier si les contraintes sont satisfiables
if solver.check() == sat:
    # Obtenir un modèle satisfaisant les contraintes
    model = solver.model()
    print(f"Solution trouvée: x = {model[x]}, y = {model[y]}")
else:
    print("Aucune solution trouvée.")
