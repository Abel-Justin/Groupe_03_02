try:
    with open(input("Nom du fichier : "), "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Fichier introuvable.")