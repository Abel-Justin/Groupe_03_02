import math
try:
    x = float(input("Nombre : "))
    print(f"Racine : {math.sqrt(x)}")
except ValueError:
    print("Erreur : Nombre invalide.")
finally:
    print("Fin du calcul.")