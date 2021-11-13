import math

#Ex 1
def dist (point_1,point_2):
    x = (point_1 [0] - point_2 [0])**2
    y = (point_1 [1] - point_2 [1])**2
    z = (point_1 [2] - point_2 [2])**2
    return (math.sqrt((x+y+z)))

#Ex 2
def Coords(point):
    return [point [0],point[1],point [2]]

#Ex 3
def index(list):
    out = []
    for i in range(len(list)):
        out.append([list[i], i])
    return out

#Ex 4
def getNearColors(pointList,indexList):
    out = []
    for i in range(len(indexList)):
        out.append(pointList [indexList[i]] [3])
    return out

thing_1 = [10,9,8,7,6,5,4,3,2,1]

#Ex 5
def Kmin(k,list):
    out = []
    list.sort()

    for i in range(k):
        out.append(list[i])
    return out

print(Kmin(3,thing_1))

