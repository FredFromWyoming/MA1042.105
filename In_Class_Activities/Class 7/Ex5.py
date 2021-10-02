frase = input("Dame una frase y te diré la cantidad de letras que tiene: ")
suma = 0
for char in frase:
    if ("a" in char):
        suma += 1
    elif ("e" in char):
        suma += 1
    elif ("i" in char):
        suma += 1
    elif ("o" in char):
        suma += 1
    elif ("u" in char):
        suma += 1
    
print(suma)

