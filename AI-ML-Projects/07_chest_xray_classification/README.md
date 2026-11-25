# 🫁 Chest X-Ray Multi-Label Pathology Classification

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)]()
[![Level](https://img.shields.io/badge/Level-Advanced-red.svg)]()

## 📌 Project Overview
Deep learning classification system for thoracic radiograph abnormalities (Normal, Pneumonia, Pleural Effusion, Infiltration) featuring Grad-CAM visual interpretability maps.

## ⚠️ Medical Disclaimer
This software is developed strictly for research, educational, and benchmarking purposes. It is not an FDA-approved diagnostic medical device.

## 🛠️ Tech Stack & Architecture
- **Framework:** PyTorch 2.0+, Torchvision, MONAI
- **Loss Function:** Binary Cross-Entropy with Logits (BCEWithLogitsLoss)
- **Interpretability:** Grad-CAM (Gradient-Weighted Class Activation Mapping)
