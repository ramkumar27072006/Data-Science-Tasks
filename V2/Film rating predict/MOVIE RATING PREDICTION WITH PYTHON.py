import pandas as pd

df = pd.read_csv(r"E:\codsoft\Datasets\imdb_top_1000.csv")
print(df.head())
print(df.info())



df = df[['Genre','IMDB_Rating','Director','Star1','Star2','Star3','Star4','No_of_Votes']]
df = df.dropna()

# Encode categorical features
df_encoded = pd.get_dummies(df, drop_first=True)


from sklearn.model_selection import train_test_split

X = df_encoded.drop("IMDB_Rating", axis=1)
y = df_encoded["IMDB_Rating"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
