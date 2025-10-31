import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv(r"E:\DOWNLOAD\archive (1)\Iris.csv")
df.drop('Id', axis=1, inplace=True)
print(" Dataset loaded successfully!")
print(df.head())


print("\nDataset Information:")
print(df.info())
print("\nNull values:", df.isnull().sum())


plt.figure(figsize=(8,5))
sns.countplot(x='Species', data=df, palette='viridis')
plt.title('Distribution of Iris Species')
plt.show()


sns.pairplot(df, hue='Species', palette='husl')
plt.suptitle("Feature Relationships in Iris Dataset", y=1.02)
plt.show()


plt.figure(figsize=(6,4))
sns.heatmap(df.iloc[:, :-1].corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.show()


X = df.iloc[:, :-1]
y = LabelEncoder().fit_transform(df['Species'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier(n_estimators=120, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


acc = accuracy_score(y_test, y_pred)
print("\n Model Evaluation:")
print("Accuracy:", round(acc, 3))
print(classification_report(y_test, y_pred))


cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, cmap='Blues', fmt='d',
            xticklabels=['Setosa','Versicolor','Virginica'],
            yticklabels=['Setosa','Versicolor','Virginica'])
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()


feature_importance = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
plt.figure(figsize=(7,4))
sns.barplot(x=feature_importance, y=feature_importance.index, palette='mako')
plt.title('Feature Importance in Iris Classification')
plt.xlabel('Importance Score')
plt.show()
