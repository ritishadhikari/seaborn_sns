#KDE - Kernel Density Estimator

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

mean =[0,0]
cov= [[0.2,0],[0,3]]

x_axis, y_axis =np.random.multivariate_normal(mean=mean,cov=cov,size=40).T
print(x_axis,"\n")

print(x_axis,"\n")

#sns.kdeplot(data=x_axis, shade=False,data2=y_axis,cmap ='gnuplot2_r',n_levels = 24, bw=1, vertical=True)

iris = sns.load_dataset('iris')
print("The Iris Dataset Looks like :\n", iris.head(),"\n")

setosa = iris[iris['species'] == 'setosa']

versicolor = iris[iris['species'] == 'versicolor']

sns.kdeplot(data=setosa.sepal_length, data2=setosa.sepal_width, cmap= 'coolwarm',shade=False,n_levels =20)
sns.kdeplot(data=versicolor.sepal_length, data2=versicolor.sepal_width, cmap= 'winter', n_levels =20)


plt.grid()
plt.show()