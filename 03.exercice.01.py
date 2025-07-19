age = int(input("Entrez votre âge :"))
pays= str(input("Entrez votre pays:").lower())

if age >= 18 and (pays == "congo" or pays =="cameroun"):
    print("Inscription autorisée.")
elif age < 18:
    print("Vous êtes trop jeune pour vous inscrite.")
else:
    print("Désolé, programme réservé aux ressortissants du congo ou Cameroun.")