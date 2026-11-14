<div align="center">

# 🤖 Artificial Intelligence & Machine Learning Learning Path

### *A Structured, Hands-On Curriculum from Python Foundations to Advanced AI/ML Architectures*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.20%2B-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Active_Development-success?style=for-the-badge)](#-roadmap--progress)
[![Notebooks](https://img.shields.io/badge/Notebooks-74%20Completed-blueviolet?style=for-the-badge&logo=gitbook&logoColor=white)](#-curriculum-breakdown)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](#-license)

<br/>

<p align="center">
  <b>74+ Interactive Notebooks</b> • <b>Zero-to-Hero Curriculum</b> • <b>Real-World Capstone Projects</b> • <b>Vectorized Computing & Wrangling</b>
</p>

<p align="center">
  <a href="./Python/"><b>🐍 Python (27 Notebooks)</b></a> •
  <a href="./Numpy/"><b>🔢 NumPy (20 Notebooks)</b></a> •
  <a href="./Pandas/"><b>📊 Pandas (27 Notebooks)</b></a> •
  <a href="#-getting-started"><b>💻 Getting Started</b></a> •
  <a href="#-roadmap--progress"><b>🎯 Roadmap</b></a>
</p>

</div>

---

## 📖 Overview

Welcome to the **AI-ML-Learning** repository! This project serves as an end-to-end, code-first educational guide engineered to take developers and data practitioners from core programming fundamentals to advanced machine learning and deep learning pipelines.

Each module is packed with **interactive Jupyter Notebooks**, clean code snippets, theory summaries, edge-case demonstrations, practical exercises, and end-to-end mini-projects that simulate real-world industry tasks.

---

## 🌟 Key Highlights

- 🧩 **Zero-to-Hero Structured Progression**: Designed step-by-step from core syntax to high-performance scientific computation, tabular data wrangling, and modeling.
- ⚡ **Vectorization & Memory Optimization**: Strong emphasis on avoiding slow Python loops by leveraging NumPy's C-accelerated universal functions (`ufuncs`), multi-axis broadcasting, memory layout (`copy` vs. `view`), and Pandas categorical downcasting.
- 🔬 **Applied Mathematics & Linear Algebra**: Hands-on matrix math, transposes, determinants, matrix inverses, and eigenvalue decompositions powering modern ML algorithms.
- 📊 **Production-Grade Data Wrangling**: Complete mastery of Pandas DataFrames, multi-source merging, groupby aggregations, pivot tables, temporal features, and missing value treatment.
- 💼 **Industry-Ready Capstone Projects**: Realistic mini-projects covering analytical system design, real estate exploratory data analysis (EDA), and global e-commerce retail pipelines.
- 📝 **Fully Documented & Reproducible**: Clean, self-contained notebooks with clear markdown explanations, execution outputs, and clean project hierarchies.

---

## 🗂️ Repository Architecture

```text
AI-ML-Learning/
│
├── 🐍 Python/                          # [COMPLETED] 27 Notebooks: Foundations, OOP & Analytics
│   ├── 01-06 Fundamentals             # Syntax, Types, I/O, Operators, Control Flow, Loops
│   ├── 07-14 Data Structures & Logic   # Strings, Lists, Tuples, Sets, Dictionaries, Functions, Comprehensions
│   ├── 15-20 Systems & Advanced OOP    # Modules, File I/O, Exceptions, OOP 4 Pillars, Iterators, Decorators
│   ├── 21-25 Standard Lib & Bridges    # Datetime, Regex, JSON, NumPy intro, Pandas intro
│   ├── 26_python_practice.ipynb        # 10 Multi-domain algorithmic problem sets
│   ├── 27_python_mini_project.ipynb     # Capstone: Student Performance & Analytics System
│   └── README.md                       # Complete Python module guide & index
│
├── 🔢 Numpy/                           # [COMPLETED] 20 Notebooks: Numerical Computing & Linear Algebra
│   ├── 01-05 Array Fundamentals        # Ndarray creation, Dtypes, Multidimensional indexing, Reshape, Slicing
│   ├── 06-10 Vectorization & Filtering # Vectorized arithmetic, Broadcasting, Ufuncs, Aggregations, Masking
│   ├── 11-13 Randomness & Attributes   # RNG sampling, Persistent binary storage (.npy/.npz), Memory layout
│   ├── 14-18 Matrix Operations         # Stacking, Splitting, Sorting, Copy vs View, Linear Algebra (np.linalg)
│   ├── 19_numpy_practice.ipynb         # Vectorized array manipulation & standardization exercises
│   ├── 20_numpy_mini_project.ipynb     # Capstone: Real Estate Valuation & EDA Pipeline
│   └── README.md                       # Exhaustive 20-notebook NumPy masterclass guide
│
├── 📊 Pandas/                          # [COMPLETED] 27 Notebooks: Data Wrangling, Time-Series & Analytics
│   ├── 01-03 Fundamentals             # Intro, 1D Series, 2D DataFrame architecture
│   ├── 04-07 Data Handling            # File ingestion, inspection, selection, .loc/.iloc slicing
│   ├── 08-12 Cleaning & Manipulation  # Boolean filters, derived columns, missing values, duplicates, sorting
│   ├── 13-16 GroupBy & Combining      # Split-Apply-Combine, multi-metric agg, relational merge, concat
│   ├── 17-25 Advanced & Other Ops     # Apply/map, strings, datetime, pivot tables, crosstabs, optimization
│   ├── 26_pandas_practice.ipynb       # 10 Multi-domain data engineering problem sets
│   ├── 27_pandas_mini_project.ipynb    # Capstone: Global E-Commerce & Retail Analytics Pipeline
│   └── README.md                      # Complete 27-notebook Pandas module guide
│
├── 📉 Data-Visualization/               # [UPCOMING] Exploratory Analysis with Matplotlib, Seaborn & Plotly
├── ⚙️ Machine-Learning/                 # [UPCOMING] Supervised & Unsupervised Learning with Scikit-Learn
└── 🧠 Deep-Learning/                    # [UPCOMING] Neural Networks, PyTorch, TensorFlow & Transformers
```

---

## 📚 Curriculum Breakdown

### 1. 🐍 [Python for AI & ML](./Python/) (27 Notebooks)
A complete grounding in modern Python (3.8+) engineered specifically for data science and AI workflows.

| Phase | Notebooks | Key Topics Covered |
| :--- | :---: | :--- |
| **Language Foundations** | `01` – `06` | Syntax rules, Dynamic typing, Type casting, Formatted f-strings, Operators, Control flow (`if-elif-else`, `match-case`), Loops (`range`, `enumerate`, `zip`) |
| **Data Structures** | `07` – `11` | String immutability & methods, Lists (mutations, shallow vs. deep copy), Tuples (`namedtuple`), Set operations, Dictionaries (`Counter`, `defaultdict`) |
| **Functional Programming** | `12` – `14` | Variadic parameters (`*args`, `**kwargs`), Scope (LEGB rule), First-class lambdas, `map()`, `filter()`, Matrix flattening with comprehensions |
| **Advanced & OOP** | `15` – `20` | Modular packages, Context managers (`with`), Custom exceptions, 4 OOP Pillars (Encapsulation, Abstraction, Inheritance, Polymorphism), Generators (`yield`), Decorators |
| **Utilities & Data Bridges** | `21` – `25` | `datetime` parsing, Regular expressions, JSON serialization, Hands-on bridge to NumPy ndarrays & Pandas DataFrames |
| **Capstone & Practice** | `26` – `27` | Comprehensive algorithmic problem sets and the **Student Performance & Analytics System** |

👉 **[View Full Python Module Documentation & Notebooks](./Python/README.md)**

---

### 2. 🔢 [NumPy Numerical Masterclass](./Numpy/) (20 Notebooks)
A rigorous masterclass in $N$-dimensional array computing, vectorized operations, and numerical linear algebra.

| Phase | Notebooks | Key Topics Covered |
| :--- | :---: | :--- |
| **Foundations & Indexing** | `01` – `05` | C-level memory efficiency, homogeneous dtypes, shape manipulation, auto-dimension inference (`-1`), multi-axis slicing |
| **Vectorization & Logic** | `06` – `10` | Eliminating Python loops with ufuncs, multi-axis broadcasting, statistical aggregations (`axis=0/1`), Boolean mask filters, `np.where` |
| **Operations & Storage** | `11` – `13` | Reproducible RNG distributions, binary disk I/O (`.npy`, `.npz`), memory footprint inspection (`nbytes`, `itemsize`) |
| **Matrix Algebra** | `14` – `18` | Array stacking & splitting, `argsort`, memory mutation (`copy` vs. `view`), matrix products (`@`), matrix inverse & eigenvalue decomposition |
| **Applied Projects** | `19` – `20` | Feature standardization (Z-score, Min-Max), Outlier filtering, and the **Real Estate EDA Mini-Project** |

👉 **[View Full NumPy Masterclass Documentation & Notebooks](./Numpy/README.md)**

---

### 3. 📊 [Pandas Data Wrangling & Analytics](./Pandas/) (27 Notebooks)
A production-grade masterclass in tabular data cleaning, manipulation, time-series extraction, and relational operations.

| Category | Notebooks | Key Topics Covered |
| :--- | :---: | :--- |
| **Fundamentals** | `01` – `03` | Series (1D), DataFrames (2D), construction methods, metadata inspection (`.dtypes`, `.shape`, `.index`) |
| **Data Handling** | `04` – `07` | Reading CSV/JSON/Excel, structural inspection (`.info()`, `.describe()`), label/integer slicing (`.loc[]` vs. `.iloc[]`) |
| **Data Cleaning** | `10`, `11`, `20` | Missing value treatment (`.isna()`, `.fillna()`, `.dropna()`), duplicate identification, header standardization |
| **Data Manipulation** | `08`, `09`, `12` | Multi-condition boolean masking, `.isin()`, `.query()`, derived column assignment, multi-key sorting (`.sort_values()`) |
| **Data Analysis** | `13`, `14`, `23` | Split-Apply-Combine groupby, named aggregations, `.transform()`, correlation matrices, descriptive statistics |
| **Combining Data** | `15` – `16` | Relational merges (inner, left, right, outer), join keys, multi-axis concatenation (`pd.concat`) |
| **Advanced Operations** | `17`, `21`, `22` | Custom `.apply()` with lambdas, multidimensional pivot tables, frequency cross-tabulation (`pd.crosstab`) |
| **Other Operations** | `18`, `19`, `24`, `25` | Vectorized text methods (`.str`), temporal dates (`.dt`), storage persistence (CSV/Parquet), memory optimization |
| **Practice & Capstone** | `26` – `27` | 10 Data engineering problem sets and the **Global E-Commerce & Retail Analytics Pipeline** |

👉 **[View Full Pandas Module Documentation & Notebooks](./Pandas/README.md)**

---

## 🏆 Featured Capstone Mini-Projects

<table>
  <tr>
    <td width="33%" valign="top">
      <h3>🎓 Student Analytics</h3>
      <p><b>Notebook:</b> <code><a href="./Python/27_python_mini_project.ipynb">Python/27_python_mini_project.ipynb</a></code></p>
      <p>Object-oriented system to process student academic records, evaluate GPAs, compute percentiles, and format automated JSON reports.</p>
      <ul>
        <li><b>Concepts:</b> Custom OOP Classes, File I/O, Error Handling, Aggregation</li>
      </ul>
    </td>
    <td width="33%" valign="top">
      <h3>🏠 Real Estate Valuation</h3>
      <p><b>Notebook:</b> <code><a href="./Numpy/20_numpy_mini_project.ipynb">Numpy/20_numpy_mini_project.ipynb</a></code></p>
      <p>Vectorized exploratory data analysis evaluating housing datasets <code>[SqFt, Beds, Baths, Price]</code> entirely through pure NumPy arrays.</p>
      <ul>
        <li><b>Concepts:</b> Multi-axis stats, Price/SqFt, Outlier masks, Min-Max scaling</li>
      </ul>
    </td>
    <td width="33%" valign="top">
      <h3>🛒 E-Commerce Pipeline</h3>
      <p><b>Notebook:</b> <code><a href="./Pandas/27_pandas_mini_project.ipynb">Pandas/27_pandas_mini_project.ipynb</a></code></p>
      <p>End-to-end retail pipeline performing missing value imputation, margin calculations, multi-level GroupBy KPIs, pivot tables, and CLV analysis.</p>
      <ul>
        <li><b>Concepts:</b> Data Cleaning, Imputation, Pivot Tables, CLV Metrics</li>
      </ul>
    </td>
  </tr>
</table>

---

## 💻 Getting Started

### 1. Prerequisites
- **Python 3.8+** installed ([python.org](https://www.python.org/downloads/))
- **Git** installed ([git-scm.com](https://git-scm.com/))

### 2. Clone the Repository
```bash
git clone https://github.com/VIJAYAPANDIANT/AI-ML-Learning.git
cd AI-ML-Learning
```

### 3. Create & Activate a Virtual Environment

#### Windows (PowerShell / Command Prompt)
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment (PowerShell)
.\venv\Scripts\Activate.ps1

# Activate virtual environment (Command Prompt)
.\venv\Scripts\activate.bat
```

#### macOS / Linux
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install --upgrade pip
pip install numpy pandas matplotlib seaborn scikit-learn jupyter jupyterlab pyarrow openpyxl
```

### 5. Launch the Notebooks
```bash
# Launch via standard Jupyter Notebook
jupyter notebook

# Or launch via modern JupyterLab
jupyter lab
```

---

## 🎯 Roadmap & Progress

| Module | Core Topics | Notebooks | Status |
| :--- | :--- | :---: | :---: |
| **01. Setup & Git Workflow** | Git, Virtual Environments, Jupyter Setup | — | `Completed` ✅ |
| **02. Python Foundations** | Core Syntax, Data Structures, OOP, Advanced Python, Capstone | 27 | `Completed` ✅ |
| **03. Numerical Computing** | NumPy Arrays, Vectorization, Broadcasting, Linear Algebra, Capstone | 20 | `Completed` ✅ |
| **04. Data Manipulation** | Pandas Series, DataFrames, Data Cleaning, Merging & Analytics, Capstone | 27 | `Completed` ✅ |
| **05. Data Visualization** | Matplotlib, Seaborn, Interactive Visualizations | — | `In Progress` 🔄 |
| **06. Exploratory Data Analysis** | Statistical EDA, Feature Relationships, Preprocessing | — | `Planned` ⏳ |
| **07. Classical Machine Learning** | Supervised & Unsupervised Learning, Scikit-Learn, Evaluation | — | `Planned` ⏳ |
| **08. Deep Learning Foundations** | PyTorch, Neural Network Architectures, Computer Vision & NLP | — | `Planned` ⏳ |

---

## 🛠️ Tech Stack & Ecosystem

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" height="28" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter" height="28" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" alt="NumPy" height="28" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas" height="28" />
  <img src="https://img.shields.io/badge/Matplotlib-11557c?style=flat-square" alt="Matplotlib" height="28" />
  <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" alt="Scikit-Learn" height="28" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch" height="28" />
  <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git" height="28" />
</p>

---

## 🤝 Contributing

Contributions, issues, and feature suggestions are welcome! If you would like to contribute:

1. **Fork** the repository
2. Create your branch: `git checkout -b feature/topic-enhancement`
3. Commit your changes: `git commit -m 'feat: add enhanced topic notes'`
4. Push to the branch: `git push origin feature/topic-enhancement`
5. Open a **Pull Request**

---

## 👤 Author & Connect

**Vijaya Pandian T**
- **GitHub:** [@VIJAYAPANDIANT](https://github.com/VIJAYAPANDIANT)
- **Repository:** [AI-ML-Learning](https://github.com/VIJAYAPANDIANT/AI-ML-Learning)

---

## 📜 License

This repository is maintained for educational and self-learning purposes under the **MIT License**. Feel free to explore, clone, and build upon the code!
