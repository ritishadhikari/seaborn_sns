import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print("The Dataset Looks Like :\n", tips.head(10), "\n")
#print("Filtering \n",tips[(tips['day']=='Sat') & (tips['time']=='Lunch')],"\n")

#sns.FacetGrid(data=tips,row='smoker',col='time').map(plt.hist, 'total_bill',color='red') #histogram
#sns.FacetGrid(data=tips,row='smoker', col='time').map(plt.scatter, 'total_bill','tip', color='brown') #scatterplot
#sns.FacetGrid(data=tips,row='smoker',col='time').map(sns.regplot,'total_bill','tip', color='green') #regplot
sns.FacetGrid(data=tips,hue='smoker', col='time').map(sns.regplot, 'total_bill','tip').add_legend() #scatterplot

sns.FacetGrid(data=tips,col='day',col_order=['Sat','Thur','Sun','Fri'], height=7, aspect=0.2,palette='tab20c_r').map(sns.boxplot,'time', 'total_bill',color='violet')
plt.show()