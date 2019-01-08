import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


tips = sns.load_dataset('tips')
print("The Original Dataframe :\n",tips.head(), "\n")

#sns.barplot(x='day', y ='tip', data=tips)
sns.barplot(x='day', y='tip', hue='sex',data=tips, palette ='RdBu',order=['Sat','Fri','Sun','Thur'],estimator=np.mean)
plt.show()