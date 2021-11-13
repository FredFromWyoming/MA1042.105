import pandas as pd
import numpy as np

table = pd.read_csv("CF.csv", index_col = 0)

#Ex4
table5 = table.drop('E05',0)
table5 = table5.drop('Yo, Robot',1)

print(table5)