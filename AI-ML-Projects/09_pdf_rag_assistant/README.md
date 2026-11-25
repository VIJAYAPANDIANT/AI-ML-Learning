# 📄 Intelligent PDF Knowledge Assistant (RAG)

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()
[![RAG](https://img.shields.io/badge/Architecture-RAG-orange.svg)]()
[![Level](https://img.shields.io/badge/Level-Intermediate-yellow.svg)]()

## 📌 Project Overview
Upload multiple PDF documents, automatically chunk and embed the content into ChromaDB, and query with verified page and paragraph citations.

## 🛠️ Tech Stack & Architecture
- **Document Loading & Parsing:** PyPDF, LangChain Text Splitters
- **Vector Database:** ChromaDB / In-Memory HNSW
- **Embeddings:** OpenAI text-embedding-3 / Hugging Face MiniLM
- **LLM Synthesis:** Grounded QA with citation validation
