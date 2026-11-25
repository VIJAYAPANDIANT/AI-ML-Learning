<div align="center">

# 📈 Matplotlib for AI, Data Science & Machine Learning

### *A Production-Grade 24-Notebook Masterclass: From Foundational Geometry to Multi-Panel Dashboards & 3D Visualizations*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7%2B-11557c?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)
[![Curriculum](https://img.shields.io/badge/Curriculum-24%20Notebooks-blueviolet?style=for-the-badge&logo=gitbook&logoColor=white)](#-curriculum-index)
[![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)](#-curriculum-index)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](../#--license)

<br/>

<p align="center">
  <b>24 Interactive Notebooks</b> • <b>Object-Oriented API</b> • <b>Statistical & 3D Plotting</b> • <b>Global Analytics Capstone</b>
</p>

<p align="center">
  <a href="../"><b>🏠 Main Repository</b></a> •
  <a href="../Python/"><b>🐍 Python Module</b></a> •
  <a href="../Numpy/"><b>🔢 NumPy Module</b></a> •
  <a href="../Pandas/"><b>📊 Pandas Module</b></a> •
  <a href="#-curriculum-index"><b>📚 Curriculum Index</b></a> •
  <a href="#-capstone-project-spotlight"><b>🌍 Capstone Project</b></a> •
  <a href="#-how-to-run"><b>🚀 How to Run</b></a>
</p>

</div>

---

## 📖 Module Overview

Data visualization is the bridge between raw mathematical data and human decision-making. In machine learning, quantitative research, and exploratory data analysis (EDA), visualization enables:
- **Model Diagnostics**: Tracking training loss and validation convergence across epochs.
- **Feature Exploration**: Detecting non-linear correlations, bimodal distributions, and anomalous outliers.
- **Cluster Understanding**: Inspecting high-dimensional embeddings via 2D and 3D projections.
- **Executive Communication**: Translating statistical models into clean, publication-ready dashboards.

**Matplotlib** is the bedrock rendering engine for Python's scientific ecosystem. Libraries like **Seaborn, Pandas Plotting, Yellowbrick, and Scikit-Learn Visualizers** are built directly on top of Matplotlib's primitive Artist and Canvas architecture.

This module delivers a code-first, rigorous curriculum structured across **24 interactive Jupyter Notebooks**, guiding you from fundamental geometry and the Object-Oriented interface to complex multi-panel `GridSpec` dashboards, 3D loss surfaces, and publication-ready figure exports.

---

## 🗂️ Topic Categories & Learning Path

| Category | Primary Focus & Visualizations | Notebooks |
| :--- | :--- | :---: |
| **1. Fundamentals** | Matplotlib architecture, Figure vs Axes hierarchy, and Inset plots | `01`, `02` |
| **2. Basic Plots** | Line series, Vertical/Horizontal bars, Multivariate scatter, Histograms, and Donut charts | `03` – `08` |
| **3. Statistical Plots** | Five-number summary Box plots, IQR outlier detection, and Experimental Error Bars | `09`, `19` |
| **4. Multiple Plots** | Multi-panel Subplots, 2D Axes iteration, and Asymmetric `GridSpec` dashboards | `10` |
| **5. Plot Customization** | LaTeX titles & labels, Legend mechanics, Colormaps, Markers, Linestyles, Spines, and `rcParams` | `11` – `13`, `16` |
| **6. Advanced Plotting** | Precision Annotations, Confidence interval fills, 100% Stacked bars, and 3D Surfaces | `15`, `17`, `18`, `21` |
| **7. Other Operations** | Major/Minor Grids, Tick formatters, Dual Y-Axis (`twinx`), Temporal time series, and High-res Export | `14`, `20`, `22` |
| **8. Practice & Capstone** | 10 Algorithmic & ML problem sets and the **Global Health & Economic Development Analytics Suite** | `23`, `24` |

---

## 🗂️ Directory Architecture

```text
Matplotlib/
│
├── README.md
│
├── 01_matplotlib_introduction.ipynb             # Category 1: Fundamentals
├── 02_matplotlib_figure_and_axes.ipynb
│
├── 03_matplotlib_line_plot.ipynb                # Category 2: Basic Plots
├── 04_matplotlib_bar_chart.ipynb
├── 05_matplotlib_horizontal_bar_chart.ipynb
├── 06_matplotlib_scatter_plot.ipynb
├── 07_matplotlib_histogram.ipynb
├── 08_matplotlib_pie_chart.ipynb
│
├── 09_matplotlib_box_plot.ipynb                 # Category 3: Statistical Plots
├── 10_matplotlib_subplots.ipynb                 # Category 4: Multiple Plots
│
├── 11_matplotlib_titles_labels_and_legends.ipynb # Category 5: Plot Customization
├── 12_matplotlib_colors_and_styles.ipynb
├── 13_matplotlib_markers_and_linestyles.ipynb
│
├── 14_matplotlib_grid_and_ticks.ipynb           # Category 7: Other Operations
├── 15_matplotlib_annotations.ipynb              # Category 6: Advanced Plotting
├── 16_matplotlib_customization.ipynb            # Category 5: Plot Customization
├── 17_matplotlib_fill_and_area_plots.ipynb      # Category 6: Advanced Plotting
├── 18_matplotlib_stacked_bar_chart.ipynb
├── 19_matplotlib_error_bars.ipynb               # Category 3: Statistical Plots
├── 20_matplotlib_date_and_time_plots.ipynb      # Category 7: Other Operations
├── 21_matplotlib_3d_plots.ipynb                 # Category 6: Advanced Plotting
├── 22_matplotlib_saving_and_exporting.ipynb     # Category 7: Other Operations
│
├── 23_matplotlib_practice.ipynb                 # Category 8: Practice & Problem Sets
└── 24_matplotlib_mini_project.ipynb             # Category 8: Capstone Mini-Project
```

---

## 📚 Curriculum Index

| # | Notebook | Category | Core Concepts & APIs | Status |
| :-: | :--- | :--- | :--- | :-: |
| **01** | [`01_matplotlib_introduction.ipynb`](./01_matplotlib_introduction.ipynb) | Fundamentals | Pyplot procedural vs Object-Oriented (`fig, ax`), basic plot anatomy, rendering backends | ✅ |
| **02** | [`02_matplotlib_figure_and_axes.ipynb`](./02_matplotlib_figure_and_axes.ipynb) | Fundamentals | Canvas resolution (`figsize`, `dpi`), `add_subplot` vs `add_axes`, Inset magnification plots | ✅ |
| **03** | [`03_matplotlib_line_plot.ipynb`](./03_matplotlib_line_plot.ipynb) | Basic Plots | Continuous trends, linestyles, colors, ML training loss vs validation loss curves, log scaling | ✅ |
| **04** | [`04_matplotlib_bar_chart.ipynb`](./04_matplotlib_bar_chart.ipynb) | Basic Plots | Vertical bars, categorical metrics, `ax.bar_label()` value labels, clustered/grouped comparisons | ✅ |
| **05** | [`05_matplotlib_horizontal_bar_chart.ipynb`](./05_matplotlib_horizontal_bar_chart.ipynb) | Basic Plots | Long category labels, `ax.barh()`, `ax.invert_yaxis()`, Machine Learning Feature Importance | ✅ |
| **06** | [`06_matplotlib_scatter_plot.ipynb`](./06_matplotlib_scatter_plot.ipynb) | Basic Plots | Pairwise correlation, 4D bubble scatter (X, Y, size, color), colorbars, K-Means cluster overlays | ✅ |
| **07** | [`07_matplotlib_histogram.ipynb`](./07_matplotlib_histogram.ipynb) | Basic Plots | Continuous data distribution, binning strategies, `density=True`, Gaussian bell curve overlays | ✅ |
| **08** | [`08_matplotlib_pie_chart.ipynb`](./08_matplotlib_pie_chart.ipynb) | Basic Plots | Part-to-whole proportions, `autopct` formatting, exploded wedges, modern Donut charts | ✅ |
| **09** | [`09_matplotlib_box_plot.ipynb`](./09_matplotlib_box_plot.ipynb) | Statistical Plots | Five-number summary (Min, Q1, Median, Q3, Max), IQR outlier fliers, cross-validation model scores | ✅ |
| **10** | [`10_matplotlib_subplots.ipynb`](./10_matplotlib_subplots.ipynb) | Multiple Plots | `plt.subplots(nrows, ncols)`, 2D axes iteration with `axes.flat`, shared axes, `GridSpec` layouts | ✅ |
| **11** | [`11_matplotlib_titles_labels_and_legends.ipynb`](./11_matplotlib_titles_labels_and_legends.ipynb) | Plot Customization | LaTeX math typesetting ($R^2$, $\sigma$), typography, `loc`, `bbox_to_anchor`, external legends | ✅ |
| **12** | [`12_matplotlib_colors_and_styles.ipynb`](./12_matplotlib_colors_and_styles.ipynb) | Plot Customization | `plt.style.available`, `seaborn-v0_8`, `dark_background`, colormaps (`viridis`, `coolwarm`), correlation heatmaps | ✅ |
| **13** | [`13_matplotlib_markers_and_linestyles.ipynb`](./13_matplotlib_markers_and_linestyles.ipynb) | Plot Customization | Marker types (`o`, `s`, `^`, `D`, `*`), face/edge colors (`mfc`, `mec`), stepped lines (`steps-post`) | ✅ |
| **14** | [`14_matplotlib_grid_and_ticks.ipynb`](./14_matplotlib_grid_and_ticks.ipynb) | Other Operations | Major & minor grids, `MultipleLocator`, `PercentFormatter`, Dual-Axis charts with `ax.twinx()` | ✅ |
| **15** | [`15_matplotlib_annotations.ipynb`](./15_matplotlib_annotations.ipynb) | Advanced Plotting | Precision pointers (`ax.annotate`), arrow styles, reference thresholds (`ax.axhline`, `ax.axvspan`) | ✅ |
| **16** | [`16_matplotlib_customization.ipynb`](./16_matplotlib_customization.ipynb) | Plot Customization | Edward Tufte minimal data-ink ratio, removing spines, global configuration with `plt.rcParams` | ✅ |
| **17** | [`17_matplotlib_fill_and_area_plots.ipynb`](./17_matplotlib_fill_and_area_plots.ipynb) | Advanced Plotting | `ax.fill_between()`, 95% confidence intervals around forecasts, conditional profit/loss shading | ✅ |
| **18** | [`18_matplotlib_stacked_bar_chart.ipynb`](./18_matplotlib_stacked_bar_chart.ipynb) | Advanced Plotting | Vertical stacked bars with `bottom`, horizontal with `left`, 100% normalized proportional bars | ✅ |
| **19** | [`19_matplotlib_error_bars.ipynb`](./19_matplotlib_error_bars.ipynb) | Statistical Plots | Experimental uncertainty, symmetric vs asymmetric error bounds (`yerr`, `xerr`), cap customization | ✅ |
| **20** | [`20_matplotlib_date_and_time_plots.ipynb`](./20_matplotlib_date_and_time_plots.ipynb) | Other Operations | Time series plotting, `matplotlib.dates`, `DateFormatter`, `fig.autofmt_xdate()`, moving average crossovers | ✅ |
| **21** | [`21_matplotlib_3d_plots.ipynb`](./21_matplotlib_3d_plots.ipynb) | Advanced Plotting | `mplot3d` toolkit, 3D scatter, 3D parametric trajectories, loss surface plots with `ax.plot_surface()` | ✅ |
| **22** | [`22_matplotlib_saving_and_exporting.ipynb`](./22_matplotlib_saving_and_exporting.ipynb) | Other Operations | Production exporting (`fig.savefig`), vector (PDF/SVG) vs raster (PNG/JPG), `dpi=300`, `bbox_inches='tight'` | ✅ |
| **23** | [`23_matplotlib_practice.ipynb`](./23_matplotlib_practice.ipynb) | Practice | 10 Comprehensive multi-domain problem sets with complete code implementations | ✅ |
| **24** | [`24_matplotlib_mini_project.ipynb`](./24_matplotlib_mini_project.ipynb) | Capstone Project | **Global Economic & Public Health Analytics Dashboard**: Multi-panel Gapminder-style visualization suite | ✅ |

---

## 🔍 Key Paradigms & Code Highlights

### 1. The Standard Object-Oriented Interface
```python
import matplotlib.pyplot as plt
import numpy as np

# Production standard: Always instantiate Figure and Axes explicitly
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=100)

x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), color='#2980b9', lw=2.2, label=r'$\sin(x)$')
ax.set_title("Harmonic Oscillations", fontsize=12, fontweight='bold', pad=10)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude (V)")
ax.legend(loc='upper right', frameon=True)
ax.grid(True, linestyle='--', alpha=0.5)

plt.show()
```

### 2. Dual-Axis Modeling (`ax.twinx()`)
```python
# Primary Axis: Categorical Volume Bars
ax1.bar(months, revenue, color='#3498db', alpha=0.8, label='Revenue ($K)')
ax1.set_ylabel("Revenue ($K)", color='#3498db', fontweight='bold')

# Secondary Axis: Continuous Rate Line
ax2 = ax1.twinx()
ax2.plot(months, profit_margin_pct, color='#e74c3c', lw=2.5, marker='o', label='Margin %')
ax2.set_ylabel("Operating Margin (%)", color='#e74c3c', fontweight='bold')
```

### 3. Asymmetric Dashboard Layouts with `GridSpec`
```python
import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(12, 7))
gs = gridspec.GridSpec(nrows=2, ncols=2, height_ratios=[1.3, 1.0])

ax_top = fig.add_subplot(gs[0, :])   # Spans across entire top row
ax_bl  = fig.add_subplot(gs[1, 0])   # Bottom-left quadrant
ax_br  = fig.add_subplot(gs[1, 1])   # Bottom-right quadrant
```

---

## 🏆 Capstone Project Spotlight

### 🌍 Global Economic & Public Health Analytics Dashboard
- **Notebook:** [`24_matplotlib_mini_project.ipynb`](./24_matplotlib_mini_project.ipynb)
- **Primary Stack:** Matplotlib 3.7+, `GridSpec`, NumPy, Pandas
- **Concepts Applied:** Multidimensional bubble scatter (GDP vs Life Expectancy, log scaling), continent error-bar benchmarks, regional infant mortality boxplots, 20-year trend forecasts with $\pm 1.96 \sigma$ confidence interval shading, minimal spine styling, and publication export (`dpi=300`).
- **Dashboard Preview:**

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│               GLOBAL ECONOMIC & PUBLIC HEALTH INTELLIGENCE DASHBOARD                  │
├───────────────────────────────────────────┬────────────────────────────────────────────┤
│ 1. WEALTH VS. HEALTH (BUBBLE CHART)       │ 2. HEALTHCARE EXPENDITURE BENCHMARK        │
│ • Log-Scale GDP vs Life Expectancy        │ • Mean Spend per Region with SD Error Bars │
│ • Sized by Population, Colored by Region  │ • Value Labels on Bars                     │
├───────────────────────────────────────────┼────────────────────────────────────────────┤
│ 3. INFANT MORTALITY DISTRIBUTION          │ 4. 20-YEAR LIFE EXPECTANCY TRAJECTORY      │
│ • Continental Boxplots & Outliers         │ • Historical Mean Trend                    │
│ • Regional Variance & Skewness            │ • Shaded 95% Confidence Band               │
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

Navigate to the `Matplotlib/` directory and open any notebook to begin learning!
