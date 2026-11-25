# 🔍 Retrieval-Augmented Generation (RAG) Architecture

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![RAG](https://img.shields.io/badge/Architecture-Advanced--RAG-FF6F00?style=for-the-badge)]()
[![Status](https://img.shields.io/badge/Status-Completed%20(16%2F16)-success?style=for-the-badge)]()

Welcome to the **RAG (Retrieval-Augmented Generation)** core module. This curriculum provides a comprehensive breakdown of production RAG pipelines, from multi-format document parsing to two-stage Cross-Encoder re-ranking, self-correction, and RAGAS evaluation.

---

## 📚 Curriculum Index

| # | Notebook | Core Retrieval Mechanism | Status |
| :-: | :--- | :--- | :-: |
| 01 | [`01_rag_introduction.ipynb`](./01_rag_introduction.ipynb) | What is RAG? Hallucination mitigation, Grounded knowledge & RAG benefits | Completed ✅ |
| 02 | [`02_rag_architecture.ipynb`](./02_rag_architecture.ipynb) | End-to-End System Architecture: Offline Ingestion vs Online Query planes | Completed ✅ |
| 03 | [`03_document_loading.ipynb`](./03_document_loading.ipynb) | Loading multi-format sources: PDF, DOCX, Markdown, HTML, CSV & JSON | Completed ✅ |
| 04 | [`04_document_parsing.ipynb`](./04_document_parsing.ipynb) | Layout analysis, Table linearization & extracting structured metadata | Completed ✅ |
| 05 | [`05_text_chunking.ipynb`](./05_text_chunking.ipynb) | Chunking strategies: Recursive character splitting, semantic boundaries & overlap | Completed ✅ |
| 06 | [`06_embedding_generation.ipynb`](./06_embedding_generation.ipynb) | Batch embedding generation, Token pre-checks & rate-limit throttling | Completed ✅ |
| 07 | [`07_vector_database_integration.ipynb`](./07_vector_database_integration.ipynb) | Ingesting chunks into vector stores with persistent metadata enrichment | Completed ✅ |
| 08 | [`08_document_retrieval.ipynb`](./08_document_retrieval.ipynb) | Query similarity search, Distance scores & minimum similarity thresholding | Completed ✅ |
| 09 | [`09_context_augmentation.ipynb`](./09_context_augmentation.ipynb) | Context injection into prompts, XML delimiter fencing & context budgeting | Completed ✅ |
| 10 | [`10_rag_pipeline.ipynb`](./10_rag_pipeline.ipynb) | Building a production, modular, object-oriented RAG pipeline class | Completed ✅ |
| 11 | [`11_retrieval_strategies.ipynb`](./11_retrieval_strategies.ipynb) | Advanced retrieval: Multi-Query synthesis, Step-Back prompting & Parent Document | Completed ✅ |
| 12 | [`12_reranking.ipynb`](./12_reranking.ipynb) | Two-stage retrieval: Bi-Encoder broad recall (Top-50) + Cross-Encoder re-ranking (Top-5) | Completed ✅ |
| 13 | [`13_hybrid_rag.ipynb`](./13_hybrid_rag.ipynb) | Hybrid RAG architecture: Dense HNSW + Sparse BM25 + Reciprocal Rank Fusion | Completed ✅ |
| 14 | [`14_conversational_rag.ipynb`](./14_conversational_rag.ipynb) | Conversational RAG with Chat History: Multi-turn query contextualization | Completed ✅ |
| 15 | [`15_advanced_rag.ipynb`](./15_advanced_rag.ipynb) | Corrective RAG (CRAG), Self-RAG reflection tokens & Adaptive query routing | Completed ✅ |
| 16 | [`16_rag_evaluation.ipynb`](./16_rag_evaluation.ipynb) | RAG Triad evaluation: Context Relevance, Faithfulness & Answer Relevance | Completed ✅ |

---

## 🔄 The Production RAG Pipeline

```
+-----------------------------------------------------------------------------------------+
|                                Production RAG Pipeline                                  |
+-----------------------------------------------------------------------------------------+
| [User Query] ---> [Query Rewriter] ---> [Dense Search (Vector DB)]                      |
|                                     \-> [Sparse Search (BM25 Index)]                    |
|                                                     |                                   |
|                                        [Reciprocal Rank Fusion]                         |
|                                                     |                                   |
|                                        [Cross-Encoder Reranker]                         |
|                                                     |                                   |
|                                        [Top-K Context Augmenter]                        |
|                                                     |                                   |
|                                            [LLM Generation]                             |
|                                                     |                                   |
|                                        [Faithfulness Guardrail]                         |
|                                                     |                                   |
|                                          [Verified Answer]                              |
+-----------------------------------------------------------------------------------------+
```
