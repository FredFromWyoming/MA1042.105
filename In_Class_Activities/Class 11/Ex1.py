def doble (list):
    """Esta función duplica cada elemento de una lista dada"""

    out = []

    for i in list:
        i += i
        out += [i]
    return out

print(doble([5,6,7]))