def mediana2(list):
    """Esta función la media de una lista"""

    if (len(list)%2==0): #even
        return [sorted(list)[int(len(list)/2)],sorted(list)[int((len(list)/2)+1)]]

    else: #odd
        return sorted(list) [int((len(list)-1)/2)]

print(mediana2([1,0,2,5,3,1,6,7,8,0,9,8,7]))

print(mediana2([1,1,1,2,2,3,3,3,4,5,10,11,5,5,20, 7]))