import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('diabetes.csv')
diabete = df[df['Outcome'] == 1]
no_diabete = df[df['Outcome'] == 0]

fig, axs = plt.subplots(1, 2)
axs[0].scatter(diabete.index.values, diabete['Insulin'])
axs[1].scatter(no_diabete.index.values, no_diabete['Insulin'])
plt.show()