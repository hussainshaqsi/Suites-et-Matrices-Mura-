print("Calcul d'un pret immobilier ou d'un credit a la consommation.")

C = float(input("Entrer le montant du pret ou credit : "))
t = float(input("Entrer le taux annuel en % : "))
taux_mensuel = t / 100 / 12
n = int(input("Entrer le nombre d'années :"))
monthly_payments = n * 12


def mensualite(monthly_payments, C, taux_mensuel):
    return (C * taux_mensuel * (1 + taux_mensuel)**monthly_payments) / ((1 + taux_mensuel)**monthly_payments - 1)

def rembourses(mensualite, monthly_payments, C):
    return mensualite * monthly_payments - C

M = mensualite(monthly_payments, C, taux_mensuel)
print(f"La mensualite avec interets est de {M}")
print(f"Le montant des interets rembourses sont de {rembourses(M, monthly_payments, C)}")
print(f"Le taux mensuel est de {taux_mensuel}")
print("\nTableau d'amortissement:")
print("Mois - Interets - Capital amorti - Capital restant du")
capital_restant = C
for mois in range(1, monthly_payments + 1):
    interets = capital_restant * taux_mensuel
    capital_amorti = M - interets
    capital_restant = capital_restant - capital_amorti
    print(f"Mois {mois}: interets {interets:.2f} | capital amorti {capital_amorti:.2f} | restant du {capital_restant:.2f}")