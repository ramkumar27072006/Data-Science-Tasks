Movie Rating Prediction Using Python
Project Overview

This project focuses on predicting the IMDb rating of a film using machine learning regression techniques. The dataset consists of various film-related attributes such as title, release year, runtime, genre, cast, number of votes, gross revenue, and other descriptive features. The objective is to develop a predictive model capable of estimating a movie’s rating based on these available metadata variables.

The exercise demonstrates fundamental steps of a supervised regression workflow: data cleaning, preprocessing, feature engineering, model training, evaluation, and interpretation.

Dataset

The dataset used is the IMDb Top 1000 Movies dataset, which includes the following important features:

Series_Title

Released_Year

Runtime (in minutes)

Genre

Director

Star1, Star2, Star3, Star4

No_of_Votes

Gross Revenue

IMDb Rating (target variable)

The dataset contains both numerical and categorical features and includes some missing values that require proper handling.

Data Preprocessing

The data underwent several essential preprocessing steps:

Removal of irrelevant columns such as poster links and descriptive text where not required.

Cleaning and conversion of text-based numerical columns:

Conversion of "Gross" to numeric values.

Extraction of numeric minutes from "Runtime".

Conversion of "Released_Year" to integer values.

Handling missing values through either removal or imputation.

One-hot encoding of categorical columns such as Genre, Director, and cast members.

Splitting of the dataset into training and testing sets.

Model Selection

A Linear Regression model was initially chosen to establish a baseline.
Additional models such as RandomForestRegressor may be tested to improve performance.

Model Evaluation

Performance metrics used include:

Mean Squared Error (MSE)

Coefficient of Determination (R² Score)

Typical results obtained:

Metric	Score
MSE	approximately 0.05
R² Score	approximately 0.12–0.22

The relatively low R² score indicates that IMDb ratings depend on subjective human opinions, which are not fully captured by the available numeric and categorical metadata.

How to Run

Install dependencies:

pip install pandas numpy scikit-learn matplotlib seaborn


Execute the script:

python "MOVIE RATING PREDICTION WITH PYTHON.py"

Conclusion

This project highlights the challenges of predicting subjective ratings using structured metadata alone. Although the model offers reasonable baseline predictions, performance can be improved through advanced feature engineering, integration of natural language processing on textual descriptions, and usage of more complex ensemble algorithms.