<div align="center">

# 🔥 PyTorch Deep Learning Masterclass

### *A Production-Grade 13-Notebook Masterclass: Dynamic Tensors, Autograd, Custom Datasets, Explicit Training Loops & TorchScript*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Curriculum](https://img.shields.io/badge/Curriculum-13%20Notebooks-blueviolet?style=for-the-badge&logo=gitbook&logoColor=white)](#-curriculum-index)
[![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)](#-curriculum-index)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](../../#--license)

<br/>

<p align="center">
  <b>13 Interactive Notebooks</b> • <b>Reverse-Mode Autodiff</b> • <b>OOP nn.Module</b> • <b>Industrial Anomaly Autoencoder Capstone</b>
</p>

<p align="center">
  <a href="../../"><b>🏠 Main Repository</b></a> •
  <a href="../"><b>🧠 Deep Learning Master</b></a> •
  <a href="../TensorFlow/"><b>🟧 TensorFlow Module</b></a> •
  <a href="#-curriculum-index"><b>📚 Curriculum Index</b></a> •
  <a href="#-capstone-project-spotlight"><b>⚙️ Capstone Project</b></a>
</p>

</div>

---

## 📖 Module Overview

**PyTorch** is the primary deep learning framework powering modern artificial intelligence research, large language models (LLMs), and cutting-edge production systems. Built around **Define-by-Run dynamic computational graphs**, PyTorch offers unparalleled developer ergonomics, native Python debugging, and effortless CUDA acceleration.

### Key Capabilities Covered:
- **PyTorch Tensors**: Dynamic allocation, device management (`.to(device)`), zero-copy NumPy memory bridging.
- **Autograd Engine**: Automatic reverse-mode differentiation across computational DAGs with `.backward()`.
- **Data Engineering**: Decoupled `Dataset` implementations paired with high-throughput multi-worker `DataLoader` pipelines.
- **Object-Oriented Modeling**: Subclassing `torch.nn.Module`, parameter registration, and custom forward computation.
- **Explicit Training Loop Discipline**: Complete mastery over the canonical 5-step loop (`zero_grad`, `forward`, `loss`, `backward`, `step`).
- **Production Compilation**: Serialization of model state dictionaries and JIT tracing with TorchScript (`torch.jit.trace`).

---

## 📚 Curriculum Index

| # | Notebook | Core Topics & Capabilities Covered | Status |
| :-: | :--- | :--- | :-: |
| **01** | [`01_pytorch_introduction.ipynb`](./01_pytorch_introduction.ipynb) | PyTorch ecosystem, dynamic graphs, CUDA GPU detection & memory inspection | Completed ✅ |
| **02** | [`02_pytorch_tensors.ipynb`](./02_pytorch_tensors.ipynb) | Tensor instantiation, dtypes, device allocation, zero-copy NumPy bridge (`from_numpy`) | Completed ✅ |
| **03** | [`03_tensor_operations.ipynb`](./03_tensor_operations.ipynb) | Tensor slicing, view vs reshape, matrix multiplications (`@`), broadcasting rules | Completed ✅ |
| **04** | [`04_autograd_and_gradients.ipynb`](./04_autograd_and_gradients.ipynb) | Autograd engine, computational DAG, `.backward()`, gradient accumulation mechanics | Completed ✅ |
| **05** | [`05_datasets_and_dataloaders.ipynb`](./05_datasets_and_dataloaders.ipynb) | Custom `Dataset` subclassing (`__len__`, `__getitem__`), multi-worker `DataLoader` | Completed ✅ |
| **06** | [`06_building_neural_networks.ipynb`](./06_building_neural_networks.ipynb) | Subclassing `nn.Module`, parameter registration, multi-layer MLP architectures | Completed ✅ |
| **07** | [`07_loss_functions.ipynb`](./07_loss_functions.ipynb) | `nn.CrossEntropyLoss` (LogSoftmax + NLL), `nn.BCEWithLogitsLoss` stability | Completed ✅ |
| **08** | [`08_optimizers.ipynb`](./08_optimizers.ipynb) | `torch.optim` (SGD, Adam, AdamW decoupled decay), learning rate schedulers | Completed ✅ |
| **09** | [`09_training_neural_networks.ipynb`](./09_training_neural_networks.ipynb) | The canonical 5-step PyTorch training loop, batch loss tracking, epoch reductions | Completed ✅ |
| **10** | [`10_model_evaluation.ipynb`](./10_model_evaluation.ipynb) | `model.eval()`, `torch.no_grad()` memory management, accuracy and confusion reporting | Completed ✅ |
| **11** | [`11_cnn_image_classification.ipynb`](./11_cnn_image_classification.ipynb) | NCHW Computer Vision, `nn.Conv2d`, `nn.BatchNorm2d`, `nn.MaxPool2d`, dense classifier | Completed ✅ |
| **12** | [`12_rnn_and_lstm.ipynb`](./12_rnn_and_lstm.ipynb) | Recurrent sequence modeling, `nn.LSTM(batch_first=True, bidirectional=True)`, hidden states | Completed ✅ |
| **13** | [`13_pytorch_mini_project.ipynb`](./13_pytorch_mini_project.ipynb) | **Capstone: Industrial Vibration Acoustic Anomaly Autoencoder** & TorchScript Compilation | Completed ✅ |

---

## 🎯 Capstone Project Spotlight

### **Industrial Machinery Acoustic Vibration Anomaly Autoencoder**
📁 **Notebook:** [`13_pytorch_mini_project.ipynb`](./13_pytorch_mini_project.ipynb)  
🛠️ **Tech Stack:** PyTorch 2.0+, Autograd, TorchScript, NumPy  

- **Domain**: Predictive maintenance & unsupervised vibration telemetry anomaly detection.
- **Architecture**: Deep Residual Autoencoder trained exclusively on healthy baseline telemetry to learn an informational bottleneck.
- **Key Deliverables**: Reconstruction error thresholding providing $>4\times$ anomalous separation ratio, followed by TorchScript (`torch.jit.trace`) compilation for low-latency edge deployment.

---

<div align="center">
  <b>Explore Next:</b> <a href="../TensorFlow/">🟧 TensorFlow Module</a> • <a href="../Advanced-Deep-Learning/">⚡ Advanced Deep Learning</a> • <a href="../Projects/">🏆 Portfolio Projects</a>
</div>
