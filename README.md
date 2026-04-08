# Sales Data Cleaning and Preparation Using Python (pandas)

##  Project Overview

This project focuses on cleaning and preparing a messy sales dataset for analysis using Python and pandas.
The dataset contains common real-world data issues such as missing values, inconsistent text formatting, and data entry errors.

The goal of this project is to transform raw, unstructured data into a clean and reliable dataset that can be used for accurate analysis and decision-making.



##  Dataset

The dataset used in this project is a manually created CSV file called **dirty_sales.csv**.

### Key Issues Identified:

* Missing values in the `Amount` and `Region` columns
* Inconsistent text formatting (e.g., "gauteng", "Kzn", "Western cape")
* Extra spaces in text fields (e.g., " Laptop ")
* Potential duplicate records



##  Tools & Technologies

* Python
* pandas



##  Data Cleaning Steps

### 1. Data Inspection

* Loaded the dataset using pandas
* Checked data types and structure using `.info()`
* Identified missing values using `.isnull().sum()`

### 2. Data Cleaning

* Removed leading and trailing spaces using `.str.strip()`
* Standardized text formatting using `.str.title()`
* Corrected inconsistent values using `.replace()`

### 3. Handling Missing Values

* Filled missing numeric values (`Amount`) with the column average
* Filled missing categorical values (`Region`) with "Unknown"

### 4. Data Type Conversion

* Converted `Date` column to datetime format
* Ensured `Amount` column is numeric

### 5. Removing Duplicates

* Removed duplicate rows to ensure data accuracy


##  Sample Analysis

After cleaning, basic analysis was performed to understand sales performance:

* Total sales by region
* Identification of top-performing regions



##  Key Insights

* Gauteng generated the highest total sales
* Data inconsistencies can significantly affect analysis results
* Cleaning data improves accuracy and reliability of insights



##  Future Improvements

* Add data visualizations (bar charts, pie charts)
* Expand dataset for deeper analysis
* Build a dashboard using Power BI or Tableau



##  Project Files

* `dirty.csv` → Raw dataset
* `clean_sales.py` → Data cleaning script



##  Conclusion

This project demonstrates the importance of data cleaning in the data analysis process.
By transforming messy data into a structured format, businesses can make more accurate and informed decisions.



##  Author

Buhle
Aspiring Data Analyst | Python | SQL | Data Analysis
