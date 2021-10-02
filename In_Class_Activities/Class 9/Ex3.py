#Ejercicio 3: Defina una función llamada cuenta_vocales, que dada una cadena de texto, regrese la cantidad de vocales que tiene la cadena.
def cuenta_vocales(frase):
    count = 0

    for i in frase:
        if i in "aeiou":
            count +=1

    return (count)