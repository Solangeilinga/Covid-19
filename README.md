# 🦠 COVID-19 & World Happiness — Data Analysis Project

## 📌 Project Overview

This project explores the relationship between the **spread of COVID-19** and **socio-economic indicators** using data analysis and visualization techniques in Python.

The goal is to understand whether factors such as **GDP, social support, life expectancy, and freedom** are correlated with the speed of COVID-19 spread across countries.

---

## 📊 Datasets Used

* **Covid19 Confirmed Cases Dataset**

  * Daily confirmed cases per country
* **World Happiness Report**

  * GDP per capita
  * Social support
  * Healthy life expectancy
  * Freedom to make life choices

---

## 🧹 Data Cleaning & Preparation

* Removed irrelevant columns (latitude and longitude)
* Aggregated COVID-19 data by country
* Calculated daily new cases using first-order differentiation
* Defined a key indicator: **Maximum Infection Rate**
* Selected relevant features from the happiness dataset
* Joined both datasets using country names

---

## 📐 Methodology

To measure the spread of COVID-19, the **maximum daily increase in confirmed cases** was used as an indicator.
This metric represents the **highest speed of infection spread** observed in each country.

---

## 📈 Data Visualization

Scatter plots were used to analyze relationships between:

* GDP per capita vs Maximum Infection Rate
* Social support vs Maximum Infection Rate
* Healthy life expectancy vs Maximum Infection Rate
* Freedom to make life choices vs Maximum Infection Rate

Correlation matrices were also computed to quantify linear relationships.

---

## 🔍 Key Insights

* Countries with **higher GDP per capita** tend to show higher maximum infection rates, likely due to better testing and reporting systems.
* **Life expectancy** shows a positive correlation with infection rate, possibly linked to urbanization and international mobility.
* **Freedom to make life choices** presents a moderate relationship with infection spread.
* **Social support** shows a weaker correlation, suggesting indirect or complex effects.


## 🧠 Skills Demonstrated

* Data cleaning and preprocessing (Pandas)
* Feature engineering (infection rate calculation)
* Exploratory Data Analysis (EDA)
* Data visualization (Matplotlib, Seaborn)
* Correlation analysis
* Critical interpretation of results

---

## 🧾 Tools & Technologies

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Jupyter Notebook

---

## 📌 Conclusion

This project highlights how data analysis can be used to explore complex global issues.
While socio-economic indicators show correlations with COVID-19 spread, multiple interacting factors must be considered for deeper insights.
