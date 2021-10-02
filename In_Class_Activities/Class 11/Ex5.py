def mediana1(list):
    """Esta función la media de una lista impar"""

    return (sorted(list) [int((len(list)-1)/2)] )

print(mediana1([1,0,2,5,3,1,6,7,8,0,9,8,7]))