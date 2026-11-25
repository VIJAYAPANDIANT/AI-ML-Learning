# 🤖 Autonomous AI Task Assistant with Human-in-the-Loop

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()
[![Level](https://img.shields.io/badge/Level-Advanced-red.svg)]()

## 📌 Project Overview
Autonomous workflow orchestration assistant that breaks down complex user objectives into multi-step ReAct action plans, dynamically selects external APIs/tools, and enforces Human-in-the-Loop approval gates on sensitive actions.

## 🛠️ Tech Stack & Algorithms
- **Agent Architecture:** ReAct (Reasoning + Acting) execution loop
- **Tool Registry:** Standard JSON Schemas with Pydantic validation
- **Governance:** Human approval interceptors & complete execution trajectory logging
