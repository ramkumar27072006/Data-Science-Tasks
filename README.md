Data Science Projects – Complete Portfolio
This repository contains a collection of four complete data science projects, covering data preprocessing, exploratory analysis, visualization, machine learning, and model evaluation using Python.
Each project demonstrates the application of machine learning to a real-world problem domain — from biology to economics, automotive analytics, and marketing.

Table of Contents
Task 1 – Iris Flower Classification
Task 2 – Unemployment Analysis
Task 3 – Car Price Prediction
Task 4 – Sales Prediction
Technologies Used
Key Learnings
Conclusion

Task 1 – Iris Flower Classification
Objective
To build a classification model that predicts the species of an Iris flower based on its sepal and petal dimensions.
Dataset
Source: UCI Machine Learning Repository
Samples: 150
Features: SepalLength, SepalWidth, PetalLength, PetalWidth, Species
Workflow
Data loading and verification
Visualization using Pairplot, Boxplot, and Heatmap
Feature scaling with StandardScaler
Model training using Support Vector Classifier (SVC)
Evaluation using accuracy, precision, recall, and F1-score
Results
Accuracy: 1.00 (100%)
Precision: 1.00
Recall: 1.00
F1-Score: 1.00
Perfect classification — all three species correctly identified.
Visuals
Pairplot: Distinct class separability
Heatmap: Strong correlation between petal features
Boxplot: Feature distribution per species
Confusion matrix: 100% correct predictions

Task 2 – Unemployment Analysis
Objective
To analyze unemployment trends in India (2019–2020) and visualize regional differences and COVID-19 effects using Python-based data analytics.
Dataset
Source: Public dataset (Unemployment in India)
Records: 740
Columns: Region, Date, Estimated Unemployment Rate (%), Employed, Labour Participation (%), Area
Workflow
Cleaned dataset, parsed dates, handled missing values
Performed Exploratory Data Analysis (EDA)
Visualized region-wise and rural/urban unemployment
Measured COVID-19 impact during April–June 2020
Key Findings
Mean Unemployment Rate: 11.78%
Max Rate: 76.74%
Highest Region: Tripura (28.35%)
Lowest Region: Meghalaya (4.79%)
Avg Labour Participation: 42.63%
Visuals
Line plot: Unemployment over time
Boxplot: Region-wise variance
Heatmap: Feature correlations
Bar chart: Top 10 highest unemployment states
Insights
COVID-19 lockdown caused sharp unemployment rise.
Urban areas more volatile than rural.
Employment and unemployment are inversely related.
Conclusion: Tripura and Haryana had the highest unemployment; Meghalaya had the lowest.

Task 3 – Car Price Prediction
Objective
To predict the selling price of used cars based on attributes like brand, age, fuel type, and transmission.
Dataset
Source: Car price dataset (Kaggle)
Records: 301
Features Used: Present_Price, Year, Owner, Fuel_Type, Transmission, Brand
Workflow
Data cleaning and encoding of categorical variables
Feature selection and splitting into training/testing sets
Model training with:
Linear Regression
Random Forest Regressor
Gradient Boosting Regressor
Evaluation using R², MAE, and RMSE metrics
Model Performance
Linear Regression: R² 0.8676, MAE 1.200, RMSE 1.746
Random Forest: R² 0.9695, MAE 0.551, RMSE 0.838
Gradient Boosting: R² 0.9745, MAE 0.482, RMSE 0.767
Best Model: Gradient Boosting (R² = 0.9745)
Visuals
Predicted vs Actual Price Plot
Feature Importance Plot
Residual Distribution
Insights
Car price depends strongly on brand, fuel type, and manufacture year.
Diesel and newer models have higher resale value.
Conclusion: Gradient Boosting offers the best balance of accuracy and interpretability.

Task 4 – Sales Prediction
Objective
To predict product sales based on advertising spending across TV, Radio, and Newspaper platforms.
Dataset
Source: Advertising dataset
Records: 200
Features: TV, Radio, Newspaper, Sales
Workflow
Data loading and checking for missing values
Performed EDA (Pairplot, Heatmap, Correlation Analysis)
Trained and compared regression models:
Linear Regression
Random Forest Regressor
Gradient Boosting Regressor
Evaluated using R², MAE, and RMSE
Model Results
Linear Regression: R² 0.8994, MAE 1.461, RMSE 1.782
Random Forest: R² 0.9818, MAE 0.629, RMSE 0.757
Gradient Boosting: R² 0.9832, MAE 0.616, RMSE 0.729
Best Model: Gradient Boosting (R² = 0.9832)
Visuals
Pairplot: Correlation between media and sales
Heatmap: Strong TV–Sales relationship
Barplot: Feature Importance
Residual Distribution
Insights
TV advertising is the most powerful sales driver.
Radio moderately effective; Newspaper least.
Residuals show unbiased, high-quality model predictions.
Conclusion: Gradient Boosting achieved exceptional performance (R² = 0.9832) — perfect for real-world marketing optimization.

Technologies Used
CategoryTools / Libraries
Language: Python
Data Handling: Pandas, NumPy
Visualization: Matplotlib, Seaborn
Machine Learning: Scikit-learn
Models: SVM, Linear Regression, Random Forest, Gradient Boosting
Environment: VS Code / Jupyter Notebook

Key Learnings
Effective data cleaning and preprocessing
Strong EDA skills with Seaborn & Matplotlib
Understanding of classification and regression models
Evaluation using R², MAE, RMSE, and confusion matrices
Interpretation of feature importance and correlations
Structuring machine learning projects systematically

Conclusion
These four projects collectively demonstrate end-to-end applications of data science and machine learning — from understanding datasets and exploring patterns to building predictive models with high accuracy.
Each task emphasizes how analytical thinking and data-driven insights can be applied across biology, economics, automotive, and marketing domains.
