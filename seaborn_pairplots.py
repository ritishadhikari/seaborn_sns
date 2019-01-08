import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')
print("Iris Dataset : \n", iris.head(),"\n")
print("Tips Dataset : \n", tips.head(),"\n")

sns.pairplot(data=tips,hue='sex',palette='husl',kind='reg', markers=['D','s'], x_vars=['tip'],y_vars=['total_bill'],height=4,diag_kind='kde')

#sns.pairplot(data=iris,diag_kind='hist')
plt.show()