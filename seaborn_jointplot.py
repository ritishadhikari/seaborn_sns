import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

tips = sns.load_dataset('tips')
print("The Tips Dataset looks like :\n", tips.head(), "\n")

iris = sns.load_dataset('iris')
print("The Iris Dataset Looks like :\n", iris.head(), "\n")

sns.jointplot(data=tips, x='total_bill', y='tip',kind='kde',color='green')

sns.jointplot(data=tips, x='total_bill', y='tip',stat_func=spearmanr,kind='reg', color='red',height=9,ratio=2)

plt.show()