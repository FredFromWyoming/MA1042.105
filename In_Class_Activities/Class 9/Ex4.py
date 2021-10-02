#Ejercicio 4: Defina una función llamada media, que dada una lista de números regrese su media (promedio).
def media(lista):
    sum = 0 
    count = 0

    for i in lista:
        sum += i
        count += 1

    return (sum/count)