import random
import string

def generer_mdp(longueur):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longueur))

print(f"Mot de passe généré : {generer_mdp(int(input('Longueur : ')))}")