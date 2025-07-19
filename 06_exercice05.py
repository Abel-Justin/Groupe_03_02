n = int(input("Entrez un entier positif : "))

while n < 0:
    print("Veuillez entrer un nombre positif.")
    n = int(input("Entrez un entier positif : "))

fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print(f"Factorielle de {n} = {fact}")