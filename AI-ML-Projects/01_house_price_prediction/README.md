# 🏡 House Price Prediction System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.2+-orange.svg)]()
[![Level](https://img.shields.io/badge/Level-Beginner-brightgreen.svg)]()

## 📌 Project Overview
Predict real estate property valuations using property characteristics: location, total square footage, bedroom count, bathroom count, age, and neighborhood quality metrics.

## 🛠️ Tech Stack & Algorithms
- **Data Processing:** NumPy, Pandas
- **Algorithms:** Linear Regression, Ridge/Lasso, Random Forest Regressor, Gradient Boosting
- **Evaluation Metrics:** Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), $R^2$ Score
- **Deployment:** Streamlit Interactive Web Application

## 📂 Dataset Information
- **Features:** `sqft_living`, `bedrooms`, `bathrooms`, `floors`, `waterfront`, `view`, `condition`, `grade`, `yr_built`
- **Target:** `price` ($USD)

## 🚀 Quickstart
```bash
# Run Jupyter Notebook
jupyter notebook notebook.ipynb

# Launch Streamlit Interface
streamlit run app.py
```
