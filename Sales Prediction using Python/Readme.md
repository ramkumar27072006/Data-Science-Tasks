TASK 4 — Sales Prediction using Python (CodeAlpha Data Science Internship)

Objective  
Developed a machine learning model to predict product sales based on advertising expenditure on TV, Radio, and Newspaper.  
The goal was to forecast sales to guide effective marketing budget allocation.

Dataset Information  
Source: Advertising Dataset – Kaggle  
Records: 200 rows  
Features:  
- TV: Advertising budget allocated to TV (in thousands)  
- Radio: Advertising budget allocated to radio (in thousands)  
- Newspaper: Advertising budget allocated to newspapers (in thousands)  
- Sales: Product sales generated (target variable)

Workflow  
Data Loading & Preprocessing  
- Imported dataset, checked and confirmed no missing values.  
- Split data into 80% training and 20% testing sets.

Exploratory Data Analysis (EDA)  
- Seaborn pairplot visualized positive relationships, especially between TV & Sales and Radio & Sales.  
- Heatmap showed correlation: TV (0.78), Radio (0.57), Newspaper (0.23) with Sales.

Model Building  
- Trained Linear Regression, Random Forest Regressor, and Gradient Boosting Regressor models.  
- Evaluated with R², MAE, and RMSE metrics.

Model Performance Results  
| Model             | R² Score | MAE   | RMSE  |  
|-------------------|-----------|--------|--------|  
| Linear Regression | 0.8994    | 1.461  | 1.782  |  
| Random Forest     | 0.9818    | 0.629  | 0.757  |  
| Gradient Boosting | 0.9832    | 0.616  | 0.729  |  

- Best Model: Gradient Boosting Regressor with R² = 0.9832, explaining 98.32% of variance in sales.

Visualizations and Insights  
1. Pairplot: Positive correlation particularly for TV and Radio ads with Sales; Newspaper less impactful.  
2. Correlation Heatmap: Confirmed strongest correlation with TV, followed by Radio, weakest with Newspaper.  
3. Actual vs Predicted Plot: Points align closely along the diagonal, indicating accurate predictions.  
4. Feature Importance: TV highest, Radio moderate, Newspaper least importance.  
5. Residual Distribution: Centered near zero, bell-shaped, indicating unbiased and well-calibrated model.

Results Summary  
- Best Model: Gradient Boosting Regressor  
- R² Score: 0.9832  
- MAE: 0.616  
- RMSE: 0.729  
- Key Drivers: TV and Radio advertisements  
- Weakest Predictor: Newspaper advertisements  
- Dataset Size: 200 samples with 3 predictors

Conclusion  
The Gradient Boosting model achieved excellent predictive accuracy, showing that TV and Radio advertising budgets are the most influential factors on product sales, while Newspaper advertising has limited effect.  
This project illustrates how regression models guide data-driven marketing budget decisions and maximize return on investment.  
It successfully demonstrated the full data science pipeline from preprocessing, EDA to model building, tuning, evaluation, and interpretation.

