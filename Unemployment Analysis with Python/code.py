import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r"E:\DOWNLOAD\archive (2)\Unemployment in India.csv")
print(" Dataset Loaded Successfully\n")
print(df.head())


df.columns = df.columns.str.strip()      
df.dropna(inplace=True)
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

print("\n Cleaned Columns:", df.columns.tolist())
print("\nDataset Info:")
print(df.info())


print("\n Statistical Summary:")
print(df.describe())


plt.figure(figsize=(10,5))
sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', data=df, color='orange')
plt.title(' Unemployment Rate Over Time (India)')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.show()


plt.figure(figsize=(12,6))
sns.boxplot(x='Region', y='Estimated Unemployment Rate (%)', data=df, palette='magma')
plt.title('Regional Variation in Unemployment Rate')
plt.xticks(rotation=90)
plt.show()


plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation between Economic Indicators')
plt.show()

df['Month'] = df['Date'].dt.to_period('M')
monthly_avg = df.groupby('Month')['Estimated Unemployment Rate (%)'].mean()

plt.figure(figsize=(10,5))
monthly_avg.plot(kind='line', color='teal', marker='o')
plt.title('Average Monthly Unemployment Rate in India')
plt.xlabel('Month')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.show()


region_avg = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values(ascending=False)
print("\n Average Unemployment Rate by Region:\n", region_avg)

plt.figure(figsize=(10,6))
sns.barplot(x=region_avg.values, y=region_avg.index, palette='viridis')
plt.title('Average Unemployment Rate by Region')
plt.xlabel('Unemployment Rate (%)')
plt.ylabel('Region')
plt.show()


plt.figure(figsize=(7,5))
sns.boxplot(x='Area', y='Estimated Unemployment Rate (%)', data=df, palette='Set2')
plt.title('Unemployment Rate: Rural vs Urban Areas')
plt.show()

print("\n Analysis Completed Successfully!")
