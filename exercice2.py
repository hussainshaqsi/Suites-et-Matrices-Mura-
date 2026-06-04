capital_initial = 300
versement_mensuel = 45
taux_annuel = 2.3 / 100
annees = 8

capital = capital_initial
for an in range(annees):
    capital = capital * (1 + taux_annuel) + versement_mensuel * 12
total_verse = capital_initial + versement_mensuel * 12 * annees
print("Question 1 (interets une fois par an)")
print(f"Capital au bout de {annees} ans : {capital:.2f} euros")
print(f"Interets obtenus : {capital - total_verse:.2f} euros")

capital = capital_initial
taux_mensuel = taux_annuel / 12
mois = annees * 12
for m in range(mois):
    capital = capital * (1 + taux_mensuel) + versement_mensuel
total_verse = capital_initial + versement_mensuel * mois
print("\nQuestion 2 (interets une fois par mois)")
print(f"Capital au bout de {annees} ans : {capital:.2f} euros")
print(f"Interets obtenus : {capital - total_verse:.2f} euros")