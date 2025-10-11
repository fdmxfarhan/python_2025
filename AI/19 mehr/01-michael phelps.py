import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('Olympic_Swimming_Results_1912to2020.csv')

michaelPhelps = df[df['Athlete'] == 'Michael Phelps'][df['Distance (in meters)'] == '100m']

print(michaelPhelps['Results'].min())