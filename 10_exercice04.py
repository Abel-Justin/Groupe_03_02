numero = input("Entrez un numéro : ")
if len(numero) > 3:
    masque = "*" * (len(numero) - 3) + numero[-3:]
    print(f"Numéro masqué : {masque}")
else:
    print("Numéro trop court pour masquer.")