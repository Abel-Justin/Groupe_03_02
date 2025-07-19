nombre = int(input("Nombre pour la table de multiplication : "))

with open("table.txt", "w", encoding="utf-8") as f:
    for i in range(1, 13):
        ligne = f"{nombre} x {i} = {nombre * i}\n"
        f.write(ligne)

print("Table générée dans 'table.txt'.")