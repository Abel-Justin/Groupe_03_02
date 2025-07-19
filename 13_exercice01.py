try:
    a, b = float(input("Nombre 1 : ")), float(input("Nombre 2 : "))
    print(f"Résultat : {a / b}")
except ZeroDivisionError:
    print("Division par zéro !")