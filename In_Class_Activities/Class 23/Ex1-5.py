from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import math

#Distance function
def dist (point_1,point_2,row):
    x = (point_1 [0] - point_2.iloc[row,0])**2
    y = (point_1 [1] - point_2.iloc[row,1])**2
    x2 = (point_1 [2] - point_2.iloc[row,2])**2
    y2 = (point_1 [3] - point_2.iloc[row,3])**2
    return (math.sqrt(x+y) + math.sqrt(x2+y2))

#Function required for Sort method
def ret1(list):
    return list [1]

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

    labelDist = []

    for i in range (pointList.shape [0]):
        labelDist.append([pointList.iloc[i,4],dist(point,pointList,i)])

    labelDist.sort(reverse=False, key = ret1)
    print(labelDist)
    colors = []

    for i in range(k):
        colors.append(labelDist [i] [0])

    out = mode(colors)
    return out


iris = datasets.load_iris()
y = pd.DataFrame(iris['target'])

#Ex1
x = pd.DataFrame(iris['data'])

print(x.shape)
print(y.shape)

#y = y.reshape(-1,1)

#Ex2

#Ex3
blank = y

base_np = pd.concat([x, y, blank], axis=1, join='inner')

#Ex4
#print(kNN(3, base_df, [5.6, 2.8, 3.9, 1.1]))

#Ex5
print(kNN(3, base_np, [5.6, 2.8, 3.9, 1.1]))
print(kNN(5, base_np, [5.7, 2.6, 3.8, 1.3]))
print(kNN(8, base_np, [4.7, 3.2, 1.3, 0.2]))