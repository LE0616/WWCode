import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random


data = pd.read_csv("iris.csv")

data.head()
# or
print(data)
# or
print(data[9:30])

petal_data = data[['petal_length', 'petal_width','species']]
print(petal_data)


length = petal_data[['petal_length']
width = petal_data[['petal_width']]
species = petal_data[['species']]
print(length)
print(width)
print(species)




fig, ax = plt.subplots()
df = pd.DataFrame({'petal_length': length, 'petal_width': width }, index= species)
print(df)

ax = df.plot.bar(rot=0)


