import pandas as pd
import numpy as np

table = pd.read_csv("CF.csv", index_col = 0)

#print(table)

p1 = pd.DataFrame(table[['Exmachina']])
p2 = pd.DataFrame(table[['Yo, Robot']])
p3 = pd.DataFrame(table[['AI']])
p4 = pd.DataFrame(table[['2001']])
p5 = pd.DataFrame(table[['Matrix']])
p6 = pd.DataFrame(table[['Blade Runner']])

#Ex2
averages = []

averages.append(np.mean(p1))
averages.append(np.mean(p2))
averages.append(np.mean(p3))
averages.append(np.mean(p4))
averages.append(np.mean(p5))
averages.append(np.mean(p6))

print(averages)