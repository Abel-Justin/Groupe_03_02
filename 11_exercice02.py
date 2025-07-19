def stats(liste):
    somme = sum(liste)
    moyenne = somme / len(liste)
    maximum = max(liste)
    return somme, moyenne, maximum

nombres = [float(x) for x in input("Entrez des nombres : ").split()]
s, m, mx = stats(nombres)
print(f"Somme : {s}\nMoyenne : {m:.2f}\nMaximum : {mx}")