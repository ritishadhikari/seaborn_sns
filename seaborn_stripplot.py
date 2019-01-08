import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips =sns.load_dataset('tips')
print("Original Tips Dataset :\n", tips.head(), "\n")

#sns.stripplot(x='day',y='total_bill',data=tips,palette='husl',jitter=0.13,hue='sex',linewidth=1,dodge=True, order=['Sun','Thur','Fri','Sat'],hue_order=['Female','Male'],marker ='D',size=5,
 #            edgecolor='black', alpha= 0.78)
#sns.boxplot(x='day',y='total_bill',data=tips,palette='husl',hue='sex',order=['Sun','Thur','Fri','Sat'],hue_order=['Female','Male'])
sns.swarmplot(x='day',y='total_bill',data=tips,palette='husl',hue='sex',order=['Sun','Thur','Fri','Sat'],hue_order=['Female','Male'],dodge=True, marker ='D',edgecolor='black', alpha= 0.78, size=5,
             linewidth=1)

sns.violinplot(x='day',y='total_bill',data=tips,palette='husl',hue='sex',linewidth=1,dodge=True, order=['Sun','Thur','Fri','Sat'],hue_order=['Female','Male'],split=False,inner='quartile',
               scale='count',scale_hue=False,bw=0.5)

plt.legend(loc ='best')

plt.show()
