choix = ""
while choix != "0":
    print("\n== MENU ==")
    print("1. Dire Bonjour")
    print("2. Additionner deux nombres")
    print("0. Quitter")

    choix = input("Choisissez une option : ")
    if choix == "1":
        print("Bonjour ! 😊")
    elif choix == "2":
        a = float(input("Nombre 1 : "))
        b = float(input("Nombre 2 : "))
        print(f"Résultat : {a + b}")
    elif choix == "0":
        print("Au revoir !")
    else:
        print("Choix invalide.")