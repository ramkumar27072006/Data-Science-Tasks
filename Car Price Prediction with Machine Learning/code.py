import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

DATA_PATH =r"E:\DOWNLOAD\archive (3)\car data.csv"
OUT_DIR = "outputs"
os.makedirs(OUT_DIR, exist_ok=True)
RANDOM_STATE = 42

df = pd.read_csv(DATA_PATH)
print("Loaded:", DATA_PATH)
print(df.head())

df.columns = df.columns.str.strip()
print("\nColumns:", df.columns.tolist())

if 'Car_Name' in df.columns:
    df['brand'] = df['Car_Name'].apply(lambda x: x.split()[0].lower())
elif 'name' in df.columns:
    df['brand'] = df['name'].apply(lambda x: str(x).split()[0].lower())
elif 'Company' in df.columns:
    df['brand'] = df['Company'].astype(str).str.lower()

possible_targets = ['Selling_Price','selling_price','price','Price','Selling Price']
target_col = next((c for c in df.columns if c in possible_targets), None)
if target_col is None:
    raise ValueError("Could not detect target column. Rename target to 'Selling_Price' or update DATA_PATH to correct dataset.")
y = df[target_col]

numeric_cols = ['Present_Price','Kms_Driven','Year','Owner','Mileage','Engine','Power']
X = pd.DataFrame()
for c in numeric_cols:
    if c in df.columns:
        X[c] = pd.to_numeric(df[c], errors='coerce')

if X.shape[1] == 0:
    X = df.select_dtypes(include=[np.number]).drop(columns=[target_col], errors='ignore')

cat_cols = []
for c in ['Fuel_Type','Seller_Type','Transmission','fuel','seller_type','transmission','Area','brand']:
    if c in df.columns and c not in X.columns:
        cat_cols.append(c)
        X[c] = df[c].astype(str)

full = pd.concat([X, y], axis=1)
full = full.dropna(subset=[target_col])
full = full.loc[full.isnull().mean(axis=1) < 0.5].copy()

for col in full.select_dtypes(include=[np.number]).columns:
    full[col].fillna(full[col].median(), inplace=True)

y = full[target_col].astype(float)
X = full.drop(columns=[target_col])

print("\nFinal feature set columns:", X.columns.tolist())
print("Rows:", X.shape[0])

X_encoded = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=RANDOM_STATE)

num_feats = X_train.select_dtypes(include=[np.number]).columns
scaler = StandardScaler()
X_train[num_feats] = scaler.fit_transform(X_train[num_feats])
X_test[num_feats] = scaler.transform(X_test[num_feats])

models = {
    "LinearRegression": LinearRegression(),
    "RandomForest": RandomForestRegressor(n_estimators=200, random_state=RANDOM_STATE),
    "GradientBoosting": GradientBoostingRegressor(n_estimators=200, random_state=RANDOM_STATE)
}

results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    results[name] = {
        "model": model,
        "r2": r2_score(y_test, pred),
        "mae": mean_absolute_error(y_test, pred),
        "mse": mean_squared_error(y_test, pred),
        "pred": pred
    }
    print(f"\n{name} — R2: {results[name]['r2']:.4f} | MAE: {results[name]['mae']:.3f} | RMSE: {np.sqrt(results[name]['mse']):.3f}")

best_name = max(results.keys(), key=lambda k: results[k]['r2'])
best = results[best_name]
print(f"\nBest Model: {best_name} (R2={best['r2']:.4f})")

plt.figure(figsize=(7,6))
plt.scatter(y_test, best['pred'], alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--', linewidth=2)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title(f'Actual vs Predicted ({best_name})')
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, f"actual_vs_predicted_{best_name}.png"), dpi=150)
plt.show()

residuals = y_test - best['pred']
plt.figure(figsize=(7,5))
sns.histplot(residuals, kde=True)
plt.title(f'Residuals Distribution ({best_name})')
plt.xlabel('Residual (Actual - Predicted)')
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, f"residuals_{best_name}.png"), dpi=150)
plt.show()

plt.figure(figsize=(7,5))
plt.scatter(best['pred'], residuals, alpha=0.6)
plt.axhline(0, linestyle='--', color='red')
plt.xlabel('Predicted Price')
plt.ylabel('Residual')
plt.title(f'Residuals vs Predicted ({best_name})')
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, f"residuals_vs_pred_{best_name}.png"), dpi=150)
plt.show()

if hasattr(best['model'], 'feature_importances_'):
    fi = pd.Series(best['model'].feature_importances_, index=X_train.columns).sort_values(ascending=False).head(20)
    plt.figure(figsize=(8,6))
    sns.barplot(x=fi.values, y=fi.index)
    plt.title(f'Feature Importance ({best_name})')
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, f"feature_importance_{best_name}.png"), dpi=150)
    plt.show()

out_df = pd.DataFrame({
    "Actual": y_test,
    "Predicted": best['pred'],
    "Residual": residuals
})
out_df.to_csv(os.path.join(OUT_DIR, f"predictions_{best_name}.csv"), index=False)
print("\nOutputs saved to", OUT_DIR)
