import pandas as pd

df = pd.read_csv(r"E:\codsoft\Datasets\Advertising.csv")
df.head()


import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(df)
plt.show()


from sklearn.model_selection import train_test_split

X = df[['TV','Radio','Newspaper']]
y = df['Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)


from sklearn.metrics import mean_squared_error, r2_score

pred = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, pred))
print("R2 Score:", r2_score(y_test, pred))
