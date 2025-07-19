entree = input("Entrez des nombres : ")
liste = [float(x) for x in entree.split()]

maximum = max(liste)
minimum = min(liste)
moyenne = sum(liste) / len(liste)

print(f"Max : {maximum}")
print(f"Min : {minimum}")
print(f"Moyenne : {moyenne:.2f}")