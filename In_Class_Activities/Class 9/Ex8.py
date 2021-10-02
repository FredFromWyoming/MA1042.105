#Ejercicio 8: Usando la función es_primo, defina una función llamada primos, que dado un entero positivo n regrese la lista de primos menores o iguales a n.

def factores (n):
    list = []

    for i in range (1,n+1):
        if (n%i == 0):
            list += [i]

    return(list)

def es_primo (n):
    if (len(factores(n))==2):
        return True
    else:
        return False


def primos(n):
    list = []

    for i in range(n):
        if es_primo(i):
            list += [i]

    return list