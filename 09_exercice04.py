phrase = input("Entrez une phrase ou un titre : ")
mots = phrase.split()
acronyme = ""
for mot in mots:
    acronyme += mot[0].upper()
print(f"Acronyme : {acronyme}")