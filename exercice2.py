print("Calcul du capital acquis et de ses interets.")
capital_initial = float(input("Entrer le placement de depart: "))
versement = float(input("Entrer le montant du versement mensuel: "))
t = float(input("Entrer le taux annuel en %: "))
annees = int(input("Entrer le nombre d'annees: "))
taux_annuel = t / 100

capital = capital_initial
for an in range(annees):
    capital = (capital + versement * 12) * (1 + taux_annuel)
total = capital_initial + versement * 12 * annees
print(f"\nQuestion 1 (interets une fois par an)")
print(f"Le capital acquis avec interets est de {capital:.2f} euros au bout de {annees} ans.")
print(f"Les interets gagnes au taux de {t} % sont de {capital - total:.2f} euros.")
print(f"Sans placement le capital serait de {total:.0f} euros.")

capital = capital_initial
taux_mensuel = taux_annuel / 12
mois = annees * 12
for m in range(mois):
    capital = (capital + versement) * (1 + taux_mensuel)
total = capital_initial + versement * mois
print(f"\nQuestion 2 (interets une fois par mois)")
print(f"Le capital acquis avec interets est de {capital:.2f} euros au bout de {annees} ans.")
print(f"Les interets gagnes au taux de {t} % sont de {capital - total:.2f} euros.")
print(f"Sans placement le capital serait de {total:.0f} euros.")