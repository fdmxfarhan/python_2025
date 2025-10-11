import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')
print('oldest person:')
print(df['Age'].max())

