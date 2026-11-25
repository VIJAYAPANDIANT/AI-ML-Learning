# 🌿 Plant Leaf Disease Detection System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)]()
[![Level](https://img.shields.io/badge/Level-Intermediate-yellow.svg)]()

## 📌 Project Overview
Automated agricultural computer vision system that classifies crop leaf diseases (Tomato Early Blight, Late Blight, Bacterial Spot, Healthy) using Convolutional Neural Networks and Transfer Learning.

## 🛠️ Tech Stack & Architecture
- **Framework:** PyTorch 2.0+, Torchvision
- **Backbone:** Transfer Learning via MobileNetV3 / ResNet-18
- **Data Augmentation:** Random Horizontal Flip, ColorJitter, Affine rotation
- **Deployment:** FastAPI inference endpoint with confidence thresholds
