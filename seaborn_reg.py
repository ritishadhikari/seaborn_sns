import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

tips = sns.load_dataset('tips')
print("Original Tips Dataset :\n", tips.head(), "\n")

sns.regplot(data=tips, x ='total_bill',y ='tip',scatter_kws={'color':'red'},line_kws={'color' : 'black', 'linewidth':4},marker='o',ci=95,x_jitter=0.05,x_estimator=np.mean)

mean =[2,5]
cov = [[1.1,0.4],[2.2,0.3]]

x_value, y_value = np.random.multivariate_normal(mean=mean,cov=cov,size=500).T
#sns.regplot(x=x_value,y=y_value, color='red')


plt.show()