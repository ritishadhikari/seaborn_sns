import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

normal = np.random.rand(12,15)
print("The Actual Random Data is :\n", normal, "\n")
#sns.heatmap(normal,annot=True, vmax=1, vmin=0)


flights = sns.load_dataset('flights')
print("The flight dataset looks like :\n", flights.head(), "\n")
flights =flights.pivot_table(index='month',columns='year',values='passengers')
print("Pivot :\n",flights,"\n")
sns.heatmap(data=flights,annot=True,fmt='d',linewidths=1.2, vmin=100, vmax=650,cmap='cividis',center=flights.loc['June',1954],cbar=True)

plt.show()