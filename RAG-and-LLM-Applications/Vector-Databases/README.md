# 🗄️ Vector Databases Masterclass

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![Vector DB](https://img.shields.io/badge/Vector--DB-Chroma%20|%20FAISS%20|%20Pinecone-8A2BE2?style=for-the-badge)]()
[![Status](https://img.shields.io/badge/Status-Completed%20(7%2F7)-success?style=for-the-badge)]()

Welcome to the **Vector Databases** section of the RAG & LLM Applications module. This curriculum covers high-dimensional vector storage, Approximate Nearest Neighbors (ANN) indexing, metadata filtering, and hybrid search fusion.

---

## 📚 Curriculum Index

| # | Notebook | Core Concepts & Architecture | Status |
| :-: | :--- | :--- | :-: |
| 01 | [`01_vector_database_introduction.ipynb`](./01_vector_database_introduction.ipynb) | Vector DB vs Traditional RDBMS/NoSQL, ANN vs Exact $k$-NN, Index structures (HNSW, IVF, PQ) | Completed ✅ |
| 02 | [`02_chroma_db.ipynb`](./02_chroma_db.ipynb) | ChromaDB architecture, Client setup, Collections, CRUD operations, SQLite/DuckDB persistence | Completed ✅ |
| 03 | [`03_faiss.ipynb`](./03_faiss.ipynb) | Meta FAISS: IndexFlatL2, IndexFlatIP, Voronoi cells (`IndexIVFFlat`), Product Quantization (`IndexIVFPQ`) | Completed ✅ |
| 04 | [`04_pinecone.ipynb`](./04_pinecone.ipynb) | Managed cloud vector search: Serverless indexes, Namespaces, Metadata schemas & top-$K$ queries | Completed ✅ |
| 05 | [`05_vector_storage_and_retrieval.ipynb`](./05_vector_storage_and_retrieval.ipynb) | Document chunk lifecycle, Deterministic UUIDs, Batch upsert pipelines, Versioned updates | Completed ✅ |
| 06 | [`06_metadata_filtering.ipynb`](./06_metadata_filtering.ipynb) | Pre-filtering, Post-filtering, Single-stage filtered ANN, Boolean expressions (`$eq`, `$in`, `$gte`) | Completed ✅ |
| 07 | [`07_hybrid_search.ipynb`](./07_hybrid_search.ipynb) | Fusing sparse BM25 keyword matching with dense vector search, Reciprocal Rank Fusion (RRF) | Completed ✅ |

---

## 📊 Vector Search Index Comparison

| Index Type | Search Speed | RAM Usage | Build Time | Recall Accuracy | Best Use Case |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Flat ($k$-NN)** | Slow ($O(N)$) | Baseline ($1\\times$) | Instant ($0$s) | 100% (Exact) | Small datasets ($<50\\text{k}$ vectors) |
| **HNSW** | Ultra Fast ($O(\\log N)$) | High ($1.2\\times - 1.5\\times$) | Moderate | 95% - 99% | Low-latency production apps |
| **IVFFlat** | Fast | Baseline ($1\\times$) | Fast | 90% - 95% | Medium datasets ($100\\text{k} - 1\\text{M}$) |
| **IVFPQ** | Ultra Fast | Minimal ($0.12\\times$) | Moderate | 85% - 92% | Billion-scale memory-constrained search |
