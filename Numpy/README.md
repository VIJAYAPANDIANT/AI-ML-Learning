# NumPy for AI & Machine Learning

Welcome to the **NumPy** module of the AI-ML Learning repository. NumPy (Numerical Python) is the foundational library for scientific computing in Python, providing support for large, multi-dimensional arrays and matrices along with a collection of mathematical functions.

---

## 📌 Topics Covered

- [x] **Array Creation**: Creating 1D, 2D, and multi-dimensional arrays (`np.array`)
- [x] **Vectorized Operations**: Element-wise arithmetic and scalar operations
- [ ] **Array Indexing & Slicing**: Slicing sub-arrays and boolean indexing
- [ ] **Reshaping & Transposing**: `reshape()`, `ravel()`, `T`
- [ ] **Matrix Math & Linear Algebra**: Matrix multiplication (`np.dot`, `@`), determinants, eigenvalues
- [ ] **Broadcasting**: Performing operations across arrays of different shapes
- [ ] **Random Number Generation**: `np.random` for sample generation

---

## 📓 Notebooks & Code

- [`01_numpy_basics.ipynb`](./01_numpy_basics.ipynb) — Introduction to NumPy array creation and basic scalar math operations.

---

## 🚀 Quick Example

```python
import numpy as np

# Create a NumPy array
numbers = np.array([10, 20, 30, 40, 50])

# Perform vectorized multiplication
result = numbers * 2
print(result)  # Output: [ 20  40  60  80 100]
```

---

## 💡 Key Features of NumPy

| Feature | Description |
| :--- | :--- |
| **`ndarray`** | Fast and space-efficient multi-dimensional array object |
| **Vectorization** | Eliminates explicit Python `for` loops for high performance |
| **Broadcasting** | Allows arithmetic operations on arrays of different dimensions |
| **C/C++ Integration** | Built on optimized C binaries for speed |
