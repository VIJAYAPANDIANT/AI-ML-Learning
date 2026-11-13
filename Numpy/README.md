<div align="center">

# 🔢 NumPy for AI & Machine Learning

### *A Rigorous 20-Notebook Masterclass: From Ndarray Fundamentals to Linear Algebra & Exploratory Data Analysis*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.20%2B-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Curriculum](https://img.shields.io/badge/Curriculum-20%20Notebooks-blueviolet?style=for-the-badge&logo=gitbook&logoColor=white)](#-curriculum-index)
[![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)](#-curriculum-index)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](../#--license)

<br/>

<p align="center">
  <b>20 Interactive Notebooks</b> • <b>Vectorized Computing</b> • <b>Linear Algebra (np.linalg)</b> • <b>Real Estate EDA Capstone</b>
</p>

<p align="center">
  <a href="../"><b>🏠 Main Repository</b></a> •
  <a href="../Python/"><b>🐍 Python Module</b></a> •
  <a href="#-curriculum-index"><b>📚 Curriculum Index</b></a> •
  <a href="#-phase-by-phase-guide"><b>🔍 Phase-by-Phase Guide</b></a> •
  <a href="#-capstone-project-spotlight"><b>🏠 Capstone Project</b></a> •
  <a href="#-performance-benchmark"><b>⚡ Performance</b></a> •
  <a href="#-how-to-run"><b>🚀 How to Run</b></a>
</p>

</div>

---

## 📖 Module Overview

NumPy (Numerical Python) is the fundamental package for scientific computing in Python. It provides the high-performance $N$-dimensional array (`ndarray`) object, sophisticated broadcasting functions, linear algebra solvers, random number generators, and C-accelerated numeric operations.

Almost all modern machine learning and deep learning frameworks — including **Pandas, Scikit-Learn, PyTorch, TensorFlow, and JAX** — are either built directly on top of NumPy or share its memory layout principles.

### Key Learning Objectives:
- **Think in Vectors**: Replace slow Python `for` loops with vectorized ufuncs running at near C/Fortran speeds.
- **Understand Memory Dynamics**: Learn contiguous buffer allocations, strides, and the critical distinction between array **Views** and **Copies**.
- **Master Broadcasting**: Perform operations on tensors of dissimilar but compatible dimensions without allocating redundant memory.
- **Execute Linear Algebra**: Calculate dot products, matrix multiplications, determinants, matrix inversions, and eigenvalue decompositions powering machine learning algorithms.

---

## 🗂️ Module Architecture

```text
Numpy/
├── 01_numpy_introduction.ipynb              # Phase 1: Foundations & Indexing
├── 02_numpy_data_types.ipynb
├── 03_numpy_multidimensional_arrays.ipynb
├── 04_numpy_reshape.ipynb
├── 05_numpy_slicing.ipynb
│
├── 06_numpy_arithmetic.ipynb                # Phase 2: Vectorization & Logic
├── 07_numpy_broadcasting.ipynb
├── 08_numpy_useful_functions.ipynb
├── 09_numpy_aggregate_functions.ipynb
├── 10_numpy_filtering.ipynb
│
├── 11_numpy_random_numbers.ipynb            # Phase 3: Operations, Storage & Attributes
├── 12_numpy_saving_loading.ipynb
├── 13_numpy_array_attributes.ipynb
│
├── 14_numpy_joining_arrays.ipynb            # Phase 4: Matrix Operations & Linear Algebra
├── 15_numpy_splitting_arrays.ipynb
├── 16_numpy_sorting_searching.ipynb
├── 17_numpy_copy_vs_view.ipynb
├── 18_numpy_linear_algebra.ipynb
│
├── 19_numpy_practice.ipynb                  # Phase 5: Applied Practice & Capstone EDA
├── 20_numpy_mini_project.ipynb
└── README.md
```

---

## 📚 Curriculum Index

| # | Notebook | Primary Topic | Core Concepts & APIs | Status |
| :-: | :--- | :--- | :--- | :-: |
| **01** | [`01_numpy_introduction.ipynb`](./01_numpy_introduction.ipynb) | NumPy Introduction | `np.array()`, memory compactness, vectorization speed vs. native lists | ✅ |
| **02** | [`02_numpy_data_types.ipynb`](./02_numpy_data_types.ipynb) | Data Types (`dtype`) | Homogeneous types, `int32`/`float64`/`bool_`, type casting via `.astype()` | ✅ |
| **03** | [`03_numpy_multidimensional_arrays.ipynb`](./03_numpy_multidimensional_arrays.ipynb) | Multi-Dimensional Arrays | Scalars (0D), Vectors (1D), Matrices (2D), Tensors (3D+), multi-axis indexing | ✅ |
| **04** | [`04_numpy_reshape.ipynb`](./04_numpy_reshape.ipynb) | Reshaping & Flattening | `.reshape()`, `-1` dimension inference, `.ravel()` (view) vs. `.flatten()` (copy) | ✅ |
| **05** | [`05_numpy_slicing.ipynb`](./05_numpy_slicing.ipynb) | Multi-Axis Slicing | `[start:stop:step]` on multi-dimensions, stride stepping, array reversing | ✅ |
| **06** | [`06_numpy_arithmetic.ipynb`](./06_numpy_arithmetic.ipynb) | Vectorized Arithmetic | Universal functions (`ufuncs`), element-wise arithmetic, powers, trigonometry | ✅ |
| **07** | [`07_numpy_broadcasting.ipynb`](./07_numpy_broadcasting.ipynb) | Array Broadcasting | Broadcasting rules, trailing dimensions, feature mean-centering | ✅ |
| **08** | [`08_numpy_useful_functions.ipynb`](./08_numpy_useful_functions.ipynb) | Array Initialization | `np.zeros()`, `np.ones()`, `np.full()`, `np.eye()`, `np.arange()`, `np.linspace()` | ✅ |
| **09** | [`09_numpy_aggregate_functions.ipynb`](./09_numpy_aggregate_functions.ipynb) | Aggregate Statistics | `np.sum()`, `np.mean()`, `np.std()`, `np.median()`, `axis=0` vs `axis=1`, `argmax` | ✅ |
| **10** | [`10_numpy_filtering.ipynb`](./10_numpy_filtering.ipynb) | Boolean Masking | Boolean indexing, bitwise operators (`&`, `\|`, `~`), conditional `np.where()` | ✅ |
| **11** | [`11_numpy_random_numbers.ipynb`](./11_numpy_random_numbers.ipynb) | Random Sampling (RNG) | Seed reproducibility, uniform, standard normal (`randn`), `randint`, `shuffle` | ✅ |
| **12** | [`12_numpy_saving_loading.ipynb`](./12_numpy_saving_loading.ipynb) | Persistent Array I/O | Binary disk storage (`.npy`, compressed `.npz`), CSV text `savetxt`/`loadtxt` | ✅ |
| **13** | [`13_numpy_array_attributes.ipynb`](./13_numpy_array_attributes.ipynb) | Memory Attributes | `.ndim`, `.shape`, `.size`, `.dtype`, `.itemsize`, `.nbytes` memory footprint | ✅ |
| **14** | [`14_numpy_joining_arrays.ipynb`](./14_numpy_joining_arrays.ipynb) | Joining & Stacking | `np.concatenate()`, `np.vstack()`, `np.hstack()`, `np.stack()`, `np.dstack()` | ✅ |
| **15** | [`15_numpy_splitting_arrays.ipynb`](./15_numpy_splitting_arrays.ipynb) | Splitting Arrays | `np.split()`, `np.array_split()`, `np.vsplit()`, `np.hsplit()` | ✅ |
| **16** | [`16_numpy_sorting_searching.ipynb`](./16_numpy_sorting_searching.ipynb) | Sorting & Searching | `np.sort()`, index sorting (`np.argsort()`), binary search (`searchsorted`) | ✅ |
| **17** | [`17_numpy_copy_vs_view.ipynb`](./17_numpy_copy_vs_view.ipynb) | Copy vs. View Dynamics | Shared memory buffers, mutation side-effects, `.base` attribute validation | ✅ |
| **18** | [`18_numpy_linear_algebra.ipynb`](./18_numpy_linear_algebra.ipynb) | Linear Algebra (`np.linalg`) | Matrix product (`@`), transposes (`.T`), determinants, inverses, eigenvalues | ✅ |
| **19** | [`19_numpy_practice.ipynb`](./19_numpy_practice.ipynb) | Practice Exercises | Z-score normalization, matrix manipulation, multi-dimensional masking | ✅ |
| **20** | [`20_numpy_mini_project.ipynb`](./20_numpy_mini_project.ipynb) | Capstone EDA Project | **Real Estate EDA & Feature Pipeline**: Cleaning, Filtering, Normalization | ✅ |

---

## 🔍 Phase-by-Phase Guide

### Phase 1: Ndarray Foundations & Slicing (`01` – `05`)
Establishes how multidimensional numeric data is organized and traversed in memory.

#### 1. [`01_numpy_introduction.ipynb`](./01_numpy_introduction.ipynb) — NumPy Introduction
- **Focus**: Why NumPy outperforms native Python lists; contiguous memory allocation and vectorization speedups.
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)  # Vectorized operation: [ 2  4  6  8 10]
```

#### 2. [`02_numpy_data_types.ipynb`](./02_numpy_data_types.ipynb) — Data Types (`dtype`)
- **Focus**: Homogeneous typed storage (`int32`, `float64`, `bool_`) and safe casting with `.astype()`.
```python
arr = np.array([1.5, 2.7, 3.2], dtype=np.float32)
arr_int = arr.astype(np.int32)  # [1, 2, 3]
```

#### 3. [`03_numpy_multidimensional_arrays.ipynb`](./03_numpy_multidimensional_arrays.ipynb) — Multi-Dimensional Arrays
- **Focus**: Working with vectors (1D), matrices (2D), and tensors (3D+) using multi-axis coordinate indexing `arr[row, col]`.
```python
matrix = np.array([[10, 20, 30], [40, 50, 60]])
print(matrix[1, 2])  # Output: 60
```

#### 4. [`04_numpy_reshape.ipynb`](./04_numpy_reshape.ipynb) — Reshaping & Flattening Arrays
- **Focus**: Changing array topology without mutating underlying data, using `-1` wildcard inference, and choosing `.ravel()` (zero-copy view) vs. `.flatten()` (allocated copy).
```python
arr = np.arange(12)
matrix = arr.reshape(3, 4)
flat_view = matrix.ravel()
```

#### 5. [`05_numpy_slicing.ipynb`](./05_numpy_slicing.ipynb) — Array Slicing Techniques
- **Focus**: Advanced multi-axis slicing syntax `[start:stop:step]`, negative strides, and multidimensional cropping.
```python
grid = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sub_grid = grid[0:2, 1:3]  # Rows 0-1, Columns 1-2
```

---

### Phase 2: Vectorization, Broadcasting & Core Functions (`06` – `10`)
Eliminating iterative bottlenecks with vectorized computing and universal functions.

#### 6. [`06_numpy_arithmetic.ipynb`](./06_numpy_arithmetic.ipynb) — Vectorized Arithmetic Operations
- **Focus**: Element-wise mathematical ufuncs (`np.add`, `np.multiply`, `np.sqrt`, `np.exp`).
```python
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print(a + b)  # [11, 22, 33]
```

#### 7. [`07_numpy_broadcasting.ipynb`](./07_numpy_broadcasting.ipynb) — Array Broadcasting
- **Focus**: Arithmetic on arrays with different shapes without copying data; mean-centering feature matrices.
```python
data = np.array([[10, 20], [30, 40]])
feature_mean = np.mean(data, axis=0)
centered_data = data - feature_mean  # Broadcasted subtraction
```

#### 8. [`08_numpy_useful_functions.ipynb`](./08_numpy_useful_functions.ipynb) — Array Creation Utilities
- **Focus**: High-speed array initialization routines.
```python
identity = np.eye(3)
grid_space = np.linspace(0.0, 1.0, num=5)  # [0. , 0.25, 0.5 , 0.75, 1. ]
```

#### 9. [`09_numpy_aggregate_functions.ipynb`](./09_numpy_aggregate_functions.ipynb) — Aggregate Statistical Functions
- **Focus**: Global and axis-specific reduction statistics (`np.mean`, `np.std`, `np.median`, `np.argmax`).
```python
matrix = np.array([[1, 2], [3, 4]])
col_sums = np.sum(matrix, axis=0)  # [4, 6]
row_sums = np.sum(matrix, axis=1)  # [3, 7]
```

#### 10. [`10_numpy_filtering.ipynb`](./10_numpy_filtering.ipynb) — Filtering & Boolean Indexing
- **Focus**: Vectorized filtering via boolean masks and conditional element replacement with `np.where`.
```python
scores = np.array([45, 88, 72, 95, 30])
passing = scores[scores >= 60]             # [88, 72, 95]
labels = np.where(scores >= 60, "Pass", "Fail")
```

---

### Phase 3: Random Numbers, Storage & Memory Layout (`11` – `13`)
Data generation, disk persistence, and memory inspection.

#### 11. [`11_numpy_random_numbers.ipynb`](./11_numpy_random_numbers.ipynb) — Random Sampling (RNG)
- **Focus**: Reproducible random seeds, standard normal sampling (`randn`), discrete distributions, and array shuffling.
```python
np.random.seed(42)
weights = np.random.randn(4, 3)  # 4x3 Gaussian distribution
```

#### 12. [`12_numpy_saving_loading.ipynb`](./12_numpy_saving_loading.ipynb) — Saving & Loading Arrays
- **Focus**: Persistent storage with single binary `.npy`, compressed multi-array `.npz`, and text CSV files.
```python
arr = np.array([10, 20, 30])
np.save("data.npy", arr)
loaded = np.load("data.npy")
```

#### 13. [`13_numpy_array_attributes.ipynb`](./13_numpy_array_attributes.ipynb) — Array Attributes
- **Focus**: Profiling array metadata and memory consumption.
```python
tensor = np.ones((100, 50), dtype=np.float64)
print(f"Shape: {tensor.shape} | Itemsize: {tensor.itemsize}B | Total: {tensor.nbytes}B")
```

---

### Phase 4: Matrix Operations & Linear Algebra (`14` – `18`)
Tensor manipulation and foundational linear algebra operations required for ML modeling.

#### 14. [`14_numpy_joining_arrays.ipynb`](./14_numpy_joining_arrays.ipynb) — Joining & Stacking Arrays
- **Focus**: Combining tensors along existing axes (`np.concatenate`) or new axes (`np.vstack`, `np.hstack`, `np.stack`).
```python
a = np.array([1, 2])
b = np.array([3, 4])
v_stacked = np.vstack((a, b))  # [[1, 2], [3, 4]]
```

#### 15. [`15_numpy_splitting_arrays.ipynb`](./15_numpy_splitting_arrays.ipynb) — Splitting Arrays
- **Focus**: Partitioning matrices for train/test splits or feature/target separation.
```python
arr = np.arange(9)
train, val, test = np.split(arr, 3)
```

#### 16. [`16_numpy_sorting_searching.ipynb`](./16_numpy_sorting_searching.ipynb) — Sorting & Searching Arrays
- **Focus**: In-place sorting, sorted index retrieval with `np.argsort`, and $\mathcal{O}(\log n)$ binary searches with `np.searchsorted`.
```python
prices = np.array([250, 100, 300])
rankings = np.argsort(prices)  # [1, 0, 2]
```

#### 17. [`17_numpy_copy_vs_view.ipynb`](./17_numpy_copy_vs_view.ipynb) — Copy vs. View Dynamics
- **Focus**: Preventing accidental in-place mutations; identifying base array ownership with `.base`.
```python
orig = np.array([10, 20, 30])
view_arr = orig[:2]        # Modifying view_arr mutates orig!
copy_arr = orig[:2].copy() # Safe independent buffer
```

#### 18. [`18_numpy_linear_algebra.ipynb`](./18_numpy_linear_algebra.ipynb) — Linear Algebra (`np.linalg`)
- **Focus**: Matrix products with the `@` operator, transposes, determinants, inverses, and eigenvalue/eigenvector decompositions.
```python
A = np.array([[2, 1], [5, 3]])
inv_A = np.linalg.inv(A)
det_A = np.linalg.det(A)
```

---

### Phase 5: Practice & Capstone Mini-Project (`19` – `20`)

#### 19. [`19_numpy_practice.ipynb`](./19_numpy_practice.ipynb) — Comprehensive Practice Exercises
- **Focus**: Problem sets combining multi-axis filtering, Z-score standardizations, and matrix generation challenges.

#### 20. [`20_numpy_mini_project.ipynb`](./20_numpy_mini_project.ipynb) — Real Estate EDA Mini-Project
- **Focus**: End-to-end data analysis and feature engineering pipeline on real estate matrices.

---

## 🏠 Capstone Project Spotlight

### 📊 Real Estate Exploratory Data Analysis & Feature Pipeline
**File:** [`20_numpy_mini_project.ipynb`](./20_numpy_mini_project.ipynb)

A comprehensive data engineering pipeline executed exclusively using pure vectorized NumPy without Pandas.

```
       Raw Feature Matrix [10 x 4]
┌───────┬───────┬─────────┬──────────────┐
│ SqFt  │ Beds  │  Baths  │    Price     │
└───────┴───────┴─────────┴──────────────┘
                    │
                    ▼
  [Vectorized Summary Statistics]
  Mean, Median, Standard Deviation per Axis
                    │
                    ▼
  [Feature Engineering]
  Price per SqFt = Price / SqFt
                    │
                    ▼
  [Outlier Filtering]
  Boolean Mask: Price > $500,000
                    │
                    ▼
  [Feature Normalization]
  Min-Max Scaling: X_norm = (X - X_min) / (X_max - X_min)
```

#### Metrics & Pipeline Steps:
1. **Synthetic Matrix Generation**: Stacking feature columns `[SqFt, Bedrooms, Bathrooms, Price]` via `np.hstack`.
2. **Axis-Specific Statistical Profiling**: Global mean and feature standard deviations computed via `np.mean(axis=0)` and `np.std(axis=0)`.
3. **Engineered Metrics**: Vectorized calculation of `Price / SqFt` across all properties in $\mathcal{O}(1)$ lines of code.
4. **Outlier Filtering**: Extracting luxury homes using boolean mask indexing:
   $$\text{luxury\_mask} = \text{dataset}[:, 3] > 500{,}000$$
5. **Feature Scaling (Min-Max Normalization)**:
   $$X_{\text{norm}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}$$

---

## ⚡ Performance Benchmark: Python Lists vs. NumPy Ndarrays

Why do AI and Machine Learning practitioners rely on NumPy?

```python
import numpy as np
import time

size = 10_000_000

# Native Python list
py_list = list(range(size))
t0 = time.perf_counter()
py_sum = sum(py_list)
t_py = time.perf_counter() - t0

# NumPy array
np_arr = np.arange(size)
t0 = time.perf_counter()
np_sum = np.sum(np_arr)
t_np = time.perf_counter() - t0

print(f"Python list sum: {t_py:.4f}s")
print(f"NumPy array sum: {t_np:.4f}s")
print(f"Speedup: {t_py / t_np:.1f}x faster")
```

| Metric | Native Python List | NumPy `ndarray` | Advantage |
| :--- | :--- | :--- | :--- |
| **Execution Time** | ~0.35s | ~0.007s | **~50x faster** |
| **Memory Allocation** | Pointers to Python objects (~80MB) | Contiguous C buffer (~40MB) | **2x - 4x less memory** |
| **Hardware Acceleration** | None (interpreted loop) | SIMD / BLAS / LAPACK | **Parallel CPU instruction sets** |

---

## 🚀 How to Run

### Prerequisites
- Python 3.8 or higher installed on your system.

### Environment Setup
From the root or `Numpy` directory:
```bash
# Optional: create virtual environment
python -m venv venv

# Windows
.\venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# Install NumPy and Jupyter
pip install numpy jupyter jupyterlab
```

### Launching the Notebooks
```bash
# Start Jupyter Notebook
jupyter notebook

# Or start JupyterLab
jupyter lab
```
Open any `.ipynb` notebook from the directory to run and experiment with the code!

---

## 🔗 Related Modules

- 🐍 **[Python for AI & ML Module](../Python/)**: Foundational Python syntax, data structures, and OOP design.
- 🏠 **[Root Repository Overview](../)**: Complete curriculum roadmap, getting started guides, and upcoming Pandas & ML modules.
