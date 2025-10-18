from sklearn.model_selection import train_test_split
import pandas as pd

titanic = pd.read_csv('titanic.csv')
x = titanic['Age']
y = titanic['Survived']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(X_train)
print(X_test)