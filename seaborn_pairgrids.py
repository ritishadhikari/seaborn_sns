import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

iris = sns.load_dataset('iris')
print(iris.head())

#p= sns.PairGrid(data=iris,hue='species',palette='coolwarm',vars=['sepal_length','petal_width','sepal_width']).map(plt.scatter,edgecolor ='blue').add_legend()

#q = sns.PairGrid(data=iris,hue='species',palette='coolwarm',y_vars=['petal_length','petal_width'],x_vars=['sepal_length','sepal_width']).map(plt.scatter,edgecolor ='blue').add_legend()

#X =sns.PairGrid(data=iris,hue='species',palette='coolwarm',vars=['sepal_length','petal_width','sepal_width']).map_diag(plt.hist,histtype='step',edgecolor ='blue').add_legend()

#Y = sns.PairGrid(data=iris,hue='species',palette='coolwarm',vars=['sepal_length','petal_width','sepal_width']).map_offdiag(plt.scatter,edgecolor ='green').add_legend()

# plotting alltogather
t = sns.PairGrid(iris,hue='species',palette='RdBu',hue_kws=({'marker':['D','s','+']}))
t = t.map_diag(plt.hist)
t = t.map_upper(plt.scatter, s =30)
t = t.map_lower(sns.kdeplot)
t =t.add_legend()


#plt.legend(loc='best')
plt.show()
