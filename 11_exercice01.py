def calculer(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b if b != 0 else "Division par zéro."
    else:
        return "Opérateur non valide."

x = float(input("Nombre 1 : "))
y = float(input("Nombre 2 : "))
operation = input("Opération (+, -, *, /) : ")
print(f"Résultat : {calculer(x, y, operation)}")