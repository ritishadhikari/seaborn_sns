import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


number = np.random.randn(150)
'''
sns.distplot(a=number,color='red', label=)
'''

label_dist = pd.Series(data=number,name='variable X')
sns.distplot(label_dist,vertical=False,color='green',hist=True, rug=True)

plt.show()