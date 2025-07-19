activite = input("Décrivez votre activité du jour : ")

with open("journal.txt", "a", encoding="utf-8") as f:
    f.write(activite + "\n")

print("Activité ajoutée dans 'journal.txt'.")