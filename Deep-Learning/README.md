<div align="center">

# 🧠 Deep Learning Masterclass: From Fundamentals to Production PyTorch & TensorFlow

### *A Production-Grade 52-Notebook Masterclass: Mathematical Foundations, TensorFlow/Keras, PyTorch, Advanced Transformers, and Multi-Modal AI Projects*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.12%2B-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org/)
[![Curriculum](https://img.shields.io/badge/Curriculum-52%20Notebooks-7928CA?style=for-the-badge&logo=gitbook&logoColor=white)](#-master-curriculum-index)
[![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)](#-master-curriculum-index)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](../#--license)

<br/>

<p align="center">
  <b>52 Interactive Notebooks</b> • <b>First-Principles Mathematics</b> • <b>TensorFlow & Keras</b> • <b>PyTorch Ecosystem</b> • <b>Multi-Modal AI Capstone</b>
</p>

<p align="center">
  <a href="../"><b>🏠 Main Repository</b></a> •
  <a href="#1--deep-learning-fundamentals-12-notebooks"><b>🔬 Fundamentals (12)</b></a> •
  <a href="./TensorFlow/"><b>🟧 TensorFlow (13)</b></a> •
  <a href="./PyTorch/"><b>🔥 PyTorch (13)</b></a> •
  <a href="#4--advanced-deep-learning-architectures-9-notebooks"><b>⚡ Advanced (9)</b></a> •
  <a href="#5--real-world-portfolio-projects-5-notebooks"><b>🏆 Projects (5)</b></a>
</p>

</div>

---

## 📖 Module Overview

While classical machine learning relies heavily on manual feature engineering and domain heuristics, **Deep Learning** learns hierarchical, end-to-end mathematical representations directly from raw perceptual data (pixels, audio waveforms, text tokens, tabular states).

This curriculum delivers an industry-standard **52-Notebook Deep Learning Masterclass** structured into 5 cohesive phases:
1. **Mathematical & Algorithmic Foundations (12 Notebooks)**: Biological vs artificial neurons, Perceptron learning dynamics, non-linear activations, computational graphs, forward propagation, loss surfaces, numerical & analytical gradient descent, backpropagation via the chain rule, and modern optimizers.
2. **TensorFlow & Keras Masterclass (13 Notebooks)**: Eager execution, tensor manipulation, Sequential and Functional APIs, model training, custom callbacks, model persistence, CNNs, and sequence LSTMs.
3. **PyTorch Deep Dive (13 Notebooks)**: Dynamic computational graphs (Define-by-Run), Autograd reverse-mode autodiff, `Dataset` & `DataLoader` pipelines, `nn.Module` object-oriented modeling, training loops, and TorchScript deployment.
4. **Advanced Architectures (9 Notebooks)**: Modern CNN backbones (ResNet, MobileNet), BPTT gradient bottlenecks in RNNs, LSTMs vs GRUs, transfer learning fine-tuning, bottleneck Autoencoders, Scaled Dot-Product Attention ($Q, K, V$), Transformers, and GPU acceleration with mixed precision.
5. **Real-World Portfolio Projects (5 Notebooks)**: MNIST Digit Recognition, CIFAR-10 Color Image Classification, Real-World Cats vs. Dogs Transfer Learning, NLP Sentiment Analysis with BiLSTM, and the Autonomous Multi-Modal Diagnostic & Predictive Intelligence Capstone.

---

## 📁 Repository & Directory Structure

```text
Deep-Learning/
│
├── README.md                                # Master Deep Learning Module guide & index
│
├── 01_deep_learning_introduction.ipynb       # Introduction to representation learning & data scaling
├── 02_machine_learning_vs_deep_learning.ipynb # Classical ML vs Deep Learning trade-offs & benchmarks
├── 03_neural_network_fundamentals.ipynb      # Feedforward topology, weight matrices & biases
├── 04_biological_neuron_and_artificial_neuron.ipynb # Biological soma/synapse vs artificial neuron models
├── 05_perceptron.ipynb                       # Rosenblatt Perceptron, update rules & the XOR limitation
├── 06_activation_functions.ipynb             # Sigmoid, Tanh, ReLU, Leaky ReLU, Softmax & saturation
├── 07_forward_propagation.ipynb              # Forward affine transformations & activation caching
├── 08_loss_functions.ipynb                   # MSE, Binary Cross-Entropy, Categorical Cross-Entropy
├── 09_gradient_descent.ipynb                 # Batch, Stochastic (SGD) & Mini-Batch Gradient Descent
├── 10_backpropagation.ipynb                  # Calculus chain rule derivation & gradient computation
├── 11_optimizers.ipynb                       # Momentum, RMSprop, and Adam adaptive second moments
├── 12_epochs_batches_and_iterations.ipynb    # Mini-batch partitioning, steps per epoch & batch sizing
│
├── TensorFlow/                              # [13 NOTEBOOKS] Google TensorFlow 2.x & Keras
│   ├── README.md                            # Dedicated TensorFlow/Keras guide & index
│   ├── 01_tensorflow_introduction.ipynb     # TensorFlow 2.x eager execution & ecosystem
│   ├── 02_tensorflow_tensors.ipynb          # Constants, Variables, ranks, and shapes
│   ├── 03_tensorflow_operations.ipynb       # Matrix multiplication, broadcasting & reductions
│   ├── 04_keras_sequential_api.ipynb        # Stacking Dense and Dropout layers
│   ├── 05_building_neural_networks.ipynb     # Functional API, multi-input/output & skip connections
│   ├── 06_model_training.ipynb              # Compilation (optimizer, loss, metrics) & model.fit()
│   ├── 07_model_evaluation.ipynb            # Holdout evaluation, test loss & ROC-AUC analysis
│   ├── 08_model_prediction.ipynb            # Inference, probability thresholding & class extraction
│   ├── 09_callbacks_and_early_stopping.ipynb # EarlyStopping, ReduceLROnPlateau & Checkpoints
│   ├── 10_model_saving_and_loading.ipynb    # Native .keras format serialization & reloading
│   ├── 11_cnn_image_classification.ipynb    # Conv2D, MaxPooling2D, padding & receptive fields
│   ├── 12_rnn_and_lstm.ipynb                # SimpleRNN, LSTM gates & sequence forecasting
│   └── 13_tensorflow_mini_project.ipynb     # Capstone: Medical Diagnostic Imaging Classifier
│
├── PyTorch/                                 # [13 NOTEBOOKS] Meta PyTorch Dynamic Framework
│   ├── README.md                            # Dedicated PyTorch guide & index
│   ├── 01_pytorch_introduction.ipynb        # PyTorch ecosystem, dynamic graphs & CUDA devices
│   ├── 02_pytorch_tensors.ipynb             # Creation, dtypes, device allocation & NumPy bridge
│   ├── 03_tensor_operations.ipynb           # Slicing, reshaping, views, matrix multiplications
│   ├── 04_autograd_and_gradients.ipynb      # Autograd engine, computational DAG & .backward()
│   ├── 05_datasets_and_dataloaders.ipynb    # Custom Dataset class & multi-threaded DataLoader
│   ├── 06_building_neural_networks.ipynb     # Subclassing nn.Module, layers & forward pass
│   ├── 07_loss_functions.ipynb              # nn.CrossEntropyLoss, nn.BCEWithLogitsLoss & stability
│   ├── 08_optimizers.ipynb                  # torch.optim (SGD, Adam, AdamW) & LR schedulers
│   ├── 09_training_neural_networks.ipynb    # The canonical 5-step PyTorch training loop
│   ├── 10_model_evaluation.ipynb            # model.eval(), torch.no_grad() & validation metrics
│   ├── 11_cnn_image_classification.ipynb    # nn.Conv2d (NCHW format), nn.MaxPool2d & flattening
│   ├── 12_rnn_and_lstm.ipynb                # nn.LSTM, nn.GRU, bidirectional context & hidden states
│   └── 13_pytorch_mini_project.ipynb        # Capstone: Acoustic Machinery Anomaly Autoencoder
│
├── Advanced-Deep-Learning/                  # [9 NOTEBOOKS] Cutting-Edge Architectures
│   ├── 01_convolutional_neural_networks.ipynb # ResNet skip highways & 1x1 bottleneck convolutions
│   ├── 02_recurrent_neural_networks.ipynb   # BPTT mathematical analysis & gradient vanishing
│   ├── 03_lstm_and_gru.ipynb                # Gate mechanics & parameter efficiency comparison
│   ├── 04_transfer_learning.ipynb           # Backbone freezing, fine-tuning & catastrophic forgetting
│   ├── 05_autoencoders.ipynb                # Unsupervised representation learning & bottleneck latent
│   ├── 06_attention_mechanism.ipynb         # Scaled Dot-Product Attention: Query, Key, Value
│   ├── 07_transformers_introduction.ipynb   # Multi-Head Attention, Positional Encodings & FFNs
│   ├── 08_gpu_training.ipynb                # CUDA memory allocation, AMP mixed precision & DDP
│   └── 09_model_regularization.ipynb        # Dropout, BatchNorm, Weight Decay, Augmentation
│
└── Projects/                                # [5 NOTEBOOKS] End-to-End Real-World AI Systems
    ├── 01_handwritten_digit_recognition.ipynb # MNIST Handwritten Digit Recognition ConvNet
    ├── 02_image_classification.ipynb        # CIFAR-10 Multi-Class RGB Image Classifier with GAP
    ├── 03_cats_vs_dogs_classification.ipynb # Real-World Binary Classification with Data Augmentation
    ├── 04_sentiment_analysis.ipynb          # NLP Review Sentiment Analysis with Embeddings & BiLSTM
    └── 05_deep_learning_final_project.ipynb # Master Capstone: Autonomous Multi-Modal Intelligence Suite
```

---

## 📚 Master Curriculum Index

### 1. 🔬 Deep Learning Fundamentals (12 Notebooks)

| # | Notebook | Core Deep Learning Mechanics | Code Highlights & First Principles |
| :-: | :--- | :--- | :--- |
| **01** | [`01_deep_learning_introduction.ipynb`](./01_deep_learning_introduction.ipynb) | Representation learning paradigm | Data scaling comparison curve (Classical ML vs Deep Learning) |
| **02** | [`02_machine_learning_vs_deep_learning.ipynb`](./02_machine_learning_vs_deep_learning.ipynb) | Feature engineering vs end-to-end | Systematic tabular comparison of capacity, hardware, and modalities |
| **03** | [`03_neural_network_fundamentals.ipynb`](./03_neural_network_fundamentals.ipynb) | Multilayer Perceptron topology | Xavier/Glorot weight initialization, layer dimensions & param count |
| **04** | [`04_biological_neuron_and_artificial_neuron.ipynb`](./04_biological_neuron_and_artificial_neuron.ipynb) | Dendrites, synapses, soma, axon | Single-neuron mathematical forward function with thresholding |
| **05** | [`05_perceptron.ipynb`](./05_perceptron.ipynb) | Rosenblatt Perceptron learning rule | Pure Python Perceptron class, solving AND gate, XOR failure analysis |
| **06** | [`06_activation_functions.ipynb`](./06_activation_functions.ipynb) | Non-linear mappings & gradients | Sigmoid, Tanh, ReLU, Leaky ReLU comparative plots, stable Softmax |
| **07** | [`07_forward_propagation.ipynb`](./07_forward_propagation.ipynb) | Computational graph execution | Multi-sample batch forward pass, intermediate activation caching |
| **08** | [`08_loss_functions.ipynb`](./08_loss_functions.ipynb) | Cost optimization objectives | Mean Squared Error (MSE), Binary Cross-Entropy with clipping |
| **09** | [`09_gradient_descent.ipynb`](./09_gradient_descent.ipynb) | Gradient descent optimization | Numerical tracking of convergence trajectory on parabolic surfaces |
| **10** | [`10_backpropagation.ipynb`](./10_backpropagation.ipynb) | Multivariate calculus chain rule | 2-layer backpropagation derived and implemented from scratch |
| **11** | [`11_optimizers.ipynb`](./11_optimizers.ipynb) | Adaptive learning rates & momentum | Implementation of the complete Adam optimizer with bias correction |
| **12** | [`12_epochs_batches_and_iterations.ipynb`](./12_epochs_batches_and_iterations.ipynb) | Mini-batch training mechanics | Generator-based batch partitioning, epoch calculation, shuffling |

---

### 2. 🟧 Google TensorFlow & Keras (13 Notebooks)

> **Dedicated Module Guide:** [`TensorFlow/README.md`](./TensorFlow/README.md)

| # | Notebook | Core TensorFlow Capabilities | Code Highlights & APIs |
| :-: | :--- | :--- | :--- |
| **01** | [`01_tensorflow_introduction.ipynb`](./TensorFlow/01_tensorflow_introduction.ipynb) | Eager execution & GPU detection | Checking CUDA acceleration, GPU physical devices |
| **02** | [`02_tensorflow_tensors.ipynb`](./TensorFlow/02_tensorflow_tensors.ipynb) | Tensors, Constants & Variables | `tf.constant`, `tf.Variable`, in-place mutations with `assign_add` |
| **03** | [`03_tensorflow_operations.ipynb`](./TensorFlow/03_tensorflow_operations.ipynb) | Vectorized tensor math | `tf.matmul` (`@`), broadcasting, reductions (`reduce_mean`, `reduce_sum`) |
| **04** | [`04_keras_sequential_api.ipynb`](./TensorFlow/04_keras_sequential_api.ipynb) | Keras Sequential API | Linear layer stacking, `Dense`, `Dropout`, model architecture summary |
| **05** | [`05_building_neural_networks.ipynb`](./TensorFlow/05_building_neural_networks.ipynb) | Functional API & Skip Connections | Multi-branch routing, residual skip addition (`layers.add`) |
| **06** | [`06_model_training.ipynb`](./TensorFlow/06_model_training.ipynb) | Compilation & Training | `compile(optimizer, loss, metrics)`, `model.fit()`, loss curves |
| **07** | [`07_model_evaluation.ipynb`](./TensorFlow/07_model_evaluation.ipynb) | Generalization assessment | `model.evaluate()`, ROC-AUC scoring, holdout validation |
| **08** | [`08_model_prediction.ipynb`](./TensorFlow/08_model_prediction.ipynb) | Production inference | `model.predict()`, probability thresholding, class argmax |
| **09** | [`09_callbacks_and_early_stopping.ipynb`](./TensorFlow/09_callbacks_and_early_stopping.ipynb) | Dynamic training callbacks | `EarlyStopping(restore_best_weights=True)`, `ReduceLROnPlateau` |
| **10** | [`10_model_saving_and_loading.ipynb`](./TensorFlow/10_model_saving_and_loading.ipynb) | Model serialization | Native `.keras` archive persistence, full weight and graph reload |
| **11** | [`11_cnn_image_classification.ipynb`](./TensorFlow/11_cnn_image_classification.ipynb) | Spatial Computer Vision | `Conv2D`, `MaxPooling2D`, filter feature maps, spatial downsampling |
| **12** | [`12_rnn_and_lstm.ipynb`](./TensorFlow/12_rnn_and_lstm.ipynb) | Sequential Time-Series | `layers.LSTM`, `return_sequences=True`, multi-layer recurrent nets |
| **13** | [`13_tensorflow_mini_project.ipynb`](./TensorFlow/13_tensorflow_mini_project.ipynb) | **Capstone: Medical Diagnostic Classifier** | Deep ConvNet for automated Pneumonia vs Normal Chest X-Ray detection |

---

### 3. 🔥 Meta PyTorch Ecosystem (13 Notebooks)

> **Dedicated Module Guide:** [`PyTorch/README.md`](./PyTorch/README.md)

| # | Notebook | Core PyTorch Capabilities | Code Highlights & APIs |
| :-: | :--- | :--- | :--- |
| **01** | [`01_pytorch_introduction.ipynb`](./PyTorch/01_pytorch_introduction.ipynb) | Ecosystem & Device Management | `torch.device('cuda')`, GPU memory inspection, dynamic graphs |
| **02** | [`02_pytorch_tensors.ipynb`](./PyTorch/02_pytorch_tensors.ipynb) | PyTorch Tensor Primitives | Tensor allocation, zero-copy memory bridge with NumPy (`from_numpy`) |
| **03** | [`03_tensor_operations.ipynb`](./PyTorch/03_tensor_operations.ipynb) | Mathematical Tensor Routines | Slicing, view vs reshape, matrix product (`@`), broadcasting |
| **04** | [`04_autograd_and_gradients.ipynb`](./PyTorch/04_autograd_and_gradients.ipynb) | Reverse-Mode Autodiff Engine | `requires_grad=True`, computational DAG, `backward()`, gradient accumulation |
| **05** | [`05_datasets_and_dataloaders.ipynb`](./PyTorch/05_datasets_and_dataloaders.ipynb) | Data Pipeline Primitives | Custom `Dataset` subclass (`__len__`, `__getitem__`), multi-worker `DataLoader` |
| **06** | [`06_building_neural_networks.ipynb`](./PyTorch/06_building_neural_networks.ipynb) | Object-Oriented Modeling | Subclassing `nn.Module`, parameter registration, `forward()` execution |
| **07** | [`07_loss_functions.ipynb`](./PyTorch/07_loss_functions.ipynb) | Numerically Stable Objectives | `nn.CrossEntropyLoss` (LogSoftmax + NLL), `nn.BCEWithLogitsLoss` |
| **08** | [`08_optimizers.ipynb`](./PyTorch/08_optimizers.ipynb) | Advanced Optimizers & Schedules | `optim.AdamW`, decoupled weight decay, `StepLR`, `CosineAnnealingLR` |
| **09** | [`09_training_neural_networks.ipynb`](./PyTorch/09_training_neural_networks.ipynb) | Explicit 5-Step Training Loop | `zero_grad()`, `forward`, `loss`, `backward()`, `optimizer.step()` |
| **10** | [`10_model_evaluation.ipynb`](./PyTorch/10_model_evaluation.ipynb) | Inference & Metrics | `model.eval()`, `torch.no_grad()` memory saving, classification accuracy |
| **11** | [`11_cnn_image_classification.ipynb`](./PyTorch/11_cnn_image_classification.ipynb) | NCHW Computer Vision | `nn.Conv2d`, `nn.BatchNorm2d`, `nn.MaxPool2d`, linear classification head |
| **12** | [`12_rnn_and_lstm.ipynb`](./PyTorch/12_rnn_and_lstm.ipynb) | Recurrent Sequence Models | `nn.LSTM(batch_first=True, bidirectional=True)`, hidden state handling |
| **13** | [`13_pytorch_mini_project.ipynb`](./PyTorch/13_pytorch_mini_project.ipynb) | **Capstone: Acoustic Anomaly Detector** | Deep Residual Autoencoder for industrial vibration telemetry & TorchScript |

---

### 4. ⚡ Advanced Deep Learning Architectures (9 Notebooks)

| # | Notebook | Advanced Architectural Concepts | Implementation Highlights |
| :-: | :--- | :--- | :--- |
| **01** | [`01_convolutional_neural_networks.ipynb`](./Advanced-Deep-Learning/01_convolutional_neural_networks.ipynb) | Modern ConvNet Evolution | $3 \times 3$ receptive field stacking vs $7 \times 7$, 1x1 bottleneck reductions |
| **02** | [`02_recurrent_neural_networks.ipynb`](./Advanced-Deep-Learning/02_recurrent_neural_networks.ipynb) | BPTT Gradient Bottlenecks | Exponential gradient decay tracking, gradient clipping (`clip_grad_norm_`) |
| **03** | [`03_lstm_and_gru.ipynb`](./Advanced-Deep-Learning/03_lstm_and_gru.ipynb) | Gated Memory Mechanics | Parameter efficiency comparison (GRU 3 linear ops vs LSTM 4 linear ops) |
| **04** | [`04_transfer_learning.ipynb`](./Advanced-Deep-Learning/04_transfer_learning.ipynb) | Transfer Learning & Fine-Tuning | Backbone parameter freezing, differential learning rates, downstream heads |
| **05** | [`05_autoencoders.ipynb`](./Advanced-Deep-Learning/05_autoencoders.ipynb) | Bottleneck Compression | Deep symmetric autoencoder, latent representation compression, reconstruction loss |
| **06** | [`06_attention_mechanism.ipynb`](./Advanced-Deep-Learning/06_attention_mechanism.ipynb) | Scaled Dot-Product Attention | From-scratch PyTorch implementation of $\text{softmax}(QK^T / \sqrt{d_k})V$ |
| **07** | [`07_transformers_introduction.ipynb`](./Advanced-Deep-Learning/07_transformers_introduction.ipynb) | Transformer Block Anatomy | Multi-Head Attention, Positional Encoding intuition, `nn.TransformerEncoder` |
| **08** | [`08_gpu_training.ipynb`](./Advanced-Deep-Learning/08_gpu_training.ipynb) | High-Performance Distributed Compute | Automatic Mixed Precision (`autocast`), `GradScaler`, CUDA memory profiling |
| **09** | [`09_model_regularization.ipynb`](./Advanced-Deep-Learning/09_model_regularization.ipynb) | Overfitting Countermeasures | Dropout, Batch Normalization, Weight Decay, and Data Augmentation |

---

### 5. 🏆 Real-World Portfolio Projects (5 Notebooks)

| # | Project | Domain & Architecture | Key Highlights & Deliverables |
| :-: | :--- | :--- | :--- |
| **01** | [`01_handwritten_digit_recognition.ipynb`](./Projects/01_handwritten_digit_recognition.ipynb) | Vision (MNIST) | 2-stage ConvNet, MaxPool, Dropout, 10-class Softmax, Confusion Matrix |
| **02** | [`02_image_classification.ipynb`](./Projects/02_image_classification.ipynb) | Color Vision (CIFAR-10) | Deep 3-channel RGB ResNet-style ConvNet with Global Average Pooling |
| **03** | [`03_cats_vs_dogs_classification.ipynb`](./Projects/03_cats_vs_dogs_classification.ipynb) | Binary Computer Vision | Real-world photograph classification, data augmentation, sigmoid cutoff |
| **04** | [`04_sentiment_analysis.ipynb`](./Projects/04_sentiment_analysis.ipynb) | NLP Sequence Modeling | Word Embeddings, Bidirectional LSTM, customer review sentiment classifier |
| **05** | [`05_deep_learning_final_project.ipynb`](./Projects/05_deep_learning_final_project.ipynb) | **Master Multi-Modal Capstone** | Autonomous Diagnostic & Predictive Intelligence Suite (Vision + Sequence + TorchScript) |

---

## 🎯 Capstone Projects Spotlight

### 1. 🩺 Medical Diagnostic Imaging Classifier (TensorFlow)
📁 **Notebook:** [`TensorFlow/13_tensorflow_mini_project.ipynb`](./TensorFlow/13_tensorflow_mini_project.ipynb)  
🛠️ **Stack:** TensorFlow 2.x, Keras, NumPy, Scikit-Learn  
- **Architecture**: Deep Convolutional Neural Network with Batch Normalization, spatial pooling, and dense dropout heads.
- **Problem Solved**: Automatically detects radiographic pulmonary pathologies (Pneumonia vs Normal Chest X-Rays) with EarlyStopping and serialization to `.keras`.

### 2. ⚙️ Industrial Vibration Acoustic Anomaly Detector (PyTorch)
📁 **Notebook:** [`PyTorch/13_pytorch_mini_project.ipynb`](./PyTorch/13_pytorch_mini_project.ipynb)  
🛠️ **Stack:** PyTorch 2.0+, Autograd, TorchScript  
- **Architecture**: Deep Residual Autoencoder trained exclusively on healthy baseline telemetry to detect mechanical bearing anomalies via reconstruction error divergence.
- **Problem Solved**: Identifies failure signals with over $4\times$ anomaly reconstruction separation and compiles to low-latency TorchScript (`.pt`) for C++ edge deployment.

### 3. 🌐 Autonomous Multi-Modal Diagnostic & Predictive Intelligence Suite (Master Capstone)
📁 **Notebook:** [`Projects/05_deep_learning_final_project.ipynb`](./Projects/05_deep_learning_final_project.ipynb)  
🛠️ **Stack:** PyTorch, Mish Activation, Multi-Task Learning, Cosine Annealing, TorchScript  
- **Architecture**: Unified multi-task deep neural architecture featuring a shared representation backbone feeding two specialized task heads:
  1. *Binary Classification Head*: Anomaly & Failure Risk Probability
  2. *Regression Head*: Continuous Severity Metric & Remaining Useful Life (RUL)
- **Problem Solved**: Replaces disparate siloed predictive models with a single unified multi-modal AI engine optimized with Cosine Annealing learning rate schedules and gradient clipping.

---

## ⚡ Hardware Acceleration & Deep Learning Best Practices

```python
import torch

# 1. Device-Agnostic Allocation
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 2. Automatic Mixed Precision (AMP) for 2x to 3x Speedups
scaler = torch.cuda.amp.GradScaler(enabled=torch.cuda.is_available())

for inputs, targets in dataloader:
    inputs, targets = inputs.to(device, non_blocking=True), targets.to(device, non_blocking=True)
    optimizer.zero_grad(set_to_none=True)  # Faster than zero_grad()
    
    with torch.cuda.amp.autocast(enabled=torch.cuda.is_available()):
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        
    scaler.scale(loss).backward()
    scaler.unscale_(optimizer)
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
    scaler.step(optimizer)
    scaler.update()
```

---

## 🚀 Environment Setup & Getting Started

```bash
# Clone repository
git clone https://github.com/VIJAYAPANDIANT/AI-ML-Learning.git
cd AI-ML-Learning/Deep-Learning

# Activate virtual environment
# Windows:
..\venv\Scripts\Activate.ps1
# Linux/macOS:
source ../venv/bin/activate

# Install Deep Learning Frameworks
pip install torch torchvision torchaudio
pip install tensorflow keras
pip install numpy pandas matplotlib scikit-learn jupyter
```

```bash
# Launch JupyterLab
jupyter lab
```

---

<div align="center">
  <b>Explore Ecosystem:</b> <a href="../Python/">🐍 Python</a> • <a href="../Numpy/">🔢 NumPy</a> • <a href="../Pandas/">📊 Pandas</a> • <a href="../Matplotlib/">📈 Matplotlib</a> • <a href="../Seaborn/">📊 Seaborn</a> • <a href="../Scikit-learn/">⚙️ Scikit-Learn</a>
</div>
