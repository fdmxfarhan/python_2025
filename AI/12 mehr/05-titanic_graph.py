import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')
df = df.sort_values('Age')
a = np.arange(0, len(df), 1)
plt.plot(a, df['Age'])
plt.show()