# Contexte :
# Vous avez trouvé un vieux cadenas à huit chiffres dans un tiroir.
# Heureusement, il y a un morceau de papier avec des indices énigmatiques écrits à côté :
# "La somme des deux premiers chiffres est égale à 1."
# "La somme des troisième et quatrième chiffres est égale à 6."
# "La somme des quatre derniers chiffres est égale à 9."
# "Le produit des premier, cinquième, septième et huitième chiffres est égal à 20."
# "Le quatrième chiffre divisé par le cinquième est égal à la somme du premier et du septième chiffre."

# Quelle est la combinaison du cadenas qui satisfait toutes ces règles ?

from QueensZ3 import *

chiffres = [Int(f'c{i}') for i in range(1, 9)]
c1, c2, c3, c4, c5, c6, c7, c8 = chiffres

solver = Solver()

solver.add([And(0 <= c, c <= 9) for c in chiffres])

solver.add(c1 + c2 == 1)
solver.add(c3 + c4 == 6)
solver.add(c5 + c6 + c7 + c8 == 9)
solver.add(c1 * c5 * c7 * c8 == 20)
solver.add(c4 / c5 == c1 + c7)

solutions = []
while solver.check() == sat:
    model = solver.model()
    solution = tuple(model.eval(c).as_long() for c in chiffres)
    solutions.append(solution)

    solver.add(Or([chiffres[i] != solution[i] for i in range(8)]))

print("Combinaisons possibles :")
print("\n".join(".".join(map(str, sol)) for sol in solutions))

