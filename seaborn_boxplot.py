import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
#print(tips['total_bill'][tips['total_bill']>40])
print("Original Tips Dataset :\n", tips.head(), "\n")
'''
sns.boxplot(x='total_bill', data=tips)
'''

'''
sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker',palette='husl')
'''

sns.boxplot(x='day',y='total_bill',data=tips,order=['Sun','Fri','Thur','Sat'], palette='husl')
sns.swarmplot(x='day',y='total_bill',data=tips,order=['Sun','Fri','Thur','Sat'],palette='husl',color='0.6')


iris = sns.load_dataset('iris')
print ('Original Iris Dataset :\n',iris.head(7),"\n")

'''
sns.boxplot(data=iris,palette='husl',orient='horizontal')
'''



plt.legend(loc ='upper left')
plt.show()