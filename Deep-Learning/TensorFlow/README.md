<div align="center">

# 🟧 TensorFlow & Keras for Deep Learning

### *A Production-Grade 13-Notebook Masterclass: From Eager Execution & Tensors to CNNs, LSTMs & Diagnostic Imaging*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.12%2B-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org/)
[![Curriculum](https://img.shields.io/badge/Curriculum-13%20Notebooks-blueviolet?style=for-the-badge&logo=gitbook&logoColor=white)](#-curriculum-index)
[![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)](#-curriculum-index)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](../../#--license)

<br/>

<p align="center">
  <b>13 Interactive Notebooks</b> • <b>Sequential & Functional APIs</b> • <b>EarlyStopping Callbacks</b> • <b>Medical Imaging Capstone</b>
</p>

<p align="center">
  <a href="../../"><b>🏠 Main Repository</b></a> •
  <a href="../"><b>🧠 Deep Learning Master</b></a> •
  <a href="../PyTorch/"><b>🔥 PyTorch Module</b></a> •
  <a href="#-curriculum-index"><b>📚 Curriculum Index</b></a> •
  <a href="#-capstone-project-spotlight"><b>🩺 Capstone Project</b></a>
</p>

</div>

---

## 📖 Module Overview

**TensorFlow 2.x** with integrated **Keras** is an industry standard platform for building, training, and deploying scalable deep learning models. Combining intuitive high-level abstractions with low-level execution control, TensorFlow powers mission-critical deployments across mobile, edge, browser, and enterprise cloud servers.

### Key Capabilities Covered:
- **TensorFlow Eager Execution**: Immediate imperative evaluation, automatic hardware GPU/TPU placement.
- **Tensors & Variables**: Creating immutable constants and mutable stateful weight variables (`tf.Variable`).
- **Keras Modeling Paradigms**: Stacking layers linearly with `Sequential` or crafting residual multi-branch networks with the `Functional API`.
- **Training Lifecycle**: Compilation, loss metrics, early stopping callbacks, learning rate schedules, and native `.keras` persistence.
- **Computer Vision & Sequence Modeling**: Convolutional architectures (`Conv2D`, `MaxPooling2D`) and recurrent time-series (`LSTM`).

---

## 📚 Curriculum Index

| # | Notebook | Core Topics & Capabilities Covered | Status |
| :-: | :--- | :--- | :-: |
| **01** | [`01_tensorflow_introduction.ipynb`](./01_tensorflow_introduction.ipynb) | TF 2.x eager execution, GPU detection, CUDA acceleration verification | Completed ✅ |
| **02** | [`02_tensorflow_tensors.ipynb`](./02_tensorflow_tensors.ipynb) | Constants, Variables (`tf.Variable`), rank inspection, in-place weight mutations | Completed ✅ |
| **03** | [`03_tensorflow_operations.ipynb`](./03_tensorflow_operations.ipynb) | Matrix multiplication (`tf.matmul`), broadcasting rules, reduction operators | Completed ✅ |
| **04** | [`04_keras_sequential_api.ipynb`](./04_keras_sequential_api.ipynb) | `Sequential` model stacking, `Dense`, `Dropout`, model architecture inspection | Completed ✅ |
| **05** | [`05_building_neural_networks.ipynb`](./05_building_neural_networks.ipynb) | Keras Functional API, multi-branch routing, residual skip connections (`layers.add`) | Completed ✅ |
| **06** | [`06_model_training.ipynb`](./06_model_training.ipynb) | Compilation (`compile`), Adam optimizer, loss objectives, `model.fit()`, loss curves | Completed ✅ |
| **07** | [`07_model_evaluation.ipynb`](./07_model_evaluation.ipynb) | Holdout testing with `model.evaluate()`, ROC-AUC scoring, accuracy validation | Completed ✅ |
| **08** | [`08_model_prediction.ipynb`](./08_model_prediction.ipynb) | Inference with `model.predict()`, probability thresholding, class argmax decoding | Completed ✅ |
| **09** | [`09_callbacks_and_early_stopping.ipynb`](./09_callbacks_and_early_stopping.ipynb) | `EarlyStopping(restore_best_weights=True)`, `ReduceLROnPlateau`, checkpoints | Completed ✅ |
| **10** | [`10_model_saving_and_loading.ipynb`](./10_model_saving_and_loading.ipynb) | Native `.keras` archive serialization, reloading models & zero-inference-gap checks | Completed ✅ |
| **11** | [`11_cnn_image_classification.ipynb`](./11_cnn_image_classification.ipynb) | 2D Spatial convolutions (`Conv2D`), `MaxPooling2D`, padding, receptive fields | Completed ✅ |
| **12** | [`12_rnn_and_lstm.ipynb`](./12_rnn_and_lstm.ipynb) | Recurrent architectures, `LSTM` gating, sequence forecasting, multi-layer stacking | Completed ✅ |
| **13** | [`13_tensorflow_mini_project.ipynb`](./13_tensorflow_mini_project.ipynb) | **Capstone: Medical Diagnostic Imaging Classifier** (Chest X-Ray Pneumonia Detection) | Completed ✅ |

---

## 🎯 Capstone Project Spotlight

### **Automated Medical Diagnostic Imaging Classifier**
📁 **Notebook:** [`13_tensorflow_mini_project.ipynb`](./13_tensorflow_mini_project.ipynb)  
🛠️ **Tech Stack:** TensorFlow 2.x, Keras, NumPy, Scikit-Learn  

- **Domain**: Automated pulmonary disease diagnosis (Chest X-Ray Pneumonia Detection).
- **Architecture**: Deep Convolutional Neural Network with Batch Normalization, spatial max pooling, dropout regularization, and a Sigmoid decision head.
- **Key Deliverables**: Automated training with EarlyStopping, ROC-AUC metric tracking, and persistent production export to native `.keras` format for clinical decision support.

---

<div align="center">
  <b>Explore Next:</b> <a href="../PyTorch/">🔥 PyTorch Module</a> • <a href="../Advanced-Deep-Learning/">⚡ Advanced Deep Learning</a> • <a href="../Projects/">🏆 Portfolio Projects</a>
</div>
