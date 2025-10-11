import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('Olympic_Swimming_Results_1912to2020.csv')

men = df[df['Gender'] == 'Men']
women = df[df['Gender'] == 'Women']

tedade_mardha = len(men)
tedade_khanomha = len(women)
tedade_tala_mardha = len(men[men['Rank'] == 1])
tedade_tala_khanomha = len(women[women['Rank'] == 1])

print('darsad talaye aghayan: ', (tedade_tala_mardha/ tedade_mardha)*100)
print('darsad talaye khanoma: ', (tedade_tala_khanomha/tedade_khanomha)*100)


