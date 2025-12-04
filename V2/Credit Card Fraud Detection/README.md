Credit Card Fraud Detection
Project Overview

This project builds a machine learning model to detect fraudulent credit card transactions. Since fraudulent transactions represent a small minority of the dataset, addressing class imbalance is a major challenge. The objective is to classify each transaction as fraudulent or legitimate using features derived through PCA transformation.

This project demonstrates data balancing, classification modeling, and evaluation using appropriate performance metrics.

Dataset

The dataset contains anonymized numerical features:

V1 to V28 (Principal Component Analysis–transformed features)

Amount

Class (0 = genuine, 1 = fraudulent)

The dataset is highly imbalanced, with fraudulent transactions representing only a very small portion of the total records.

Data Preprocessing

Key preprocessing steps:

Normalization of the "Amount" field.

Handling severe class imbalance using SMOTE (Synthetic Minority Oversampling Technique).

Splitting the dataset into training and testing sets.

Preparing data for classification models.

Model Selection

A Random Forest Classifier was used due to its robustness, ability to handle complex patterns, and suitability for imbalanced datasets when combined with SMOTE.

Model Evaluation
Confusion Matrix
[[56739    11]
 [    0 56976]]

Performance Metrics:
Metric	Score
Accuracy	1.00
Precision	1.00
Recall	1.00
F1 Score	1.00

The model achieved perfect scores primarily due to class balance created through SMOTE and the nature of the dataset.

How to Run

Install required dependencies:

pip install pandas numpy scikit-learn imbalanced-learn matplotlib seaborn


Execute the script:

python "CREDIT CARD FRAUD DETECTION.py"

Conclusion

The Random Forest model, combined with oversampling using SMOTE, performs exceptionally well on the credit card fraud dataset. This project successfully demonstrates classification on highly imbalanced datasets and highlights essential techniques to improve performance in fraud detection scenarios.