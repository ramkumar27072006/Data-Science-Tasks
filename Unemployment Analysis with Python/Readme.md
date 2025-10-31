TASK 2 — Unemployment Analysis with Python (CodeAlpha Data Science Internship)

Objective  
The project aimed to analyze unemployment trends across Indian regions, highlight disparities, and study the employment impact of the COVID-19 pandemic using Python. The goal was to visualize patterns in unemployment rates and generate socio-economic insights for policy analysis.

Dataset Information  
Source: Unemployment in India – Kaggle Dataset  
Records: 740 rows  
Features:  
-  Region: Indian state/region  
-  Date: Record date (2019–2020)  
-  Frequency: Monthly  
-  Estimated Unemployment Rate (%): Percentage of unemployed individuals  
-  Estimated Employed: Number of employed individuals  
-  Estimated Labour Participation Rate (%): Labor market participation  
-  Area: Rural or Urban classification

Workflow  
Data Loading & Cleaning  
-  Imported CSV and standardized column names  
-  Converted Date to datetime format (dayfirst=True)  
-  Removed null values and checked data consistency

Exploratory Data Analysis (EDA)  
-  Produced summary statistics and descriptive metrics  
-  Used Seaborn and Matplotlib to plot unemployment trends and regional differences  
-  Created boxplots, heatmaps, and region-wise bar charts

Feature Analysis  
-  Aggregated monthly data to highlight temporal trends  
-  Compared unemployment rates between rural and urban areas

Statistical Summary  
-  Total Records: 740  
-  Time Period: May 2019 – June 2020  
-  Mean Unemployment Rate: 11.78%  
-  Minimum: 0.00%, Maximum: 76.74%  
-  Average Labour Participation: 42.63%  
-  Average Employment: ~7.2 million

Regional Insights  
Rank | Region            | Avg. Unemployment Rate (%)  
---- |-------------------|---------------------------  
1    | Tripura           | 28.35  
2    | Haryana           | 26.28  
3    | Jharkhand         | 20.58  
4    | Bihar             | 18.92  
5    | Himachal Pradesh  | 18.54  
Lowest | Meghalaya      | 4.79  

Key Observations  
-  Tripura and Haryana had the highest unemployment rates  
-  Gujarat, Karnataka, and Meghalaya had the lowest  
-  Rural areas showed more stability, urban areas were more volatile

Visualizations and Insights  
1. Unemployment Rate Over Time: Spike during March–June 2020 (COVID-19 lockdown)  
2. Regional Variation: High variability, especially in northern and eastern states  
3. Correlation Heatmap: Unemployment Rate negatively correlated with Employment and Labour Participation  
4. Monthly Trend: Peak in unemployment in April–May 2020  
5. Rural vs Urban: Urban unemployment slightly higher and more volatile

Results Summary  
-  Period: May 2019 – June 2020  
-  Highest Unemployment: Tripura (28.35%)  
-  Lowest Unemployment: Meghalaya (4.79%)  
-  COVID-19 Impact: Sharp spike April–May 2020  
-  Labour Participation: Avg. 42.63%  
-  Urban vs Rural: Urban shows higher variance  
-  Employment and Unemployment are negatively correlated

Conclusion  
Unemployment in India sharply escalated during the COVID-19 lockdown, peaking in several states. Industrialized regions like Gujarat and Karnataka showed quicker recovery, while states such as Tripura and Jharkhand continued to struggle. This analysis demonstrated the value of Python-based EDA and visualization tools (Pandas, Seaborn, Matplotlib) in drawing actionable economic and policy insights.
