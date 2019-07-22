import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool



data = pd.read_csv('data/pokemon.csv')
print(data.info())
print(data.corr())
f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
plt.show()
print(data.head(10))
print(data.columns)

# Plotting all data
data1 = data.loc[:,["Attack","Defense","Speed"]]
data1.plot()
# it is confusing

# subplots
data1.plot(subplots = True)
plt.show()

# scatter plot
data1.plot(kind = "scatter",x="Attack",y = "Defense")
plt.show()

# hist plot
data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),normed = True)