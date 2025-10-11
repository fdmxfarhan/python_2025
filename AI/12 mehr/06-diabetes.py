import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('diabetes.csv')
diabete = df[df['Outcome'] == 1]
no_diabete = df[df['Outcome'] == 0]
print('diabete: ', len(diabete))
print('no diabete: ', len(no_diabete))
