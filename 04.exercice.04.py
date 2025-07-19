anciennete = int(input("Années d'ancienneté :"))
note = int(input("Note de performance (1-5) :"))
if anciennete >= 5:
    if note >= 4:
        prime = 2000
    else:
        prime = 1000
else:
    if note >= 4:
        prime = 500
    else:
        prime = 0
print(f"Prime attribuée : {prime}€.")

