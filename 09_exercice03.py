texte = input("Entrez un texte : ")
mot = input("Mot à chercher : ")
compte = texte.count(mot)
print(f"Le mot '{mot}' apparaît {compte} fois.")