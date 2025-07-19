fièvre = input("Avez-vous de la fièvre ? (oui/non):").lower()
if fièvre == "oui":
    douleurs = input("Avez-vous des douleurs ? (oui/non):").lower()
    if douleurs == "oui":
        print("Consulter un médecin.")
    else:
        toux = input("Avez-vous une toux ? (oui/non) :").lower()
        if toux == "oui":
            print("Repos conseillé.")
        else:
            print("Bonne santé")