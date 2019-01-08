import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
print("The Original Dataframe :\n",tips.head(20), "\n")

sns.barplot(x='smoker', y='tip', hue='sex',data=tips, color = 'red',estimator=np.mean,ci=95,saturation=0.9)
plt.show()