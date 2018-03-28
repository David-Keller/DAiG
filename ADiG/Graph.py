import csv
from igraph import *
import pandas as pd

df = pd.read_csv('/Users/davidjia/Desktop/SpeedDatingData.csv', encoding = "ISO-8859-1")
x = df['iid']
# print(x)
print(x[9])
print(x[10])
print("--------------------")
print(x.unique())
