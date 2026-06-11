print("Calcul d'un pret immobilier ou d'un credit a la consommation.")
C = float(input("Entrer le montant du pret ou credit: "))
t = float(input("Entrer le taux annuel en %: "))
n = int(input("Entrer le nombre d'annees: "))
taux_mensuel = t / 100 / 12
N = n * 12
M = (C * taux_mensuel * (1 + taux_mensuel)**N) / ((1 + taux_mensuel)**N - 1)
interets_total = M * N - C
print(f"La mensualite avec interets est de {M:.2f} euros")
print(f"Le montant des interets rembourses sont de {interets_total:.2f} euros.")
print(f"Le taux mensuel est de {taux_mensuel}")
print("\nTableau d'amortissement:")
print("Mois - Mensualite - Interets - Capital rembourse - Capital restant du - Interets rembourses")
capital_restant = C
interets_cumules = 0
for mois in range(1, N + 1):
    interets = capital_restant * taux_mensuel
    capital_rembourse = M - interets
    capital_restant = capital_restant - capital_rembourse
    interets_cumules = interets_cumules + interets
    print(f"{mois} - {M:.1f} - {interets:.1f} - {capital_rembourse:.1f} - {capital_restant:.1f} - {interets_cumules:.2f}")