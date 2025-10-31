TASK 3 — Car Price Prediction (CodeAlpha Data Science Internship)  
Objective  
Developed a machine learning model to predict the selling price of used cars using attributes such as brand, year, fuel type, transmission, and present price.  
The goal was to help car resellers and buyers assess fair market prices and understand what drives car depreciation.

Dataset Information  
Source: Car Price Prediction – Kaggle Dataset  
Records: 301 rows  
Final features included:  
Present_Price: Current ex-showroom price (in lakhs)  
Year: Year of manufacture (used to derive car age)  
Owner: Number of previous owners  
Fuel_Type: Petrol/Diesel/CNG  
Transmission: Manual/Automatic  
brand: Extracted from car name  
Target Variable: Selling_Price (actual resale price)

Workflow  
Data Loading & Cleaning  
-  Imported dataset, fixed column headers, and extracted brand name from car model.  
-  Cleaned missing entries and standardized numeric columns.

Feature Engineering  
-  Categorical features (Fuel_Type, Transmission, brand) were converted to numeric via one-hot encoding.  
-  Split: 80% training / 20% testing.  
-  Numeric features were standardized for linear models.

Model Building & Evaluation  
-  Trained three models: Linear Regression, Random Forest Regressor, and Gradient Boosting Regressor.  
-  Evaluation metrics: R² Score, MAE, RMSE.

Model Performance Results  
Model | R² Score | MAE | RMSE  
Linear Regression | 0.8676 | 1.200 | 1.746  
Random Forest | 0.9695 | 0.551 | 0.838  
Gradient Boosting | 0.9745 | 0.482 | 0.767  

-  Best Model: GradientBoostingRegressor — R² of 0.9745, meaning it explained 97.45% of the variance in car prices.

Visualizations Generated  
-  Actual vs Predicted Prices — Scatter plot shows strong alignment.  
-  Residuals Distribution — Centered around zero, indicating no bias.  
-  Residuals vs Predicted — Random, confirms model reliability.  
-  Feature Importance Plot — Top predictors are Present_Price, Year, and brand.

Key Insights  
-  Present_Price and Year (car age) critically determine price.  
-  Fuel_Type (especially diesel) and Transmission (automatic) positively influence resale value.  
-  Gradient Boosting outperformed other models, capturing complex relationships.  
-  Minimal residuals confirm generalization capability.

Conclusion  
Gradient Boosting Regression offers extremely accurate car price prediction.  
This project showcases the practical application of machine learning in the automotive market, with effective data preparation, feature engineering, and evaluation using Scikit-learn and Seaborn.  
It helps businesses and individuals estimate fair prices reliably and efficiently.
