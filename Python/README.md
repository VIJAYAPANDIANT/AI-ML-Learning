<div align="center">

# 🐍 Python for AI & Machine Learning

### *A Comprehensive 27-Notebook Masterclass: From Programming Foundations to Data Analytics*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Curriculum](https://img.shields.io/badge/Curriculum-27%20Notebooks-blueviolet?style=for-the-badge&logo=gitbook&logoColor=white)](#-curriculum-index)
[![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)](#-curriculum-index)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](../#--license)

<br/>

<p align="center">
  <b>27 Interactive Notebooks</b> • <b>Core Syntax & OOP</b> • <b>Functional Paradigms & Decorators</b> • <b>Analytics Capstone</b>
</p>

<p align="center">
  <a href="../"><b>🏠 Main Repository</b></a> •
  <a href="#-curriculum-index"><b>📚 Curriculum Index</b></a> •
  <a href="#-phase-by-phase-guide"><b>🔍 Phase-by-Phase Guide</b></a> •
  <a href="#-capstone-project-spotlight"><b>🎓 Capstone Project</b></a> •
  <a href="#-how-to-run"><b>🚀 How to Run</b></a>
</p>

</div>

---

## 📖 Module Overview

Python is the cornerstone language of Artificial Intelligence, Data Science, and Machine Learning. Its clean syntax, expressive power, and extensive scientific ecosystem make it the primary tool for developing data pipelines, training neural networks, and deploying production AI systems.

This module provides a **code-first, rigorous curriculum** consisting of **27 self-contained Jupyter Notebooks**. Beyond basic programming constructs, the learning path emphasizes:

- **Algorithmic efficiency**: Avoiding inefficient iterative patterns in favor of comprehensions and generator pipelines.
- **Object-Oriented Design (OOP)**: Building modular, reusable architectures adhering to Encapsulation, Abstraction, Inheritance, and Polymorphism.
- **Production reliability**: Proper exception propagation, context managers (`with`), type hints, and structured serialization (JSON).
- **Seamless data transitions**: Direct bridges from built-in Python sequences to NumPy $N$-dimensional arrays and Pandas DataFrames.

---

## 🗂️ Module Architecture

```text
Python/
├── 01_python_introduction.ipynb             # Phase 1: Foundations & Control Flow
├── 02_variables_and_data_types.ipynb
├── 03_input_and_output.ipynb
├── 04_operators.ipynb
├── 05_conditional_statements.ipynb
├── 06_loops.ipynb
│
├── 07_strings.ipynb                         # Phase 2: Data Structures & Functional Tools
├── 08_lists.ipynb
├── 09_tuples.ipynb
├── 10_sets.ipynb
├── 11_dictionaries.ipynb
├── 12_functions.ipynb
├── 13_lambda_functions.ipynb
├── 14_list_comprehension.ipynb
│
├── 15_modules_and_packages.ipynb            # Phase 3: Systems, OOP & Advanced Python
├── 16_file_handling.ipynb
├── 17_exception_handling.ipynb
├── 18_object_oriented_programming.ipynb
├── 19_iterators_and_generators.ipynb
├── 20_decorators.ipynb
│
├── 21_python_datetime.ipynb                 # Phase 4: Standard Library & AI/ML Bridges
├── 22_python_regular_expressions.ipynb
├── 23_python_json.ipynb
├── 24_python_numpy_intro.ipynb
├── 25_python_pandas_intro.ipynb
│
├── 26_python_practice.ipynb                 # Phase 5: Algorithmic Practice & Capstone
├── 27_python_mini_project.ipynb
└── README.md
```

---

## 📚 Curriculum Index

| # | Notebook | Primary Topic | Core Concepts & Techniques | Status |
| :-: | :--- | :--- | :--- | :-: |
| **01** | [`01_python_introduction.ipynb`](./01_python_introduction.ipynb) | Python Introduction | Syntax conventions, whitespace indentation, comments, runtime architecture | ✅ |
| **02** | [`02_variables_and_data_types.ipynb`](./02_variables_and_data_types.ipynb) | Variables & Types | Dynamic typing, primitives (`int`, `float`, `str`, `bool`), explicit casting | ✅ |
| **03** | [`03_input_and_output.ipynb`](./03_input_and_output.ipynb) | I/O & Formatting | User input parsing, formatted output, f-strings, precision specifiers | ✅ |
| **04** | [`04_operators.ipynb`](./04_operators.ipynb) | Operators | Arithmetic, comparison, bitwise, membership (`in`), identity (`is`) | ✅ |
| **05** | [`05_conditional_statements.ipynb`](./05_conditional_statements.ipynb) | Control Flow | `if-elif-else`, ternary expressions, structural pattern matching (`match-case`) | ✅ |
| **06** | [`06_loops.ipynb`](./06_loops.ipynb) | Iteration | `for`, `while`, `range()`, `enumerate()`, `zip()`, `break`, `continue`, `pass` | ✅ |
| **07** | [`07_strings.ipynb`](./07_strings.ipynb) | Strings & Slicing | Immutability, multi-index slicing `[start:stop:step]`, text transformation methods | ✅ |
| **08** | [`08_lists.ipynb`](./08_lists.ipynb) | Lists | Dynamic arrays, in-place mutations, sorting, shallow vs. deep copy semantics | ✅ |
| **09** | [`09_tuples.ipynb`](./09_tuples.ipynb) | Tuples | Immutable sequences, sequence packing/unpacking, `namedtuple` schemas | ✅ |
| **10** | [`10_sets.ipynb`](./10_sets.ipynb) | Sets | Unique collections, hashing, set algebra (union, intersection, symmetric diff) | ✅ |
| **11** | [`11_dictionaries.ipynb`](./11_dictionaries.ipynb) | Dictionaries | Hash maps, key-value lookups, `.get()`, `Counter`, `defaultdict` | ✅ |
| **12** | [`12_functions.ipynb`](./12_functions.ipynb) | Functions & Scope | First-class functions, `*args`, `**kwargs`, LEGB variable scoping rules | ✅ |
| **13** | [`13_lambda_functions.ipynb`](./13_lambda_functions.ipynb) | Lambda & Functional | Anonymous functions, functional programming pipelines (`map`, `filter`, `reduce`) | ✅ |
| **14** | [`14_list_comprehension.ipynb`](./14_list_comprehension.ipynb) | Comprehensions | List, Dict & Set comprehensions, conditional filtering, matrix flattening | ✅ |
| **15** | [`15_modules_and_packages.ipynb`](./15_modules_and_packages.ipynb) | Modules & Packages | Standard library imports, modular organization, `sys`, `os`, namespaces | ✅ |
| **16** | [`16_file_handling.ipynb`](./16_file_handling.ipynb) | File Operations | Context managers (`with open()`), buffered file streams, text/CSV I/O | ✅ |
| **17** | [`17_exception_handling.ipynb`](./17_exception_handling.ipynb) | Error Handling | `try-except-else-finally` blocks, built-in hierarchies, custom exception classes | ✅ |
| **18** | [`18_object_oriented_programming.ipynb`](./18_object_oriented_programming.ipynb) | OOP 4 Pillars | Encapsulation (`__private`), Abstraction, Inheritance (`super()`), Polymorphism | ✅ |
| **19** | [`19_iterators_and_generators.ipynb`](./19_iterators_and_generators.ipynb) | Generators | Iterator protocol (`__iter__`, `__next__`), `yield`, lazy streaming pipelines | ✅ |
| **20** | [`20_decorators.ipynb`](./20_decorators.ipynb) | Decorators | Higher-order functions, function wrappers, `@functools.wraps`, execution timers | ✅ |
| **21** | [`21_python_datetime.ipynb`](./21_python_datetime.ipynb) | Datetime Handling | `datetime`, `timedelta`, timestamp formatting (`strftime`), parsing (`strptime`) | ✅ |
| **22** | [`22_python_regular_expressions.ipynb`](./22_python_regular_expressions.ipynb) | Regular Expressions | Regex syntax, `re.search`, `re.findall`, `re.sub`, data validation patterns | ✅ |
| **23** | [`23_python_json.ipynb`](./23_python_json.ipynb) | JSON Processing | Serialization & deserialization (`dumps`, `loads`, `dump`, `load`) | ✅ |
| **24** | [`24_python_numpy_intro.ipynb`](./24_python_numpy_intro.ipynb) | NumPy Bridge | Pure Python lists vs. `ndarray`, vectorization speedups, broadcasting intro | ✅ |
| **25** | [`25_python_pandas_intro.ipynb`](./25_python_pandas_intro.ipynb) | Pandas Bridge | Series, DataFrame creation, index-based selection (`loc`/`iloc`), head inspection | ✅ |
| **26** | [`26_python_practice.ipynb`](./26_python_practice.ipynb) | Practice Problem Set | 10 Comprehensive multi-domain algorithmic coding challenges with solutions | ✅ |
| **27** | [`27_python_mini_project.ipynb`](./27_python_mini_project.ipynb) | Capstone Project | **Student Performance & Analytics System**: OOP + File I/O + JSON + Analytics | ✅ |

---

## 🔍 Phase-by-Phase Guide

### Phase 1: Core Fundamentals & Control Flow (`01` – `06`)
Builds rock-solid foundational programming discipline.
- **Key Concepts**: Explicit type conversion, f-string templating, relational & identity operators (`is` vs `==`), nested condition evaluation, and high-performance loop constructs.
```python
# Modern Python 3.10+ Pattern Matching
command = "FETCH_DATA"
match command:
    case "FETCH_DATA":
        status = "Processing query..."
    case "ABORT":
        status = "Operation cancelled."
    case _:
        status = "Unknown command."
```

---

### Phase 2: Data Structures & Functional Programming (`07` – `14`)
Explores Python's memory collections and functional paradigms vital for data manipulation.
- **Key Concepts**: String immutability, list mutation methods, shallow vs. deep copies (`copy.deepcopy`), set operations for de-duplication, hash-map dictionaries, variadic function signatures (`*args`, `**kwargs`), and concise nested comprehensions.
```python
# Multi-conditional Matrix Flattening & Transformation
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
evens_squared = [val ** 2 for row in matrix for val in row if val % 2 == 0]
# Output: [4, 16, 36, 64]
```

---

### Phase 3: Systems, OOP & Advanced Python (`15` – `20`)
Transitions from procedural scripting to enterprise-grade object-oriented system design.
- **Key Concepts**: Safe file manipulation with context managers, custom exception raising, class inheritance with method overriding, memory-efficient generators (`yield`) for massive datasets, and meta-programming with decorators.
```python
import functools
import time

def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"Executed {func.__name__} in {duration:.6f}s")
        return result
    return wrapper
```

---

### Phase 4: Standard Library & AI/ML Bridges (`21` – `25`)
Prepares developers for real-world machine learning libraries by mastering data interchange formats and library entry points.
- **Key Concepts**: Temporal features with `datetime`, pattern extraction with `re`, JSON data persistence, and foundational transitions into `numpy.ndarray` and `pandas.DataFrame`.
```python
import json

# Serializing structured AI dataset configuration
config = {"model": "RandomForest", "n_estimators": 100, "metrics": ["accuracy", "f1_score"]}
json_data = json.dumps(config, indent=2)
```

---

### Phase 5: Algorithmic Challenges & Capstone (`26` – `27`)
Integrates all preceding concepts into rigorous algorithmic practice and an end-to-end analytical application.
- **Key Concepts**: Algorithmic optimization, data validation, object modeling, and aggregate statistical reporting.

---

## 🎓 Capstone Project Spotlight

### 📊 Student Grade & Performance Analytics System
**File:** [`27_python_mini_project.ipynb`](./27_python_mini_project.ipynb)

A modular, object-oriented system engineered to manage student cohort performance, enforce data validation constraints, and generate statistical insights.

```
                  ┌────────────────────────┐
                  │      GradeBook         │
                  ├────────────────────────┤
                  │ - students: dict       │
                  ├────────────────────────┤
                  │ + add_student()        │
                  │ + get_class_average()  │
                  │ + get_top_performers() │
                  │ + export_to_json()     │
                  └───────────┬────────────┘
                              │ 1..* manages
                              ▼
                  ┌────────────────────────┐
                  │        Student         │
                  ├────────────────────────┤
                  │ - student_id: int      │
                  │ - name: str            │
                  │ - scores: dict         │
                  ├────────────────────────┤
                  │ + add_score()          │
                  │ + calculate_average()  │
                  │ + to_dict()            │
                  └────────────────────────┘
```

#### Key Capabilities Demonstrated:
1. **Domain Modeling**: Encapsulated entities (`Student`, `GradeBook`) with strict validation (score bounds $0 \le score \le 100$).
2. **Statistical Aggregations**: Calculates individual averages, class-wide means, and dynamic grade thresholds.
3. **Data Persistence**: Exports clean, nested JSON reports with execution timestamps.
4. **Resilient Execution**: Graceful handling of invalid inputs and custom error states.

---

## 💡 Best Practices for AI & Machine Learning Python

| Practice | Bad Approach | Recommended Approach |
| :--- | :--- | :--- |
| **Iteration** | Manual indexing `range(len(items))` | Pythonic `enumerate(items)` or `zip(a, b)` |
| **Collection Search** | Searching in lists `target in large_list` ($\mathcal{O}(n)$) | Searching in sets/dicts `target in hash_set` ($\mathcal{O}(1)$) |
| **Memory Streaming** | Loading entire massive file into a list | Streaming line-by-line via a generator with `yield` |
| **String Building** | Repeated concatenation `s += word` in a loop | Fast list accumulation and `' '.join(words)` |
| **Safe Resource I/O** | `f = open(...); ...; f.close()` | Safe context manager `with open(...) as f:` |

---

## 🚀 How to Run

### Prerequisites
- Python 3.8 or higher installed on your system.

### Installation
From the root or `Python` directory:
```bash
# Optional: create and activate virtual environment
python -m venv venv

# Windows
.\venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# Install required tools
pip install jupyter jupyterlab numpy pandas
```

### Launching the Notebooks
```bash
# Launch Jupyter Notebook
jupyter notebook

# Or launch modern JupyterLab
jupyter lab
```
Open any `.ipynb` notebook from the directory tree to inspect explanations and run code cells interactively!

---

## 🔗 Related Modules

- 🔢 **[NumPy Numerical Masterclass](../Numpy/)**: Next step in the AI/ML curriculum covering $N$-dimensional arrays, broadcasting, vectorization, and linear algebra.
- 🏠 **[Root Repository Overview](../)**: Full curriculum roadmap, setup instructions, and future modules.
