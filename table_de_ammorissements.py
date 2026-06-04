print("Calcul d'un pret immobilier ou d'un credit a la consommation.")

C = float(input("Entrer le montant du pret ou credit : "))
t = float(input("Entrer le taux annuel en % : "))
taux_annuel = t / 100 / 12
taux_mensuel = taux_annuel / 100 * 12
n = int(input("Entrer le nombre d'années :"))
monthly_payments = n * 12


def mensualite(monthly_payments,C,taux_annuel):
    return (C * taux_annuel*(1+taux_annuel)**monthly_payments) / ((1+taux_annuel)**monthly_payments -1)

def rembourses(mensualite,monthly_payments,C):
    return mensualite * monthly_payments - C

M=mensualite(monthly_payments,C,taux_annuel)
print(f"La mensualite avec interets est de {M}")
print(f"Le montant des interets rembourses sont de {rembourses(M, monthly_payments, C)}")
print(f"Le taux mensuel est de {taux_mensuel}")