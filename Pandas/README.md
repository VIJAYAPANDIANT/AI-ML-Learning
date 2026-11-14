<div align="center">

# 📊 Pandas for AI, Data Science & Machine Learning

### *A Production-Grade 27-Notebook Masterclass: From Tabular Fundamentals to Feature Engineering & Business Analytics*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Curriculum](https://img.shields.io/badge/Curriculum-27%20Notebooks-blueviolet?style=for-the-badge&logo=gitbook&logoColor=white)](#-curriculum-index)
[![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)](#-curriculum-index)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](../#--license)

<br/>

<p align="center">
  <b>27 Interactive Notebooks</b> • <b>Data Wrangling & Cleaning</b> • <b>Time Series & Pivot Tables</b> • <b>Retail Analytics Capstone</b>
</p>

<p align="center">
  <a href="../"><b>🏠 Main Repository</b></a> •
  <a href="../Python/"><b>🐍 Python Module</b></a> •
  <a href="../Numpy/"><b>🔢 NumPy Module</b></a> •
  <a href="#-curriculum-index"><b>📚 Curriculum Index</b></a> •
  <a href="#-topic-categories--learning-path"><b>🗂️ Topic Categories</b></a> •
  <a href="#-capstone-project-spotlight"><b>🛒 Capstone Project</b></a> •
  <a href="#-performance--optimization-tips"><b>⚡ Optimization</b></a> •
  <a href="#-how-to-run"><b>🚀 How to Run</b></a>
</p>

</div>

---

## 📖 Module Overview

Pandas is the bedrock of the modern data science and machine learning ecosystem. In real-world AI/ML projects, up to 80% of an engineer's time is dedicated to **data cleaning, transformation, feature engineering, and exploratory data analysis (EDA)**.

This module delivers a code-first, production-oriented curriculum structured across **27 interactive Jupyter Notebooks**. It guides you from raw data ingestion and missing value treatments to complex multi-table relational merges, time-series feature generation, cross-tabulations, and memory footprint optimization.

---

## 🗂️ Topic Categories & Learning Path

| Category | Primary Focus & Capabilities | Notebooks |
| :--- | :--- | :---: |
| **1. Fundamentals** | Core Pandas architecture, 1D Series, 2D DataFrames, and dimensional metadata | `01` – `03` |
| **2. Data Handling** | Reading CSV/JSON/Excel, structural inspection, index slicing, and `.loc`/`.iloc` selection | `04` – `07` |
| **3. Data Cleaning** | Imputing missing values, removing duplicates, and standardizing categorical sentinels | `10`, `11`, `20` |
| **4. Data Manipulation** | Adding calculated metrics, multi-condition boolean filtering, and multi-key sorting | `08`, `09`, `12` |
| **5. Data Analysis** | Split-Apply-Combine groupby routines, multi-metric aggregations, and statistical profiling | `13`, `14`, `23` |
| **6. Combining Data** | Relational merges (inner, left, outer), index joins, and multi-axis concatenation | `15`, `16` |
| **7. Advanced Operations** | Custom `.apply()`, mapping functions, multidimensional pivot tables, and crosstabs | `17`, `21`, `22` |
| **8. Other Operations** | Vectorized text cleaning (`.str`), temporal dates (`.dt`), storage formats, and memory downcasting | `18`, `19`, `24`, `25` |
| **9. Practice & Capstone** | 10 Algorithmic problem sets and the **Global E-Commerce & Retail Analytics Pipeline** | `26`, `27` |

---

## 🗂️ Directory Architecture

```text
Pandas/
│
├── README.md
│
├── 01_pandas_introduction.ipynb             # Category 1: Fundamentals
├── 02_pandas_series.ipynb
├── 03_pandas_dataframe.ipynb
│
├── 04_pandas_reading_data.ipynb             # Category 2: Data Handling
├── 05_pandas_inspecting_data.ipynb
├── 06_pandas_data_selection.ipynb
├── 07_pandas_indexing_and_slicing.ipynb
│
├── 08_pandas_filtering.ipynb                # Category 4: Data Manipulation
├── 09_pandas_adding_modifying_columns.ipynb
│
├── 10_pandas_handling_missing_values.ipynb  # Category 3: Data Cleaning
├── 11_pandas_handling_duplicates.ipynb
├── 12_pandas_sorting.ipynb                  # Category 4: Data Manipulation
│
├── 13_pandas_groupby.ipynb                  # Category 5: Data Analysis
├── 14_pandas_aggregation.ipynb
│
├── 15_pandas_merging_and_joining.ipynb      # Category 6: Combining Data
├── 16_pandas_concatenation.ipynb
│
├── 17_pandas_apply_map_lambda.ipynb         # Category 7: Advanced Operations
├── 18_pandas_string_operations.ipynb        # Category 8: Other Operations
├── 19_pandas_datetime.ipynb
├── 20_pandas_renaming_and_replacing.ipynb   # Category 3: Data Cleaning
├── 21_pandas_pivot_tables.ipynb             # Category 7: Advanced Operations
├── 22_pandas_crosstab.ipynb
├── 23_pandas_statistical_functions.ipynb    # Category 5: Data Analysis
├── 24_pandas_exporting_data.ipynb           # Category 8: Other Operations
├── 25_pandas_optimization.ipynb
│
├── 26_pandas_practice.ipynb                 # Category 9: Practice & Capstone
└── 27_pandas_mini_project.ipynb
```

---

## 📚 Curriculum Index

| # | Notebook | Category | Core Concepts & APIs | Status |
| :-: | :--- | :--- | :--- | :-: |
| **01** | [`01_pandas_introduction.ipynb`](./01_pandas_introduction.ipynb) | Fundamentals | What is Pandas, NumPy foundation, basic DataFrame creation, metadata inspection | ✅ |
| **02** | [`02_pandas_series.ipynb`](./02_pandas_series.ipynb) | Fundamentals | 1D labeled Series, dictionary conversion, indexing, vectorized calculations | ✅ |
| **03** | [`03_pandas_dataframe.ipynb`](./03_pandas_dataframe.ipynb) | Fundamentals | 2D tabular structure, column extraction (Series vs DataFrame), custom index | ✅ |
| **04** | [`04_pandas_reading_data.ipynb`](./04_pandas_reading_data.ipynb) | Data Handling | `read_csv`, `read_json`, parameters: `sep`, `usecols`, `nrows`, `parse_dates` | ✅ |
| **05** | [`05_pandas_inspecting_data.ipynb`](./05_pandas_inspecting_data.ipynb) | Data Handling | `.head()`, `.sample()`, `.info()`, `.describe()`, `.value_counts(normalize=True)` | ✅ |
| **06** | [`06_pandas_data_selection.ipynb`](./06_pandas_data_selection.ipynb) | Data Handling | Single/multi column selection, scalar cell retrieval, row selection | ✅ |
| **07** | [`07_pandas_indexing_and_slicing.ipynb`](./07_pandas_indexing_and_slicing.ipynb) | Data Handling | `.loc[]` (label) vs. `.iloc[]` (integer), boundary inclusion, fast `.at[]`/`.iat[]` | ✅ |
| **08** | [`08_pandas_filtering.ipynb`](./08_pandas_filtering.ipynb) | Data Manipulation | Boolean masks, bitwise `&`/`\|`/`~`, `.isin()`, `.between()`, `.query()` expressions | ✅ |
| **09** | [`09_pandas_adding_modifying_columns.ipynb`](./09_pandas_adding_modifying_columns.ipynb) | Data Manipulation | Derived columns, `.assign()`, `.insert()`, conditional assignment (`np.where`), `.drop()` | ✅ |
| **10** | [`10_pandas_handling_missing_values.ipynb`](./10_pandas_handling_missing_values.ipynb) | Data Cleaning | `.isna()`, `.dropna(subset=...)`, `.fillna()`, mean/median/ffill/bfill imputation | ✅ |
| **11** | [`11_pandas_handling_duplicates.ipynb`](./11_pandas_handling_duplicates.ipynb) | Data Cleaning | `.duplicated(subset=..., keep=...)`, count duplicates, `.drop_duplicates()` | ✅ |
| **12** | [`12_pandas_sorting.ipynb`](./12_pandas_sorting.ipynb) | Data Manipulation | `.sort_values()`, multi-column mixed asc/desc, `.sort_index()`, `.nlargest()` | ✅ |
| **13** | [`13_pandas_groupby.ipynb`](./13_pandas_groupby.ipynb) | Data Analysis | Split-Apply-Combine, multi-column grouping, `.get_group()`, `.size()`, iterating groups | ✅ |
| **14** | [`14_pandas_aggregation.ipynb`](./14_pandas_aggregation.ipynb) | Data Analysis | Multi-metric `.agg()`, named aggregations, dict mapping, `.transform()` vs `.filter()` | ✅ |
| **15** | [`15_pandas_merging_and_joining.ipynb`](./15_pandas_merging_and_joining.ipynb) | Combining Data | Relational `pd.merge()`, inner/left/right/outer joins, mismatched keys, `.join()` | ✅ |
| **16** | [`16_pandas_concatenation.ipynb`](./16_pandas_concatenation.ipynb) | Combining Data | Row stacking (`axis=0`), column stacking (`axis=1`), MultiIndex keys, `ignore_index` | ✅ |
| **17** | [`17_pandas_apply_map_lambda.ipynb`](./17_pandas_apply_map_lambda.ipynb) | Advanced Ops | Series `.apply()`, row-wise `.apply(axis=1)`, anonymous lambdas, dictionary `.map()` | ✅ |
| **18** | [`18_pandas_string_operations.ipynb`](./18_pandas_string_operations.ipynb) | Other Ops | Vectorized `.str` accessor, lower/title, strip, `.contains()`, `.split(expand=True)` | ✅ |
| **19** | [`19_pandas_datetime.ipynb`](./19_pandas_datetime.ipynb) | Other Ops | `to_datetime()`, `.dt.year`/`.month`/`.day_name()`, time deltas, duration arithmetic | ✅ |
| **20** | [`20_pandas_renaming_and_replacing.ipynb`](./20_pandas_renaming_and_replacing.ipynb) | Data Cleaning | `.rename(columns=...)`, string regex standardization, replacing sentinel codes | ✅ |
| **21** | [`21_pandas_pivot_tables.ipynb`](./21_pandas_pivot_tables.ipynb) | Advanced Ops | Multidimensional `pd.pivot_table()`, row/col margins, unpivoting with `pd.melt()` | ✅ |
| **22** | [`22_pandas_crosstab.ipynb`](./22_pandas_crosstab.ipynb) | Advanced Ops | Contingency matrices, frequency cross-tabs, row/col normalized percentage tables | ✅ |
| **23** | [`23_pandas_statistical_functions.ipynb`](./23_pandas_statistical_functions.ipynb) | Data Analysis | Covariance, Pearson correlation matrix (`.corr()`), skewness, cumulative `.cumsum()` | ✅ |
| **24** | [`24_pandas_exporting_data.ipynb`](./24_pandas_exporting_data.ipynb) | Other Ops | `.to_csv()`, `.to_json()`, Excel `.to_excel()`, columnar Parquet / Feather storage | ✅ |
| **25** | [`25_pandas_optimization.ipynb`](./25_pandas_optimization.ipynb) | Other Ops | Memory profiling (`deep=True`), downcasting types, `category` dtype, `chunksize` | ✅ |
| **26** | [`26_pandas_practice.ipynb`](./26_pandas_practice.ipynb) | Practice | 10 Comprehensive multi-domain problem sets with complete code solutions | ✅ |
| **27** | [`27_pandas_mini_project.ipynb`](./27_pandas_mini_project.ipynb) | Capstone Project | **Global E-Commerce & Retail Analytics Pipeline**: Cleaning, Groupby, CLV, KPIs | ✅ |

---

## 🔍 Topic Guides & Code Demonstrations

### 1. Data Cleaning: Missing Values & Duplicates
```python
import pandas as pd
import numpy as np

# Imputing category-specific median values into missing slots
df['Salary'] = df.groupby('Department')['Salary'].transform(lambda g: g.fillna(g.median()))

# De-duplicating records based on key composite identifiers
clean_df = df.drop_duplicates(subset=['Customer_ID', 'Order_Date'], keep='last')
```

### 2. GroupBy & Named Aggregations
```python
# Modern clean Pandas aggregation syntax
kpi_summary = df.groupby(['Region', 'Category']).agg(
    Total_Revenue=('Sales', 'sum'),
    Average_Profit=('Profit', 'mean'),
    Transaction_Count=('Order_ID', 'count')
).round(2)
```

### 3. Temporal Feature Engineering (`.dt`)
```python
# Extracting ML features from datetime columns
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Quarter'] = df['Order_Date'].dt.quarter
df['Day_Name'] = df['Order_Date'].dt.day_name()
df['Is_Weekend'] = df['Order_Date'].dt.dayofweek >= 5
```

### 4. Multidimensional Reshaping: Pivot Table & Melt
```python
# Cross-tabulating Regional Category Profitability with Totals
pivot = pd.pivot_table(
    df,
    values='Profit',
    index='Category',
    columns='Region',
    aggfunc='sum',
    margins=True,
    margins_name='Grand_Total'
)
```

---

## 🛒 Capstone Project Spotlight

### 📊 Global E-Commerce & Retail Analytics Pipeline
**File:** [`27_pandas_mini_project.ipynb`](./27_pandas_mini_project.ipynb)

An end-to-end analytics workflow simulating a modern enterprise retail environment.

```
       Raw Multi-Column Transactions [250 x 10]
┌──────────┬────────────┬─────────────┬─────────┬──────────────┐
│ Order_ID │ Order_Date │ Customer_ID │ Region  │ Sales/Profit │
└──────────┴────────────┴─────────────┴─────────┴──────────────┘
                               │
                               ▼
     [Data Cleaning & Missing Value Imputation]
     Group-specific median profit filling, schema audits
                               │
                               ▼
     [Derived Feature Engineering]
     Profit Margin %, Net Revenue, Temporal month extraction
                               │
                               ▼
     [Cohort & Segment Analysis]
     Customer Lifetime Value (CLV), purchase frequencies
                               │
                               ▼
     [Multidimensional Pivot Tables & Crosstabs]
     Regional performance cross-tabulation & Grand Totals
                               │
                               ▼
     [Executive KPI Export]
     Total Revenue, Gross Profit, Margins, Top Customer Tables
```

#### Pipeline Highlights:
1. **Missing Data Imputation**: Sub-category median fill without data leakage.
2. **Feature Engineering**: Margin percentage, net revenue, and profitability classification flags.
3. **Cohort Aggregations**: Customer Lifetime Value (CLV) evaluation across order counts and total net spend.
4. **Multidimensional Summaries**: Matrix cross-tabulations and regional profitability comparisons.
5. **Executive KPI Dashboard**: Formatted summary statistics ready for executive presentation.

---

## ⚡ Performance & Optimization Tips

| Technique | Inefficient Approach | Optimized Approach | Impact |
| :--- | :--- | :--- | :--- |
| **Categorical Data** | High-cardinality `object` strings | Convert to `df['col'].astype('category')` | **60% – 85% RAM reduction** |
| **Row Iteration** | Python `for index, row in df.iterrows():` | Vectorized operations or `.itertuples()` | **100x – 500x speedup** |
| **Numeric Precision** | Default `int64` and `float64` | `pd.to_numeric(downcast='integer'/'float')` | **50% memory cut** |
| **Large Files** | `pd.read_csv('huge.csv')` into RAM | `pd.read_csv('huge.csv', chunksize=50000)` | **Zero RAM overflow crashes** |
| **Disk Storage** | Heavy text CSV (`.to_csv`) | Snappy-compressed Parquet (`.to_parquet`) | **Up to 10x faster load times** |

---

## 🚀 How to Run

### Prerequisites
- Python 3.8+ installed on your machine.

### Environment Setup
From the repository root:
```bash
# Optional: create & activate virtual environment
python -m venv venv

# Windows
.\venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# Install Pandas and Jupyter
pip install pandas numpy openpyxl pyarrow jupyter jupyterlab
```

### Launch Interactive Notebooks
```bash
# Launch standard Jupyter Notebook
jupyter notebook

# Or launch JupyterLab
jupyter lab
```
Navigate to any notebook from `01` to `27` to inspect markdown explanations and execute code cells interactively!

---

## 🔗 Related Modules

- 🐍 **[Python for AI & ML Module](../Python/)**: Foundational Python syntax, data structures, and OOP design.
- 🔢 **[NumPy Numerical Masterclass](../Numpy/)**: $N$-dimensional array manipulation, broadcasting, vectorization, and linear algebra.
- 🏠 **[Root Repository Overview](../)**: Complete curriculum roadmap, getting started guides, and upcoming ML modules.
