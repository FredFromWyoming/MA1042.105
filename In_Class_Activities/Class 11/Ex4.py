def suma (listA, listB):
    """Esta función suma elemento a elemento dos listas numéricas del mismo tamaño"""

    out = []

    if (len(listA) == len(listB)):
        for i in range(len(listA)):
            out += [ listA[i] + listB[i] ]
        return (out)

    else:

        return("Error: lists must be the same length")

print(suma([1,2,3],[10,20]))
print(suma([1,2,3], [10,20,30]))