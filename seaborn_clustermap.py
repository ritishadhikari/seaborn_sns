import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

flights = sns.load_dataset('flights')
print("The flight dataset looks like :\n", flights.head(), "\n")
flights =flights.pivot(index='month',columns='year',values='passengers')
print("Pivot :\n",flights,"\n")


#sns.clustermap(data=flights)

#sns.clustermap(data=flights,standard_scale=1)  #standardize 0-row, 1-column

#sns.clustermap(data=flights,z_score=0)   #normalize 0-row, 1-column

#sns.clustermap(data=flights,col_cluster=False) #cluster by rows

#sns.clustermap(flights,row_cluster=False) #cluster by column

sns.clustermap(data=flights,cmap='cool', linewidths =1.2,figsize=(12,8))


plt.show()
