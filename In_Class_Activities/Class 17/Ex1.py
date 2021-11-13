import pandas as pd
import numpy as np

table = pd.read_csv("CF.csv", index_col = 0)

#print(table)

#Ex1

p1 = pd.DataFrame(table['Exmachina'])
p2 = pd.DataFrame(table['Yo, Robot'])
p3 = pd.DataFrame(table['AI'])
p4 = pd.DataFrame(table['2001'])
p5 = pd.DataFrame(table['Matrix'])
p6 = pd.DataFrame(table['Blade Runner'])

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)

#Ex2
averages = []

averages.append(np.mean(p1))

print(averages)