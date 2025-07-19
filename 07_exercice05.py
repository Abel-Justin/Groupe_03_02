entree = input("Entrez des éléments : ")
liste = entree.split()

liste_inverse = []
for i in range(len(liste) - 1, -1, -1):
    liste_inverse.append(liste[i])

print(f"Liste inversée : {liste_inverse}")