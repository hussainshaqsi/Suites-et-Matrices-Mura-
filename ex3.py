import math
print("Calcul du diametre et de la longueur enroulee d'un volet roulant.")
d_axe = float(input("Entrer le diametre de l'axe en mm: "))
n = int(input("Entrer nombre de tours n: "))
print("\nCalcul de la longueur L pour chaque tour:")
L = 0
for tour in range(1, n + 1):
    d = d_axe + 18 * tour
    L = L + round(math.pi * d)
    print(f"Tour: {tour}  - Diametre [mm]: {d}  - Longueur enroulee [mm]: {L}")
print("\nCalcul de la longueur L par formule:")
L_formule = math.pi * sum(d_axe + 18 * i for i in range(n))
print(f"Longueur [mm] pour {n} tours: {L_formule}")