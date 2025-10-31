import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np

df = pd.read_csv(r"E:\DOWNLOAD\archive (4)\Advertising.csv")
print("Dataset Loaded Successfully\n")
print(df.head())

print("\nDataset Info:")
print(df.info())
print("\nMissing Values:\n", df.isnull().sum())

sns.pairplot(df)
plt.suptitle("Feature Relationships in Advertising Dataset", y=1.02)
plt.show()

plt.figure(figsize=(6,4))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

X = df[['TV','Radio','Newspaper']]
y = df['Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=200, random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=200, random_state=42)
}

results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    r2 = r2_score(y_test, pred)
    mae = mean_absolute_error(y_test, pred)
    rmse = np.sqrt(mean_squared_error(y_test, pred))
    results[name] = (r2, mae, rmse)
    print(f"{name} — R²: {r2:.4f} | MAE: {mae:.3f} | RMSE: {rmse:.3f}")

best_model = max(results, key=lambda x: results[x][0])
print(f"\nBest Model: {best_model} (R²={results[best_model][0]:.4f})")

model = models[best_model]
y_pred = model.predict(X_test)

plt.figure(figsize=(7,6))
plt.scatter(y_test, y_pred, color='teal', alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Actual Sales')
plt.ylabel('Predicted Sales')
plt.title(f'Actual vs Predicted Sales ({best_model})')
plt.show()

if hasattr(model, 'feature_importances_'):
    fi = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
    plt.figure(figsize=(6,4))
    sns.barplot(x=fi.values, y=fi.index, palette='magma')
    plt.title(f'Feature Importance ({best_model})')
    plt.xlabel('Importance Score')
    plt.show()

residuals = y_test - y_pred
plt.figure(figsize=(7,4))
sns.histplot(residuals, kde=True, color='blue')
plt.title(f'Residual Distribution ({best_model})')
plt.xlabel('Residual (Actual - Predicted)')
plt.show()

print("\nSales Prediction Analysis Completed Successfully!")
