import pandas as pd

df = pd.read_csv(r"E:\codsoft\Datasets\creditcard.csv")
df.head()


from imblearn.over_sampling import SMOTE

X = df.drop('Class', axis=1)
y = df['Class']

sm = SMOTE()
X_res, y_res = sm.fit_resample(X, y)


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)


from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X_train, y_train)


from sklearn.metrics import classification_report, confusion_matrix

pred = model.predict(X_test)

print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))
