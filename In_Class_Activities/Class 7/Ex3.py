frase = input("Dame una frase y te diré la cantidad de letras que tiene: ")
suma = 0
for char in frase:
    if (" " in char):
        continue
    else:
        suma = suma + 1
  
print(suma)