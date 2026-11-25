# 🔍 Module 05: Exploratory Data Analysis (EDA)

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![SciPy](https://img.shields.io/badge/SciPy-1.10%2B-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)](https://scipy.org/)
[![Status](https://img.shields.io/badge/Status-Completed_✅-00DF72?style=for-the-badge)](#-curriculum-index)

**Exploratory Data Analysis (EDA)** is the foundational investigative discipline of exploring, cleaning, profiling, diagnosing, and mathematically understanding a dataset before training Machine Learning models. Pioneered by mathematician **John W. Tukey** in 1977, EDA shifts modern data science from unverified assumptions to data-driven discovery.

---

## 🏗️ 5-Phase Industry EDA Workflow

```
   ┌─────────────────────────────────────────────────────────────────┐
   │ 1. DATA UNDERSTANDING & PROFILING                               │
   │    Shape, Headers, Dtypes, Scale Taxonomy & Memory Optimization │
   └───────────────────────────────┬─────────────────────────────────┘
                                   ▼
   ┌─────────────────────────────────────────────────────────────────┐
   │ 2. DATA CLEANING & HYGIENE                                      │
   │    String Sanitization, Mixed Datetimes, Out-of-Bounds Coercion │
   └───────────────────────────────┬─────────────────────────────────┘
                                   ▼
   ┌─────────────────────────────────────────────────────────────────┐
   │ 3. MISSINGNESS & DUPLICATE DIAGNOSTICS                          │
   │    Rubin Taxonomy (MCAR/MAR/MNAR), KNN Imputation & Deduplication│
   └───────────────────────────────┬─────────────────────────────────┘
                                   ▼
   ┌─────────────────────────────────────────────────────────────────┐
   │ 4. STATISTICAL & MULTIVARIATE EXPLORATION                       │
   │    Moments, Normality, Pearson/Spearman, VIF, t-tests, ANOVA    │
   └───────────────────────────────┬─────────────────────────────────┘
                                   ▼
   ┌─────────────────────────────────────────────────────────────────┐
   │ 5. SYNTHESIS, WoE/IV & EXECUTIVE SCORECARDS                     │
   │    Information Value, Outlier Consensus & Modeling Readiness    │
   └─────────────────────────────────────────────────────────────────┘
```

---

## 📚 Curriculum Index (20 Notebooks)

| # | Notebook | Core Focus & Techniques | Status |
| :-: | :--- | :--- | :-: |
| **01** | [`01_eda_introduction.ipynb`](./01_eda_introduction.ipynb) | EDA philosophy, John Tukey paradigm, CRISP-DM lifecycle, Exploratory vs Confirmatory analysis | Completed ✅ |
| **02** | [`02_dataset_understanding.ipynb`](./02_dataset_understanding.ipynb) | Shape, column metadata, attribute scale taxonomy (Nominal/Ordinal/Interval/Ratio), memory downcasting | Completed ✅ |
| **03** | [`03_data_profiling.ipynb`](./03_data_profiling.ipynb) | Automated data profiler engine, cardinalities, uniqueness ratio, data dictionary construction | Completed ✅ |
| **04** | [`04_data_cleaning.ipynb`](./04_data_cleaning.ipynb) | String sanitization, mixed datetime parsing, currency regex stripping, domain boundary checks | Completed ✅ |
| **05** | [`05_missing_value_analysis.ipynb`](./05_missing_value_analysis.ipynb) | Rubin's missingness taxonomy (MCAR, MAR, MNAR), missingness indicators, Median vs KNN Imputer | Completed ✅ |
| **06** | [`06_duplicate_analysis.ipynb`](./06_duplicate_analysis.ipynb) | Exact vs business subset duplicates, variance deflation, chronological deduplication | Completed ✅ |
| **07** | [`07_univariate_analysis.ipynb`](./07_univariate_analysis.ipynb) | Continuous moments (Fisher Skewness, Excess Kurtosis), Pareto analysis for categorical features | Completed ✅ |
| **08** | [`08_bivariate_analysis.ipynb`](./08_bivariate_analysis.ipynb) | Continuous-continuous regression slopes, GroupBy aggregations, categorical cross-tabulations | Completed ✅ |
| **09** | [`09_multivariate_analysis.ipynb`](./09_multivariate_analysis.ipynb) | Simultaneous multi-feature interactions, correlation matrices, Principal Component Analysis (PCA) | Completed ✅ |
| **10** | [`10_descriptive_statistics.ipynb`](./10_descriptive_statistics.ipynb) | Parametric vs robust estimators, Trimmed Mean, Interquartile Range (IQR), Median Absolute Deviation (MAD) | Completed ✅ |
| **11** | [`11_distribution_analysis.ipynb`](./11_distribution_analysis.ipynb) | Theoretical vs empirical distributions, Q-Q plots, Shapiro-Wilk, Kolmogorov-Smirnov, D'Agostino tests | Completed ✅ |
| **12** | [`12_correlation_analysis.ipynb`](./12_correlation_analysis.ipynb) | Pearson $r$, Spearman $\rho$, Kendall $\tau$, multicollinearity screening with Variance Inflation Factor (VIF) | Completed ✅ |
| **13** | [`13_statistical_hypothesis_testing.ipynb`](./13_statistical_hypothesis_testing.ipynb) | Welch's two-sample t-test, Mann-Whitney U rank-sum test, One-Way ANOVA, Pearson's Chi-Square | Completed ✅ |
| **14** | [`14_outlier_detection.ipynb`](./14_outlier_detection.ipynb) | Tukey's IQR fences, Modified Z-score, Scikit-Learn Isolation Forest, Local Outlier Factor (LOF) | Completed ✅ |
| **15** | [`15_feature_profiling.ipynb`](./15_feature_profiling.ipynb) | Target separation, quantile binning, Weight of Evidence (WoE) and Information Value (IV) ranking | Completed ✅ |
| **16** | [`16_feature_relationship_analysis.ipynb`](./16_feature_relationship_analysis.ipynb) | Non-linear dependencies via Mutual Information $I(X; Y)$, interaction synergies, Simpson's Paradox | Completed ✅ |
| **17** | [`17_eda_visualization.ipynb`](./17_eda_visualization.ipynb) | Multi-panel distribution grids, masked correlation heatmaps, categorical facet grids | Completed ✅ |
| **18** | [`18_eda_report_generation.ipynb`](./18_eda_report_generation.ipynb) | Automated data quality scorecard, findings synthesis, risk matrices, and modeling readiness criteria | Completed ✅ |
| **19** | [`19_eda_practice.ipynb`](./19_eda_practice.ipynb) | **Comprehensive Practice Lab:** 10 multi-domain real-world dirty data problem sets | Completed ✅ |
| **20** | [`20_eda_mini_project.ipynb`](./20_eda_mini_project.ipynb) | **Capstone Project:** Enterprise Customer Churn & Health Risk Diagnostic Intelligence Suite | Completed ✅ |

---

## 🎯 Main Topics & Concepts Matrix

| Category | Practical Concepts Covered | Primary Notebooks |
| :--- | :--- | :--- |
| **Data Understanding** | Matrix shape, headers, dtypes, scale taxonomy, deep memory downcasting | `01`, `02` |
| **Data Profiling** | Automated dataset summarizer, cardinality audit, data dictionaries | `03` |
| **Data Cleaning** | Whitespace trimming, mixed datetime parsing, regex currency stripping, bounds validation | `04` |
| **Missing Values** | MCAR vs MAR vs MNAR, missingness indicators, Median and KNN Imputation | `05` |
| **Duplicate Analysis** | Exact vs subset duplicates, data leakage prevention, chronological deduplication | `06` |
| **Univariate Analysis** | Skewness, Kurtosis, distribution moments, categorical Pareto distributions | `07` |
| **Bivariate Analysis** | Pearson/Spearman correlation, GroupBy stratified summaries, cross-tabs | `08` |
| **Multivariate Analysis** | Multi-feature matrices, PCA orthogonal projections, high-dimensional intuition | `09` |
| **Descriptive Statistics** | Mean vs Median, Standard Deviation vs MAD, Trimmed Mean, IQR | `10` |
| **Distribution Analysis** | Probability densities (Gaussian, Exponential, Lognormal), Q-Q plots, Shapiro-Wilk | `11` |
| **Correlation Analysis** | Pearson linear, Spearman rank, Kendall tau, Multicollinearity & VIF | `12` |
| **Hypothesis Testing** | Type I/II errors, Welch's t-test, Mann-Whitney U, One-Way ANOVA, Chi-Square | `13` |
| **Outlier Detection** | Tukey IQR rule, Modified Z-score, Isolation Forest, Local Outlier Factor | `14` |
| **Feature Profiling** | Target separation, Weight of Evidence (WoE), Information Value (IV) | `15` |
| **Feature Relationships**| Mutual Information, interaction synergies, Simpson's Paradox | `16` |
| **Visualization** | Multi-panel distribution plots, masked heatmaps, categorical facet grids | `17` |
| **Executive Reporting** | Data quality scorecards, actionable findings matrix, modeling readiness | `18` |
| **Practice & Capstone** | 10 multi-domain problem sets + Full-lifecycle Customer Churn Diagnostic Suite | `19`, `20` |

---

## 🚀 Quickstart & Execution

```bash
# 1. Activate your virtual environment
source venv/bin/activate       # On Linux/macOS
# or: .\venv\Scripts\Activate  # On Windows PowerShell

# 2. Launch JupyterLab or Jupyter Notebook
jupyter lab
```

Navigate to `05_Exploratory_Data_Analysis/` and open any notebook to begin interactive execution!
