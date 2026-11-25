<div align="center">

# 📊 Seaborn for AI, Data Science & Machine Learning

### *A Production-Grade 26-Notebook Masterclass: From Statistical Data Exploration to Multi-Plot Grids & Financial Risk Dashboards*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.12%2B-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Curriculum](https://img.shields.io/badge/Curriculum-26%20Notebooks-blueviolet?style=for-the-badge&logo=gitbook&logoColor=white)](#-curriculum-index)
[![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)](#-curriculum-index)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](../#--license)

<br/>

<p align="center">
  <b>26 Interactive Notebooks</b> • <b>Statistical Aggregations</b> • <b>Figure-Level & Axes-Level Grids</b> • <b>Credit Risk Capstone</b>
</p>

<p align="center">
  <a href="../"><b>🏠 Main Repository</b></a> •
  <a href="../Python/"><b>🐍 Python Module</b></a> •
  <a href="../Numpy/"><b>🔢 NumPy Module</b></a> •
  <a href="../Pandas/"><b>📊 Pandas Module</b></a> •
  <a href="../Matplotlib/"><b>📈 Matplotlib Module</b></a> •
  <a href="#-curriculum-index"><b>📚 Curriculum Index</b></a> •
  <a href="#-capstone-project-spotlight"><b>🏦 Capstone Project</b></a>
</p>

</div>

---

## 📖 Module Overview

While Matplotlib provides the low-level rendering canvas, **Seaborn** provides the statistical intelligence layer. Built directly on top of Matplotlib and integrated closely with Pandas DataFrames, Seaborn is the default choice for Exploratory Data Analysis (EDA) in data science and machine learning.

### Why Seaborn is Indispensable for AI/ML:
- **Automatic Statistical Aggregation**: Computes mean, median, standard deviations, and bootstrap confidence intervals ($\pm 95\%$ CI) on the fly without manual groupby code.
- **DataFrame-Centric Semantics**: Directly maps column names to visual aesthetics (`x`, `y`, `hue`, `size`, `style`).
- **Figure-Level vs. Axes-Level Architecture**: Seamlessly switch between single axes plots and multi-panel categorical faceting (`FacetGrid`, `PairGrid`, `JointGrid`).
- **Statistical Model Fitting**: Built-in linear, polynomial, and logistic regression trendlines with shaded uncertainty bounds.

This module delivers a complete **26-Notebook Masterclass** covering foundational dataset manipulation, relational scatter and line series, categorical distributions, probability densities, masked correlation heatmaps, pairwise matrices, and custom publication themes.

---

## 🗂️ Topic Categories & Learning Path

| Category | Primary Focus & Visualizations | Notebooks |
| :--- | :--- | :---: |
| **1. Fundamentals & Datasets** | Seaborn architecture, Figure-level vs Axes-level API, and Built-in benchmark datasets | `01` – `03` |
| **2. Relational Plots** | Figure-level `relplot`, Multivariate Scatter with semantic encodings, and Aggregated Line plots with confidence bands | `04` – `06` |
| **3. Categorical Plots** | Figure-level `catplot`, Statistical Bar charts, Frequency Counts, Box plots, Split Violins, and Swarm overlays | `07` – `12` |
| **4. Distribution Plots** | Figure-level `displot`, Histograms with KDE density curves, 2D Bivariate contours, and Empirical CDFs | `13` – `15` |
| **5. Regression & Multivariable** | Linear, Polynomial & Logistic regression (`lmplot`/`regplot`), Correlation Heatmaps, Pairwise scatter (`pairplot`), and Joint plots | `16` – `19` |
| **6. Multi-Plot Grids & Styling** | Custom mapping with `FacetGrid` & `PairGrid`, Theme presets (`darkgrid`/`ticks`), Despining, Color Palettes, and Matplotlib integration | `20` – `24` |
| **7. Practice & Capstone** | 10 Algorithmic & ML problem sets and the **Financial Credit Risk & Default Analytics Suite** | `25`, `26` |

---

## 🗂️ Directory Architecture

```text
Seaborn/
│
├── README.md
│
├── 01_seaborn_introduction.ipynb                # Category 1: Fundamentals & Datasets
├── 02_seaborn_installation_and_setup.ipynb
├── 03_seaborn_datasets.ipynb
│
├── 04_seaborn_relational_plots.ipynb            # Category 2: Relational Plots
├── 05_seaborn_scatter_plot.ipynb
├── 06_seaborn_line_plot.ipynb
│
├── 07_seaborn_categorical_plots.ipynb           # Category 3: Categorical Plots
├── 08_seaborn_bar_plot.ipynb
├── 09_seaborn_count_plot.ipynb
├── 10_seaborn_box_plot.ipynb
├── 11_seaborn_violin_plot.ipynb
├── 12_seaborn_strip_and_swarm_plot.ipynb
│
├── 13_seaborn_distribution_plots.ipynb          # Category 4: Distribution Plots
├── 14_seaborn_histogram_and_kde.ipynb
├── 15_seaborn_ecdf_plot.ipynb
│
├── 16_seaborn_regression_plots.ipynb            # Category 5: Regression & Multivariable
├── 17_seaborn_heatmap.ipynb
├── 18_seaborn_pairplot.ipynb
├── 19_seaborn_jointplot.ipynb
│
├── 20_seaborn_facetgrid.ipynb                   # Category 6: Multi-Plot Grids & Styling
├── 21_seaborn_pairgrid.ipynb
├── 22_seaborn_themes_and_styles.ipynb
├── 23_seaborn_color_palettes.ipynb
├── 24_seaborn_figure_customization.ipynb
│
├── 25_seaborn_practice.ipynb                    # Category 7: Practice & Problem Sets
└── 26_seaborn_mini_project.ipynb                # Category 7: Capstone Mini-Project
```

---

## 📚 Curriculum Index

| # | Notebook | Category | Core Concepts & APIs | Status |
| :-: | :--- | :--- | :--- | :-: |
| **01** | [`01_seaborn_introduction.ipynb`](./01_seaborn_introduction.ipynb) | Fundamentals | Why Seaborn for AI/ML, DataFrame integration, Matplotlib comparison, first multi-dimensional scatter | ✅ |
| **02** | [`02_seaborn_installation_and_setup.ipynb`](./02_seaborn_installation_and_setup.ipynb) | Fundamentals | Axes-level vs. Figure-level functions, embedding with `ax=ax`, `FacetGrid` returns, global themes | ✅ |
| **03** | [`03_seaborn_datasets.ipynb`](./03_seaborn_datasets.ipynb) | Fundamentals | Built-in datasets (`tips`, `iris`, `titanic`, `diamonds`, `penguins`), Tidy wide-form to long-form reshaping | ✅ |
| **04** | [`04_seaborn_relational_plots.ipynb`](./04_seaborn_relational_plots.ipynb) | Relational Plots | `sns.relplot()`, `kind='scatter'` vs `kind='line'`, multi-panel faceting with `col`, `row`, `col_wrap` | ✅ |
| **05** | [`05_seaborn_scatter_plot.ipynb`](./05_seaborn_scatter_plot.ipynb) | Relational Plots | `sns.scatterplot()`, multidimensional mapping: `hue`, `size`, `sizes=(min, max)`, `style`, alpha transparency | ✅ |
| **06** | [`06_seaborn_line_plot.ipynb`](./06_seaborn_line_plot.ipynb) | Relational Plots | `sns.lineplot()`, time series, automatic aggregation, 95% bootstrap confidence bands (`errorbar='ci'`), `markers` | ✅ |
| **07** | [`07_seaborn_categorical_plots.ipynb`](./07_seaborn_categorical_plots.ipynb) | Categorical Plots | `sns.catplot()`, categorical scatter, distribution and estimate plot families, column faceting | ✅ |
| **08** | [`08_seaborn_bar_plot.ipynb`](./08_seaborn_bar_plot.ipynb) | Categorical Plots | `sns.barplot()`, point estimates with confidence intervals, custom aggregators (`estimator=np.median`), `hue` | ✅ |
| **09** | [`09_seaborn_count_plot.ipynb`](./09_seaborn_count_plot.ipynb) | Categorical Plots | `sns.countplot()`, frequency counts for discrete categories, ordering categories, horizontal bars | ✅ |
| **10** | [`10_seaborn_box_plot.ipynb`](./10_seaborn_box_plot.ipynb) | Categorical Plots | `sns.boxplot()`, statistical quartiles, IQR outlier detection, nested subgroup comparisons with `hue` | ✅ |
| **11** | [`11_seaborn_violin_plot.ipynb`](./11_seaborn_violin_plot.ipynb) | Categorical Plots | `sns.violinplot()`, combining box plot with KDE density estimation, `split=True` for binary cohorts, `inner='quartile'` | ✅ |
| **12** | [`12_seaborn_strip_and_swarm_plot.ipynb`](./12_seaborn_strip_and_swarm_plot.ipynb) | Categorical Plots | `sns.stripplot()`, jitter, `sns.swarmplot()`, non-overlapping points, hybrid layering over box plots | ✅ |
| **13** | [`13_seaborn_distribution_plots.ipynb`](./13_seaborn_distribution_plots.ipynb) | Distribution Plots | `sns.displot()`, univariate & bivariate distributions, toggling `kind='hist'`, `'kde'`, `'ecdf'` with faceting | ✅ |
| **14** | [`14_seaborn_histogram_and_kde.ipynb`](./14_seaborn_histogram_and_kde.ipynb) | Distribution Plots | `sns.histplot()`, `kde=True`, `stat='density'`, `multiple='dodge'`, 2D Bivariate density contours (`sns.kdeplot`) | ✅ |
| **15** | [`15_seaborn_ecdf_plot.ipynb`](./15_seaborn_ecdf_plot.ipynb) | Distribution Plots | `sns.ecdfplot()`, Empirical Cumulative Distribution Functions, percentile cutoffs, comparing cohort CDFs | ✅ |
| **16** | [`16_seaborn_regression_plots.ipynb`](./16_seaborn_regression_plots.ipynb) | Regression & Multi | `sns.regplot()` vs `sns.lmplot()`, linear & 2nd-order polynomial fits, logistic regression (`logistic=True`) | ✅ |
| **17** | [`17_seaborn_heatmap.ipynb`](./17_seaborn_heatmap.ipynb) | Regression & Multi | `sns.heatmap()`, Pearson correlation matrices, `annot=True`, `mask` upper triangle with `np.triu`, `clustermap` | ✅ |
| **18** | [`18_seaborn_pairplot.ipynb`](./18_seaborn_pairplot.ipynb) | Regression & Multi | `sns.pairplot()`, pairwise relationship scatter matrices across all numerical features, `corner=True`, `hue` | ✅ |
| **19** | [`19_seaborn_jointplot.ipynb`](./19_seaborn_jointplot.ipynb) | Regression & Multi | `sns.jointplot()`, bivariate relationship with marginal univariate distributions, `kind='scatter'`, `'hex'`, `'reg'` | ✅ |
| **20** | [`20_seaborn_facetgrid.ipynb`](./20_seaborn_facetgrid.ipynb) | Multi-Plot Grids | `sns.FacetGrid`, mapping arbitrary functions with `.map()` and `.map_dataframe()`, custom titles & labels | ✅ |
| **21** | [`21_seaborn_pairgrid.ipynb`](./21_seaborn_pairgrid.ipynb) | Multi-Plot Grids | `sns.PairGrid`, granular mapping: `.map_diag()` for KDE, `.map_upper()` for scatter, `.map_lower()` for contours | ✅ |
| **22** | [`22_seaborn_themes_and_styles.ipynb`](./22_seaborn_themes_and_styles.ipynb) | Multi-Plot Grids | 5 Styles (`darkgrid`, `whitegrid`, `ticks`), scaling with `set_context()`, `sns.despine()` border removal | ✅ |
| **23** | [`23_seaborn_color_palettes.ipynb`](./23_seaborn_color_palettes.ipynb) | Multi-Plot Grids | Qualitative (`deep`, `Set2`), Sequential (`Blues`, `rocket`), Diverging (`vlag`, `coolwarm`), `palplot` | ✅ |
| **24** | [`24_seaborn_figure_customization.ipynb`](./24_seaborn_figure_customization.ipynb) | Multi-Plot Grids | Interfacing Seaborn with Matplotlib `Axes` & `Figure`, custom titles, legends, and export (`dpi=300`) | ✅ |
| **25** | [`25_seaborn_practice.ipynb`](./25_seaborn_practice.ipynb) | Practice | 10 Comprehensive multi-domain statistical EDA and Machine Learning visualization problem sets | ✅ |
| **26** | [`26_seaborn_mini_project.ipynb`](./26_seaborn_mini_project.ipynb) | Capstone Project | **Financial Risk & Credit Default Analytics Suite**: Multi-panel exploratory data analysis and modeling | ✅ |

---

## 🔍 Key Paradigms & Code Highlights

### 1. The Power of `hue`, `size`, and `style`
```python
import seaborn as sns
import matplotlib.pyplot as plt

# A 4-dimensional visualization in a single line of code
sns.scatterplot(
    data=df,
    x='Annual_Income',
    y='Spending_Score',
    hue='Customer_Segment', # 3rd dimension (Color)
    size='Account_Age',     # 4th dimension (Bubble Size)
    palette='Set2',
    alpha=0.8
)
plt.show()
```

### 2. Masked Lower-Triangle Correlation Matrix
```python
import numpy as np

corr = df.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))

sns.heatmap(
    corr, 
    mask=mask, 
    annot=True, 
    fmt='.2f', 
    cmap='vlag', 
    center=0, 
    square=True, 
    linewidths=1
)
plt.show()
```

### 3. Logistic Regression Probability Estimation
```python
# Directly fits a sigmoid logistic curve to binary classification target
sns.regplot(
    data=df, 
    x='FICO_Score', 
    y='Loan_Defaulted', 
    logistic=True, 
    y_jitter=0.03, 
    color='#c0392b'
)
plt.show()
```

---

## 🏆 Capstone Project Spotlight

### 🏦 Financial Risk & Customer Credit Default Analytics Suite
- **Notebook:** [`26_seaborn_mini_project.ipynb`](./26_seaborn_mini_project.ipynb)
- **Primary Stack:** Seaborn 0.12+, Matplotlib, Pandas, NumPy
- **Concepts Applied:** DTI vs. Loan Amount multivariate scatter, empirical default rate bar charts with 95% bootstrap confidence bounds, FICO score box plots across loan purposes, masked correlation heatmap, and logistic regression default probability modeling.
- **Dashboard Preview:**

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│               FINANCIAL CREDIT RISK & DEFAULT ANALYTICS DASHBOARD                      │
├───────────────────────────────────────────┬────────────────────────────────────────────┤
│ 1. DTI VS LOAN PRINCIPAL (SCATTER)        │ 2. EMPIRICAL DEFAULT PROBABILITY (BAR)     │
│ • Color-Coded by Default Status (0 vs 1)  │ • Credit Risk Grades (A Prime to E Sub)    │
│ • Risk Boundaries & Debt Ratios           │ • 95% Bootstrap Confidence Intervals       │
├───────────────────────────────────────────┼────────────────────────────────────────────┤
│ 3. FICO SCORE BY LOAN PURPOSE (BOXPLOT)   │ 4. MULTIVARIABLE CORRELATION HEATMAP       │
│ • Interquartile Ranges across Borrowers   │ • Lower Triangle Mask with Diverging Colormap │
│ • Outlier Flier Identification            │ • FICO, Income, DTI, Default Correlations  │
└───────────────────────────────────────────┴────────────────────────────────────────────┘
```

---

## 🚀 How to Run the Notebooks

### 1. Activate Environment
Ensure you have installed the repository dependencies:
```bash
# If using virtual environment
source venv/bin/activate  # macOS/Linux
.\venv\Scripts\Activate.ps1 # Windows PowerShell

# Install dependencies if not already installed
pip install -r ../requirements.txt
```

### 2. Launch JupyterLab or Notebook
```bash
# Launch from the repository root
jupyter lab
```

Navigate to the `Seaborn/` directory and open any notebook to begin learning!
