import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Boston']
})
print(df['City'])
print(df.loc[1])
print(df.iloc[2:4])
print(df.head())      # پنج تا سطر اول
print(df.tail())    # پنج تا سطر آخر