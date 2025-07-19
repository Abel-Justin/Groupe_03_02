def est_palindrome(mot):
    return mot == mot[::-1]

mot = input("Entrez un mot : ")
print("C'est un palindrome." if est_palindrome(mot) else "Ce n'est pas un palindrome.")