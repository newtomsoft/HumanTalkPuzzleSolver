# Contexte :
# Vous avez trouvé un vieux cadenas à huit chiffres dans un tiroir.
# Heureusement, il y a un morceau de papier avec des indices énigmatiques écrits à côté :
# "La somme des deux premiers chiffres est égale à 1."
# "La somme des troisième et quatrième chiffres est égale à 6."
# "La somme des quatre derniers chiffres est égale à 9."
# "Le produit premier, cinquième, septième et huitième chiffres est égal à 20."
# "Le quatrième chiffre divisé par le cinquième est égal à la somme du premier et du septième chiffre."
import time


# Quelle est la combinaison du cadenas qui satisfait toutes ces règles ?

def verifier_combinaison(code):
    # Transformation de la liste en chiffres individuels
    c1, c2, c3, c4, c5, c6, c7, c8 = code

    # Vérification de toutes les contraintes
    if c1 + c2 != 1:
        return False

    if c3 + c4 != 6:
        return False

    if c5 + c6 + c7 + c8 != 9:
        return False

    if c1 * c5 * c7 * c8 != 20:
        return False

    if c5 == 0:
        return False

    if c4 / c5 != c1 + c7:
        return False

    return True


def trouver_combinaison():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                for c4 in range(10):
                    for c5 in range(10):
                        for c6 in range(10):
                            for c7 in range(10):
                                for c8 in range(10):
                                    code = (c1, c2, c3, c4, c5, c6, c7, c8)
                                    if verifier_combinaison(code):
                                        return code
    return None

begin_time = time.time()
solution = trouver_combinaison()
end_time = time.time()
print(f"Temps de recherche : {end_time - begin_time:.2f} secondes")

print(f"Combinaison possible :")
if solution is None:
    print("Aucune combinaison trouvée.")
    exit(-1)
print("".join(map(str, solution)))


