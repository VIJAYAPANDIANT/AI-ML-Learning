# 🔢 NumPy for AI & Machine Learning

Welcome to the **NumPy** module of the **AI-ML Learning** repository! NumPy (Numerical Python) is the foundational library for scientific computing and data manipulation in Python, powering almost all modern AI, Data Science, and Machine Learning frameworks.

---

## 🗂️ Module Directory Structure

```text
NumPy/
│
├── README.md
│
├── 01_numpy_introduction.ipynb
├── 02_numpy_data_types.ipynb
├── 03_numpy_multidimensional_arrays.ipynb
├── 04_numpy_reshape.ipynb
├── 05_numpy_slicing.ipynb
├── 06_numpy_arithmetic.ipynb
├── 07_numpy_broadcasting.ipynb
├── 08_numpy_useful_functions.ipynb
├── 09_numpy_aggregate_functions.ipynb
├── 10_numpy_filtering.ipynb
├── 11_numpy_random_numbers.ipynb
├── 12_numpy_saving_loading.ipynb
│
├── 13_numpy_array_attributes.ipynb
├── 14_numpy_joining_arrays.ipynb
├── 15_numpy_splitting_arrays.ipynb
├── 16_numpy_sorting_searching.ipynb
├── 17_numpy_copy_vs_view.ipynb
├── 18_numpy_linear_algebra.ipynb
│
├── 19_numpy_practice.ipynb
└── 20_numpy_mini_project.ipynb
```

---

## 📚 Detailed Topic Breakdown & Notebook Guides

### 1. [`01_numpy_introduction.ipynb`](./01_numpy_introduction.ipynb) — NumPy Introduction
- **Overview**: Learn why NumPy is preferred over native Python lists for numeric computing. Understand memory layout, C-level optimization, and speed gains from vectorization.
- **Key Concepts**: `np.array()`, `np.__version__`, performance benchmarking.
```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)  # Output: [ 2  4  6  8 10]
```

---

### 2. [`02_numpy_data_types.ipynb`](./02_numpy_data_types.ipynb) — Data Types (`dtype`)
- **Overview**: NumPy arrays are homogeneous. Explore primitive numerical dtypes (`int32`, `int64`, `float32`, `float64`, `bool_`, `complex128`), explicit type assignment, and casting with `.astype()`.
- **Key Concepts**: `.dtype`, explicit `dtype=` parameter, type conversion.
```python
arr = np.array([1, 2, 3], dtype='float32')
arr_int = arr.astype(np.int64)
```

---

### 3. [`03_numpy_multidimensional_arrays.ipynb`](./03_numpy_multidimensional_arrays.ipynb) — Multi-Dimensional Arrays
- **Overview**: Master scalar (0D), vector (1D), matrix (2D), and tensor (3D+) arrays. Learn tuple-based multi-dimensional indexing.
- **Key Concepts**: `.ndim`, `.shape`, multi-axis indexing `arr[row, col]`.
```python
matrix_2d = np.array([[1, 2, 3], [4, 5, 6]])
val = matrix_2d[1, 2] # 6
```

---

### 4. [`04_numpy_reshape.ipynb`](./04_numpy_reshape.ipynb) — Reshaping & Flattening Arrays
- **Overview**: Change array dimensions without altering underlying data. Understand automatic dimension inference using `-1` and the difference between `.flatten()` (copy) and `.ravel()` (view).
- **Key Concepts**: `.reshape()`, `-1` wildcard, `.flatten()`, `.ravel()`.
```python
arr = np.arange(12)
matrix = arr.reshape(3, 4)
flat = matrix.ravel()
```

---

### 5. [`05_numpy_slicing.ipynb`](./05_numpy_slicing.ipynb) — Array Slicing Techniques
- **Overview**: Slice 1D and 2D arrays using `[start:stop:step]` syntax along multiple dimensions simultaneously.
- **Key Concepts**: Sub-array extraction, step slicing `[::2]`, array reversing `[::-1]`.
```python
grid = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sub_matrix = grid[0:2, 1:3] # Top 2 rows, cols 1-2
```

---

### 6. [`06_numpy_arithmetic.ipynb`](./06_numpy_arithmetic.ipynb) — Vectorized Arithmetic Operations
- **Overview**: Perform element-wise addition, subtraction, multiplication, division, powers, and universal mathematical functions (`ufuncs`).
- **Key Concepts**: Vectorized operations, `np.add()`, `np.sqrt()`, `np.exp()`, `np.sin()`.
```python
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
result = a + b # [11, 22, 33]
```

---

### 7. [`07_numpy_broadcasting.ipynb`](./07_numpy_broadcasting.ipynb) — Array Broadcasting
- **Overview**: Perform arithmetic operations on arrays of incompatible shapes without manual array duplication.
- **Key Concepts**: Broadcasting rules, scalar-to-array, 1D-vector-to-2D-matrix, mean-centering data.
```python
data = np.array([[10, 20], [30, 40]])
mean = np.mean(data, axis=0)
centered = data - mean
```

---

### 8. [`08_numpy_useful_functions.ipynb`](./08_numpy_useful_functions.ipynb) — Useful Array Creation Utilities
- **Overview**: Rapidly initialize arrays filled with zeros, ones, constant values, identity matrices, or numeric sequences.
- **Key Concepts**: `np.zeros()`, `np.ones()`, `np.full()`, `np.eye()`, `np.arange()`, `np.linspace()`.
```python
identity = np.eye(3)
sequence = np.linspace(0, 1, 5) # 5 evenly spaced numbers from 0 to 1
```

---

### 9. [`09_numpy_aggregate_functions.ipynb`](./09_numpy_aggregate_functions.ipynb) — Aggregate Statistical Functions
- **Overview**: Compute statistical metrics globally or across specific axes (`axis=0` for columns, `axis=1` for rows).
- **Key Concepts**: `np.sum()`, `np.mean()`, `np.std()`, `np.median()`, `np.min()`, `np.max()`, `np.argmax()`.
```python
data = np.array([[1, 2], [3, 4]])
col_sums = np.sum(data, axis=0) # [4, 6]
```

---

### 10. [`10_numpy_filtering.ipynb`](./10_numpy_filtering.ipynb) — Filtering & Boolean Indexing
- **Overview**: Extract elements using conditional boolean masks, combine conditions using bitwise operators (`&`, `|`), and conditionally replace values using `np.where()`.
- **Key Concepts**: Boolean indexing, logical masking, `np.where(condition, x, y)`.
```python
arr = np.array([10, 25, 30, 5])
filtered = arr[arr > 20] # [25, 30]
replaced = np.where(arr > 20, 999, arr)
```

---

### 11. [`11_numpy_random_numbers.ipynb`](./11_numpy_random_numbers.ipynb) — Random Number Generation
- **Overview**: Generate random numbers from uniform, standard normal, and integer distributions. Practice seed reproducibility and random sampling.
- **Key Concepts**: `np.random.seed()`, `np.random.rand()`, `np.random.randn()`, `np.random.randint()`, `np.random.choice()`, `np.random.shuffle()`.
```python
np.random.seed(42)
rand_mat = np.random.randn(3, 3) # 3x3 Standard Normal
```

---

### 12. [`12_numpy_saving_loading.ipynb`](./12_numpy_saving_loading.ipynb) — Saving & Loading Arrays
- **Overview**: Save array data to persistent disk storage using binary formats (`.npy`, `.npz`) or text/CSV formats, and reload them.
- **Key Concepts**: `np.save()`, `np.load()`, `np.savez()`, `np.savetxt()`, `np.loadtxt()`.
```python
arr = np.array([1, 2, 3, 4])
np.save('my_array.npy', arr)
loaded_arr = np.load('my_array.npy')
```

---

### 13. [`13_numpy_array_attributes.ipynb`](./13_numpy_array_attributes.ipynb) — Array Attributes
- **Overview**: Inspect essential array properties including dimension count, shape, total item count, element byte size, and memory footprint.
- **Key Concepts**: `.ndim`, `.shape`, `.size`, `.dtype`, `.itemsize`, `.nbytes`.
```python
arr = np.ones((4, 5), dtype='float64')
print(f"Shape: {arr.shape}, Memory: {arr.nbytes} bytes")
```

---

### 14. [`14_numpy_joining_arrays.ipynb`](./14_numpy_joining_arrays.ipynb) — Joining & Stacking Arrays
- **Overview**: Combine multiple arrays along existing dimensions using `concatenate` or stack along new axes vertically, horizontally, or depth-wise.
- **Key Concepts**: `np.concatenate()`, `np.vstack()`, `np.hstack()`, `np.stack()`, `np.dstack()`.
```python
a = np.array([1, 2])
b = np.array([3, 4])
v_stacked = np.vstack((a, b)) # [[1, 2], [3, 4]]
```

---

### 15. [`15_numpy_splitting_arrays.ipynb`](./15_numpy_splitting_arrays.ipynb) — Splitting Arrays
- **Overview**: Divide a single array into multiple smaller sub-arrays equally or at specified indices.
- **Key Concepts**: `np.split()`, `np.array_split()`, `np.vsplit()`, `np.hsplit()`.
```python
arr = np.arange(9)
parts = np.split(arr, 3) # [0, 1, 2], [3, 4, 5], [6, 7, 8]
```

---

### 16. [`16_numpy_sorting_searching.ipynb`](./16_numpy_sorting_searching.ipynb) — Sorting & Searching Arrays
- **Overview**: Sort elements in ascending/descending order, retrieve sorted indices (`argsort`), perform binary searches (`searchsorted`), and extract non-zero elements.
- **Key Concepts**: `np.sort()`, `np.argsort()`, `np.searchsorted()`, `np.nonzero()`.
```python
arr = np.array([30, 10, 20])
sorted_indices = np.argsort(arr) # [1, 2, 0]
```

---

### 17. [`17_numpy_copy_vs_view.ipynb`](./17_numpy_copy_vs_view.ipynb) — Copy vs View Memory Dynamics
- **Overview**: Understand how NumPy optimizes memory via array views (shallow copies) versus explicit deep copies (`.copy()`). Learn to check data ownership with `.base`.
- **Key Concepts**: View vs Copy memory behavior, `.copy()`, `.base` attribute check.
```python
original = np.array([1, 2, 3])
view_arr = original[0:2] # Modifying view mutates original!
copy_arr = original[0:2].copy() # Independent memory buffer
```

---

### 18. [`18_numpy_linear_algebra.ipynb`](./18_numpy_linear_algebra.ipynb) — Linear Algebra (`np.linalg`)
- **Overview**: Perform essential linear algebra operations used in Machine Learning: matrix multiplication, transposes, determinants, inverses, and eigenvalue decompositions.
- **Key Concepts**: `@` matrix product operator, `np.dot()`, `.T`, `np.linalg.det()`, `np.linalg.inv()`, `np.linalg.eig()`.
```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
matrix_prod = A @ B
inv_A = np.linalg.inv(A)
```

---

### 19. [`19_numpy_practice.ipynb`](./19_numpy_practice.ipynb) — Comprehensive Practice Exercises
- **Overview**: Hands-on challenge notebook combining multiple NumPy topics into practical problem sets (z-score normalization, matrix patterns, masking).
- **Key Concepts**: Problem-solving, array manipulation, data standardization.

---

### 20. [`20_numpy_mini_project.ipynb`](./20_numpy_mini_project.ipynb) — Real Estate EDA Mini-Project
- **Overview**: End-to-end mini project applying NumPy to clean, filter, analyze, and feature-engineer synthetic real estate data `[SqFt, Bedrooms, Bathrooms, Price]`.
- **Key Concepts**: Exploratory Data Analysis (EDA), feature scaling (Min-Max scaling), outlier filtering, price per square foot calculations.

---

## 🚀 How to Run the Notebooks

1. Ensure Python 3.8+ and NumPy are installed:
```bash
pip install numpy jupyter
```
2. Launch Jupyter Notebook or Jupyter Lab from the `NumPy` directory:
```bash
jupyter notebook
```
3. Open any `.ipynb` file and execute the cells sequentially!
