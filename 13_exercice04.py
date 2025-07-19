while True:
    try:
        n = int(input("Entier positif : "))
        if n >= 0:
            break
    except ValueError:
        print("Erreur : Entrez un entier valide.")