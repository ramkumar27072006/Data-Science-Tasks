TASK 1 — Iris Flower Classification (CodeAlpha Data Science Internship)
Objective  
To classify Iris flower species — Setosa, Versicolor, and Virginica — based on four botanical measurements:  
Sepal Length  
Sepal Width  
Petal Length  
Petal Width  
The goal is to build a machine learning model that accurately predicts the flower species and visualize relationships among features.

Dataset Information  
Source: [Iris CSV Dataset (Kaggle)](https://www.kaggle.com/datasets/saurabh00007/iriscsv)  
Records: 150 rows  
Features:  
FeatureDescription  
SepalLengthCm  
Length of the sepal (cm)  
SepalWidthCm  
Width of the sepal (cm)  
PetalLengthCm  
Length of the petal (cm)  
PetalWidthCm  
Width of the petal (cm)  
Species  
Target (Setosa, Versicolor, Virginica)

Workflow  
Data Loading & Cleaning:  
Imported dataset using Pandas and removed unnecessary Id column.    
Exploratory Data Analysis (EDA):  
Checked for missing values and feature correlations.  
Used Seaborn and Matplotlib to visualize species distribution and feature relationships.  
Feature Encoding:  
Converted the categorical species column into numerical labels using LabelEncoder.  
Model Training:  
Algorithm: Random Forest Classifier  
Train-test split: 80% train, 20% test  
Trained with 120 estimators for stable accuracy.  
Evaluation Metrics:  
Accuracy  
Precision, Recall, F1-score  
Confusion Matrix Visualization  
Feature Importance Graph

Visualizations and Their Meanings  
1. Species Distribution  
Plot: Bar chart showing the number of samples per species.  
Insight: All three species have equal representation (50 each), ensuring a balanced dataset.

2. Pairplot of Features  
Plot: Seaborn pairplot with color-coded species.  
Insight:  
Setosa is clearly separable based on petal measurements.  
Versicolor and Virginica overlap slightly, showing minor feature similarity.

3. Correlation Heatmap  
Plot: Heatmap of correlations between sepal and petal dimensions.  
Insight: Petal length and width are strongly correlated, making them key features for classification.

4. Confusion Matrix  
Plot: Heatmap showing correct vs misclassified predictions.  
Insight: All predictions are correct (diagonal matrix), confirming perfect model performance.

5. Feature Importance  
Plot: Horizontal bar graph of feature importance scores.  
Insight:  
Petal Length and Petal Width are the most influential predictors.  
Sepal features contribute less to classification accuracy.

Results  
MetricScore  
Accuracy 1.00  
Precision 1.00  
Recall 1.00  
F1-Score 1.00  
Model achieved perfect classification on the test data.

Conclusion  
Random Forest successfully identified species with 100% accuracy.  
Visual analysis showed petal measurements are the most discriminative features.  
This project demonstrates the power of ensemble learning for simple, well-structured datasets.
