def convertir(usd):
    return usd * 0.93, usd * 610, usd * 0.79

montant = float(input("Montant en USD : "))
eur, cfa, gbp = convertir(montant)
print(f"{montant} USD = {eur:.2f} EUR, {cfa:.2f} CFA, {gbp:.2f} GBP")