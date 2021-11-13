import math

#Ex 7

#Distance function
def dist (point_1,point_2):
    x = (point_1 [0] - point_2 [0])**2
    y = (point_1 [1] - point_2 [1])**2
    z = (point_1 [2] - point_2 [2])**2
    return (math.sqrt((x+y+z)))

#Function required for Sort method
def ret4(point):
    return point [4]

#Function to find the mode in a list
def mode (list):
    counts = []
    out = {}
    for i in list:
        counts.append(list.count(i))
        out [list.count(i)] = {i}

    return out[max(counts)]

#kNN algorithm 
def kNN(k,pointList,point):

    for i in pointList:
        i [4] = dist(point,i)

    pointList.sort(reverse=False, key = ret4)

    colors = []

    for i in range(k):
        colors.append(pointList[i] [3])

    out = mode(colors)

    return out


#Running Tests
import random as rd
import statistics

rd.seed(777)
puntos = []
for i in range(50):
    puntos.append([rd.randint(1,100), rd.randint(1,100), rd.randint(1,100), rd.choice(['yellow','blue', 'red']),0])

print("Test 1")
#print(puntos)
print(kNN(5,puntos, [20,30,40]))
print(kNN(5, puntos, [20,30,47]))
print(kNN(5, puntos, [11,53,89]))
print(kNN(8, puntos, [97, 11, 54]))
#Respuestas primer prueba:
#red
#blue
#yellow
#blue


print("Test 2")
rd.seed(777)
puntos2 = []
for i in range(500):
    puntos2.append([rd.randint(1,100), rd.randint(1,100), rd.randint(1,100), rd.choice(['yellow','blue', 'red']),0])

print(kNN(10, puntos2, [11,80,77]))
print(kNN(13, puntos2, [23, 53, 31]))
#Respuestas: blue, red