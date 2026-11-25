<div align="center">

# ⚙️ Scikit-Learn for Machine Learning & Predictive Modeling

### *A Production-Grade 35-Notebook Masterclass: From Preprocessing & Classical Algorithms to Ensembles, Pipelines & Model Persistence*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.2%2B-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Curriculum](https://img.shields.io/badge/Curriculum-35%20Notebooks-blueviolet?style=for-the-badge&logo=gitbook&logoColor=white)](#-curriculum-index)
[![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)](#-curriculum-index)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](../#--license)

<br/>

<p align="center">
  <b>35 Interactive Notebooks</b> • <b>Supervised & Unsupervised Learning</b> • <b>Leakage-Free Pipelines</b> • <b>Enterprise Churn Capstone</b>
</p>

<p align="center">
  <a href="../"><b>🏠 Main Repository</b></a> •
  <a href="../Python/"><b>🐍 Python Module</b></a> •
  <a href="../Numpy/"><b>🔢 NumPy Module</b></a> •
  <a href="../Pandas/"><b>📊 Pandas Module</b></a> •
  <a href="../Matplotlib/"><b>📈 Matplotlib Module</b></a> •
  <a href="../Seaborn/"><b>📊 Seaborn Module</b></a> •
  <a href="#-curriculum-index"><b>📚 Curriculum Index</b></a> •
  <a href="#-capstone-project-spotlight"><b>🎯 Capstone Project</b></a>
</p>

</div>

---

## 📖 Module Overview

**Scikit-learn** is the industry standard for classical machine learning and data science in Python. Built upon NumPy, SciPy, and Matplotlib, it delivers a unified, elegant, and computationally efficient API for supervised learning (regression, classification), unsupervised learning (clustering, dimensionality reduction), data preprocessing, model selection, and production pipeline deployment.

### Why Scikit-Learn is Essential for AI/ML:
- **Consistent Object-Oriented Interface**: Every estimator implements `.fit()`, `.predict()`, `.predict_proba()`, or `.transform()`, creating an intuitive and modular developer experience.
- **Leakage-Free Orchestration**: The `Pipeline` and `ColumnTransformer` APIs ensure preprocessing steps (imputation, scaling, encoding) learn statistics strictly from training splits, completely eliminating data leakage.
- **Comprehensive Algorithmic Coverage**: State-of-the-art implementations of Linear Models, Tree Ensembles (Random Forest, Gradient Boosting), Support Vector Machines, Nearest Neighbors, K-Means, DBSCAN, and Principal Component Analysis (PCA).
- **Production Validation & Tuning**: Rigorous model evaluation via Stratified K-Fold cross-validation, exhaustive `GridSearchCV`, randomized search, and model serialization with `joblib`.

This module delivers a complete **35-Notebook Masterclass** designed to take you from foundational ML concepts to deploying battle-tested enterprise predictive pipelines.

---

## 🗂️ Topic Categories & Learning Path

| Category | Topics Covered | Notebooks |
| :--- | :--- | :--- |
| **Fundamentals** | Scikit-learn architecture, 5-stage ML lifecycle, built-in datasets & generators | [`01`](./01_scikit_learn_introduction.ipynb) – [`03`](./03_loading_datasets.ipynb) |
| **Data Preprocessing** | Feature extraction, train/test splitting, imputation, one-hot/ordinal encoding, scaling, feature selection | [`04`](./04_features_and_labels.ipynb) – [`10`](./10_feature_selection.ipynb) |
| **Supervised Learning** | Mathematical formulation of regression and classification objectives | [`11`](./11_linear_regression.ipynb) – [`20`](./20_gradient_boosting.ipynb) |
| **Regression Algorithms** | Ordinary Least Squares, Ridge ($L_2$), Lasso ($L_1$), Polynomial regression | [`11`](./11_linear_regression.ipynb) – [`13`](./13_polynomial_regression.ipynb) |
| **Classification Algorithms** | Logistic Regression, KNN, Decision Trees, Random Forests, Support Vector Machines, Naive Bayes | [`14`](./14_logistic_regression.ipynb) – [`19`](./19_naive_bayes.ipynb) |
| **Ensemble Learning** | Bootstrap Aggregating (Bagging / Random Forest) and Sequential Boosting (Gradient Boosting) | [`17`](./17_random_forest.ipynb), [`20`](./20_gradient_boosting.ipynb) |
| **Unsupervised Learning** | Centroid-based (K-Means), agglomerative hierarchical, and density-based (DBSCAN) clustering | [`21`](./21_k_means_clustering.ipynb) – [`23`](./23_dbscan_clustering.ipynb) |
| **Dimensionality Reduction** | Principal Component Analysis (PCA), explained variance ratio, eigenvalue decomposition | [`24`](./24_pca_dimensionality_reduction.ipynb) |
| **Model Evaluation** | Confusion matrices, Precision, Recall, F1-Score, ROC-AUC, PR-AUC, MAE, MSE, RMSE, $R^2$ | [`25`](./25_model_evaluation.ipynb) – [`28`](./28_regression_metrics.ipynb) |
| **Model Optimization** | K-Fold & Stratified K-Fold CV, hyperparameter spaces, GridSearchCV, RandomizedSearchCV | [`29`](./29_cross_validation.ipynb) – [`31`](./31_grid_search_and_random_search.ipynb) |
| **Advanced Workflow** | Scikit-Learn `Pipeline`, `ColumnTransformer`, production serialization via Joblib | [`32`](./32_pipelines.ipynb) – [`33`](./33_model_persistence.ipynb) |
| **Practice & Capstone** | 10 multi-domain algorithmic practice sets & End-to-End Enterprise Churn Capstone | [`34`](./34_scikit_learn_practice.ipynb) – [`35`](./35_scikit_learn_mini_project.ipynb) |

---

## 📁 Repository & Directory Structure

```text
Scikit-learn/
│
├── README.md                                # Comprehensive module documentation & guide
│
├── 01_scikit_learn_introduction.ipynb       # Scikit-learn architecture, API conventions & estimators
├── 02_machine_learning_workflow.ipynb       # 5-stage ML lifecycle: data -> train -> evaluate -> deploy
├── 03_loading_datasets.ipynb                # Toy datasets, synthetic generators, openml fetches
├── 04_features_and_labels.ipynb             # Feature matrix X vs target vector y structure
├── 05_train_test_split.ipynb                # Train/test split, random_state, stratified sampling
├── 06_data_preprocessing.ipynb              # Preprocessing fundamentals, transformers & fit_transform
├── 07_handling_missing_values.ipynb         # SimpleImputer, KNNImputer, IterativeImputer strategies
├── 08_encoding_categorical_data.ipynb       # OneHotEncoder, OrdinalEncoder, LabelEncoder mechanics
├── 09_feature_scaling.ipynb                 # StandardScaler, MinMaxScaler, RobustScaler comparisons
├── 10_feature_selection.ipynb               # SelectKBest, VarianceThreshold, RFE recursive elimination
│
├── 11_linear_regression.ipynb               # Simple Ordinary Least Squares (OLS) regression
├── 12_multiple_linear_regression.ipynb      # Multiple regression, multicollinearity, Ridge & Lasso
├── 13_polynomial_regression.ipynb           # PolynomialFeatures, bias-variance tradeoff & degree tuning
├── 14_logistic_regression.ipynb             # Sigmoid curve, log-odds, decision thresholds & probabilities
├── 15_knn_classification.ipynb              # K-Nearest Neighbors, distance metrics & optimal k selection
├── 16_decision_tree.ipynb                   # CART algorithm, Gini impurity, entropy, tree pruning
├── 17_random_forest.ipynb                   # Bagging, feature subspacing, Out-Of-Bag (OOB) error
├── 18_support_vector_machine.ipynb          # Support vectors, C margin penalty, RBF & polynomial kernels
├── 19_naive_bayes.ipynb                     # Bayes Theorem, GaussianNB, MultinomialNB, prior probabilities
├── 20_gradient_boosting.ipynb               # Sequential boosting, pseudo-residuals, learning rate shrinkage
│
├── 21_k_means_clustering.ipynb              # K-Means clustering, inertia, Elbow Method, Silhouette score
├── 22_hierarchical_clustering.ipynb         # Agglomerative clustering, linkage criteria, dendrograms
├── 23_dbscan_clustering.ipynb               # Density-based spatial clustering, eps, min_samples, noise
├── 24_pca_dimensionality_reduction.ipynb    # Principal Component Analysis, scree plots, variance retention
│
├── 25_model_evaluation.ipynb                # Holdout validation, train vs test divergence, overfit detection
├── 26_confusion_matrix.ipynb                # TP, FP, TN, FN analysis, ConfusionMatrixDisplay visualization
├── 27_classification_metrics.ipynb          # Precision, Recall, F1, Balanced Accuracy, ROC-AUC, PR curves
├── 28_regression_metrics.ipynb              # MAE, MSE, RMSE, MAPE, R² score, residual analysis plots
├── 29_cross_validation.ipynb                # KFold, StratifiedKFold, cross_val_score, cross_validate
├── 30_hyperparameter_tuning.ipynb           # Parameters vs hyperparameters, validation curves
├── 31_grid_search_and_random_search.ipynb   # Exhaustive GridSearchCV vs budget-conscious RandomizedSearchCV
├── 32_pipelines.ipynb                       # Pipeline & ColumnTransformer, preventing data leakage
├── 33_model_persistence.ipynb               # Serializing trained estimators with joblib & version metadata
│
├── 34_scikit_learn_practice.ipynb           # 10 comprehensive multi-domain ML algorithmic challenges
└── 35_scikit_learn_mini_project.ipynb       # Capstone: Enterprise Customer Churn & Risk Predictive Pipeline
```

---

## 📚 Curriculum Index

| # | Notebook | Key ML Algorithms & APIs | Code Highlights & Techniques |
| :-: | :--- | :--- | :--- |
| **01** | [`01_scikit_learn_introduction.ipynb`](./01_scikit_learn_introduction.ipynb) | Estimator API, `fit`, `predict`, `score` | Unified API structure, fitting first KNN model, evaluating accuracy score |
| **02** | [`02_machine_learning_workflow.ipynb`](./02_machine_learning_workflow.ipynb) | 5-stage ML workflow, `StandardScaler`, `LogisticRegression` | End-to-end classification pipeline, train/val/test partitioning, metric reporting |
| **03** | [`03_loading_datasets.ipynb`](./03_loading_datasets.ipynb) | `load_iris`, `fetch_california_housing`, `make_classification` | Ingesting toy datasets as DataFrames, synthesizing custom multi-cluster data |
| **04** | [`04_features_and_labels.ipynb`](./04_features_and_labels.ipynb) | Feature matrix $X$ ($N \times P$), target vector $y$ | Continuous vs discrete targets, feature type auditing, label verification |
| **05** | [`05_train_test_split.ipynb`](./05_train_test_split.ipynb) | `train_test_split`, `stratify`, `shuffle` | Stratified splitting on imbalanced labels, deterministic seeding (`random_state`) |
| **06** | [`06_data_preprocessing.ipynb`](./06_data_preprocessing.ipynb) | Transformer API, `fit_transform`, `transform` | Data leakage prevention: fitting transformers strictly on training sets |
| **07** | [`07_handling_missing_values.ipynb`](./07_handling_missing_values.ipynb) | `SimpleImputer`, `KNNImputer` | Mean, median, most frequent imputation, multivariate KNN distance imputation |
| **08** | [`08_encoding_categorical_data.ipynb`](./08_encoding_categorical_data.ipynb) | `OneHotEncoder`, `OrdinalEncoder` | Sparse vs dense matrices, `handle_unknown='ignore'`, multi-category encoding |
| **09** | [`09_feature_scaling.ipynb`](./09_feature_scaling.ipynb) | `StandardScaler`, `MinMaxScaler`, `RobustScaler` | Z-score scaling, 0-1 normalization, outlier-robust median/IQR scaling |
| **10** | [`10_feature_selection.ipynb`](./10_feature_selection.ipynb) | `SelectKBest`, `f_classif`, `RFE`, `RandomForestClassifier` | Filter methods, ANOVA F-value ranking, Recursive Feature Elimination (RFE) |
| **11** | [`11_linear_regression.ipynb`](./11_linear_regression.ipynb) | `LinearRegression`, Ordinary Least Squares (OLS) | Slope `coef_`, intercept `intercept_`, $R^2$ computation, regression line plotting |
| **12** | [`12_multiple_linear_regression.ipynb`](./12_multiple_linear_regression.ipynb) | `Ridge` ($L_2$), `Lasso` ($L_1$), Multicollinearity | Shrinkage penalty tuning ($\alpha$), automatic feature pruning with Lasso zeros |
| **13** | [`13_polynomial_regression.ipynb`](./13_polynomial_regression.ipynb) | `PolynomialFeatures`, `make_pipeline` | Non-linear curve fitting, interaction terms, Bias-Variance tradeoff visualization |
| **14** | [`14_logistic_regression.ipynb`](./14_logistic_regression.ipynb) | `LogisticRegression`, Sigmoid function | Binary classification, probability extraction (`predict_proba`), threshold tuning |
| **15** | [`15_knn_classification.ipynb`](./15_knn_classification.ipynb) | `KNeighborsClassifier`, Euclidean distance | Hyperparameter search over $k$, odd vs even neighbors, feature scaling impact |
| **16** | [`16_decision_tree.ipynb`](./16_decision_tree.ipynb) | `DecisionTreeClassifier`, `plot_tree` | Gini impurity, tree depth pruning (`max_depth`), flowchart visualization |
| **17** | [`17_random_forest.ipynb`](./17_random_forest.ipynb) | `RandomForestClassifier`, Bagging | Out-of-bag (`oob_score_`) error, Gini feature importance bar chart |
| **18** | [`18_support_vector_machine.ipynb`](./18_support_vector_machine.ipynb) | `SVC`, Kernel trick (`'rbf'`, `'linear'`) | Margin maximization, support vector extraction, non-linear moon separation |
| **19** | [`19_naive_bayes.ipynb`](./19_naive_bayes.ipynb) | `GaussianNB`, Bayes' Theorem | Conditional independence assumption, continuous priors, fast single-pass training |
| **20** | [`20_gradient_boosting.ipynb`](./20_gradient_boosting.ipynb) | `GradientBoostingClassifier`, Boosting | Residual correction, shrinkage (`learning_rate`), deviance loss convergence plot |
| **21** | [`21_k_means_clustering.ipynb`](./21_k_means_clustering.ipynb) | `KMeans`, Inertia, `silhouette_score` | Unsupervised centroid partitioning, Elbow heuristic method, silhouette evaluation |
| **22** | [`22_hierarchical_clustering.ipynb`](./22_hierarchical_clustering.ipynb) | `AgglomerativeClustering`, `scipy.cluster.hierarchy` | Ward linkage, dendrogram visualization, distance threshold truncation |
| **23** | [`23_dbscan_clustering.ipynb`](./23_dbscan_clustering.ipynb) | `DBSCAN`, Core points, Border points | Arbitrary shape clustering, automatic noise detection (`label == -1`), eps tuning |
| **24** | [`24_pca_dimensionality_reduction.ipynb`](./24_pca_dimensionality_reduction.ipynb) | `PCA`, Singular Value Decomposition (SVD) | Scree plots, cumulative explained variance ratio, 2D latent space projection |
| **25** | [`25_model_evaluation.ipynb`](./25_model_evaluation.ipynb) | Train vs Test error, Overfitting vs Underfitting | Learning curves, detecting generalization gap between training and validation |
| **26** | [`26_confusion_matrix.ipynb`](./26_confusion_matrix.ipynb) | `confusion_matrix`, `ConfusionMatrixDisplay` | True Positive, False Positive, Type I & Type II error analysis, heatmap plots |
| **27** | [`27_classification_metrics.ipynb`](./27_classification_metrics.ipynb) | `classification_report`, `roc_auc_score`, `RocCurveDisplay` | Precision-Recall tradeoff, F1 harmonic mean, ROC curves, optimal cutoff threshold |
| **28** | [`28_regression_metrics.ipynb`](./28_regression_metrics.ipynb) | `mean_squared_error`, `mean_absolute_error`, $R^2$ | RMSE, MAE, residual distribution plots, heteroscedasticity diagnosis |
| **29** | [`29_cross_validation.ipynb`](./29_cross_validation.ipynb) | `KFold`, `StratifiedKFold`, `cross_val_score` | 5-fold cross-validation, variance reduction across splits, scoring parameter |
| **30** | [`30_hyperparameter_tuning.ipynb`](./30_hyperparameter_tuning.ipynb) | `validation_curve`, Bias vs Variance | Visualizing model complexity curves across regularization hyperparameter ranges |
| **31** | [`31_grid_search_and_random_search.ipynb`](./31_grid_search_and_random_search.ipynb) | `GridSearchCV`, `RandomizedSearchCV` | Multi-parameter grid combinatorial search vs budget-friendly randomized sampling |
| **32** | [`32_pipelines.ipynb`](./32_pipelines.ipynb) | `Pipeline`, `ColumnTransformer`, `StandardScaler` | Assembling heterogeneous feature pipelines (numerical + categorical) with zero leakage |
| **33** | [`33_model_persistence.ipynb`](./33_model_persistence.ipynb) | `joblib.dump`, `joblib.load` | Serializing entire trained pipelines to `.joblib` files, mock production inference |
| **34** | [`34_scikit_learn_practice.ipynb`](./34_scikit_learn_practice.ipynb) | 10 Comprehensive Problem Sets | Regression, classification, clustering, PCA, and hyperparameter tuning challenges |
| **35** | [`35_scikit_learn_mini_project.ipynb`](./35_scikit_learn_mini_project.ipynb) | **Capstone: Enterprise Churn & Risk Pipeline** | End-to-end customer churn prediction pipeline, SMOTE/imbalance, model benchmarking, production bundle |

---

## 🎯 Capstone Project Spotlight

### **Enterprise Customer Churn & Lifetime Risk Predictive Pipeline**
📁 **Notebook:** [`35_scikit_learn_mini_project.ipynb`](./35_scikit_learn_mini_project.ipynb)  
🛠️ **Tech Stack:** Scikit-Learn 1.2+, NumPy, Pandas, Matplotlib, Joblib  

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│              ENTERPRISE CUSTOMER CHURN PREDICTIVE ARCHITECTURE PIPELINE                │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   RAW TABULAR INGESTION ──▶ DATA CLEANING & LEAK-FREE SPLITTING ──▶ COLUMNTRANSFORMER  │
│   [5,000 Customers, 12 Feats]   [Stratified 80/20 Train-Test]     [Num: RobustScaler   │
│                                                                    Cat: OneHotEncoder] │
│                                                                             │          │
│                                                                             ▼          │
│   PRODUCTION JOBPERSIST ◀── MODEL SELECTION & TUNING ◀── MULTI-MODEL BENCHMARKING      │
│   [Serialized .joblib Bundle]   [RandomizedSearchCV on RF]   [Logistic, RF, GradientBoost]
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

#### Key Engineering Highlights:
1. **Realistic Enterprise Dataset**: Synthesizes 5,000 enterprise telecom/SaaS customer accounts featuring realistic tenure, monthly charges, contract types, customer support inquiries, payment methods, and an imbalanced ~24% churn rate.
2. **Leakage-Free Preprocessing with `ColumnTransformer`**: Combines `RobustScaler` (to handle outliers in charges and usage) and `OneHotEncoder(handle_unknown='ignore')` into an integrated transformer, fit strictly on the training partition.
3. **Multi-Model Tournament**: Benchmarks three distinct model families:
   - Baseline: `LogisticRegression` with balanced class weights
   - Bagging Ensemble: `RandomForestClassifier` with Gini impurity
   - Sequential Boosting: `GradientBoostingClassifier` with learning rate shrinkage
4. **Comprehensive Evaluation**: Generates side-by-side Confusion Matrices, ROC Curves ($AUC \approx 0.88$), and Precision-Recall Curves to optimize decision thresholds for business cost-benefit trade-offs.
5. **Hyperparameter Optimization**: Conducts `RandomizedSearchCV` across tree depth, number of estimators, and leaf sample splits with 5-fold Stratified Cross-Validation.
6. **Feature Importance Interpretation**: Extracts and plots the top 10 churn drivers, identifying contract type and customer support tickets as primary early warning indicators.
7. **Production Model Persistence**: Exports the final trained pipeline bundle to disk using `joblib`, verifying round-trip inference on unseen customer records.

---

## 💡 Scikit-Learn Production Best Practices

```python
# 1. ALWAYS prevent data leakage using ColumnTransformer & Pipeline
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier

num_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

cat_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

preprocessor = ColumnTransformer([
    ('num', num_pipe, ['tenure', 'monthly_charges', 'total_charges']),
    ('cat', cat_pipe, ['contract_type', 'payment_method'])
])

# 2. Bundle preprocessing and estimator into one deployable unit
full_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# 3. Fit strictly on training data
full_pipeline.fit(X_train, y_train)

# 4. Predict directly on raw test features with zero manual transformations
y_pred = full_pipeline.predict(X_test)
```

---

## 🚀 Getting Started & Execution

### Prerequisites
Ensure your Python environment is set up with Scikit-learn, NumPy, Pandas, Matplotlib, and Jupyter:

```bash
# Clone the repository
git clone https://github.com/VIJAYAPANDIANT/AI-ML-Learning.git
cd AI-ML-Learning/Scikit-learn

# Activate your virtual environment
# Windows:
..\venv\Scripts\Activate.ps1
# macOS/Linux:
source ../venv/bin/activate

# Install required dependencies
pip install scikit-learn numpy pandas matplotlib joblib jupyter
```

### Launching the Curriculum
```bash
# Launch JupyterLab
jupyter lab

# Or launch traditional Jupyter Notebook
jupyter notebook
```

---

<div align="center">
  <b>Explore Next:</b> <a href="../Python/">🐍 Python</a> • <a href="../Numpy/">🔢 NumPy</a> • <a href="../Pandas/">📊 Pandas</a> • <a href="../Matplotlib/">📈 Matplotlib</a> • <a href="../Seaborn/">📊 Seaborn</a>
</div>
