Sales Prediction Using Python
Project Overview

This project analyzes the impact of advertising expenditures on product sales and develops a regression model to predict sales figures. The dataset includes advertising budgets allocated across TV, Radio, and Newspaper media channels. The goal is to estimate sales by identifying the degree to which each medium contributes to the final outcome.

This task demonstrates the practical application of regression analysis in business forecasting and marketing analytics.

Dataset

The dataset contains the following columns:

TV (Advertising budget for TV)

Radio (Advertising budget for Radio)

Newspaper (Advertising budget for Newspaper)

Sales (Target variable)

The dataset is clean, structured, and contains no missing values, making it suitable for supervised learning tasks.

Data Preprocessing

The preprocessing steps include:

Loading the dataset using pandas.

Performing exploratory data analysis through pairplots and correlation heatmaps.

Separating the independent variables (TV, Radio, Newspaper) and the dependent variable (Sales).

Splitting the dataset into training and testing sets.

Model Selection

A Linear Regression model was selected to capture the linear relationship between advertising expenditure and sales.

Model Evaluation

Performance metrics:

Metric	Score
MSE	approximately 3.17
R² Score	approximately 0.89

An R² score of 0.89 demonstrates strong model performance, indicating that the advertising features explain approximately 89% of the variability in sales.

How to Run

Install dependencies:

pip install pandas numpy scikit-learn matplotlib seaborn


Run the script:

python "SALES PREDICTION USING PYTHON.py"

Conclusion

The model successfully predicts sales with high accuracy and confirms that TV advertising contributes the most to sales growth, followed by Radio. Newspaper spending exhibits minimal impact. The project effectively illustrates how regression techniques can support marketing decision-making.