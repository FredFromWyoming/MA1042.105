import pandas as pd
import numpy as np

table = pd.read_csv("CF.csv", index_col = 0)

#Ex3
table4 = table.loc['E01':'E11']

print(table4)