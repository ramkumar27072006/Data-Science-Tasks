TASK 2 — Unemployment Analysis with Python (CodeAlpha Data Science Internship)  
Objective  
To analyze and visualize unemployment trends across India before, during, and after the COVID-19 pandemic using Python.  
The goal is to identify key regional variations, pandemic impacts, and labor participation insights through data visualization and analysis.

Dataset Information  
Source: Unemployment in India (Kaggle)  
Records: 740 rows  
Features:  
Column/Description  
Region — Indian state or region  
Date — Data recording date  
Frequency — Reporting frequency (Monthly)  
Estimated Unemployment Rate (%) — % of unemployed individuals  
Estimated Employed — Number of employed individuals  
Estimated Labour Participation Rate (%) — % of people participating in the labor market  
Area — Classification as Rural or Urban

Workflow  
Data Loading and Cleaning  
-  Loaded CSV file using Pandas.  
-  Removed missing values and cleaned column names.  
-  Converted the Date column to datetime format for time-based plotting.  
Exploratory Data Analysis (EDA)  
-  Used Seaborn and Matplotlib for multiple visualizations.  
-  Added monthly grouping and region-wise aggregation.  
Feature Engineering  
-  Extracted month from date for time series analysis.  
-  Grouped data to compute monthly and regional averages.  
Data Visualization  
-  Created six high-quality plots for regional and temporal trends.

Visualizations and Insights  
1. Unemployment Rate Over Time  
-  Line Chart  
-  Sharp spike in unemployment between March–June 2020 aligns with COVID-19 lockdown.  
-  Gradual recovery observed post-2021.

2. Regional Variation (Boxplot)  
-  Box Plot grouped by Region  
-  Northern and Eastern states show higher fluctuations in unemployment.  
-  Tripura and Jharkhand have the highest rates.

3. Correlation Heatmap  
-  Seaborn Heatmap  
-  Unemployment Rate shows negative correlation with Employment and Labour Participation Rate.  
-  As employment increases, unemployment naturally decreases.

4. Monthly Average Trend  
-  Line Plot (aggregated monthly)  
-  April 2020 saw the highest average unemployment, reflecting the pandemic’s economic impact.

5. Region-wise Average Unemployment Rate  
-  Horizontal Bar Chart  
-  Highest: Tripura, Jharkhand, Delhi  
-  Lowest: Gujarat, Tamil Nadu, Karnataka  
-  Indicates industrial and economic resilience differences.

6. Area-wise Comparison (Rural vs Urban)  
-  Box Plot  
-  Urban areas display slightly higher unemployment variability than rural areas, reflecting more volatile job markets.

Results Summary  
Aspect/Observation  
Dataset Size: 740 entries  
Time Period: May 2019 – June 2021  
Peak Unemployment: April–May 2020 (Pandemic lockdown)  
Most Affected Regions: Tripura, Jharkhand, Delhi  
Least Affected Regions: Gujarat, Tamil Nadu, Karnataka  
Area Comparison: Urban > Rural (in variation)  
Correlation: Employment and Unemployment are negatively correlated.

Conclusion  
The unemployment rate in India dramatically spiked during the COVID-19 lockdown but gradually stabilized after 2021.  
Regions with stronger industrial economies (Gujarat, Tamil Nadu) recovered more quickly, while others remained affected longer.  
This project demonstrates the use of Python, Pandas, and Seaborn to understand real-world economic data and extract insights that are relevant to policy-making.
