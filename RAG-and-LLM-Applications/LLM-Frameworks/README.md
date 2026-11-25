# ⚡ LLM Frameworks: LangChain & LlamaIndex

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![Frameworks](https://img.shields.io/badge/Frameworks-LangChain%20|%20LlamaIndex-10B981?style=for-the-badge)]()
[![Status](https://img.shields.io/badge/Status-Completed%20(11%2F11)-success?style=for-the-badge)]()

Welcome to the **LLM Frameworks** section. This curriculum provides deep architectural mastery over the two dominant orchestration frameworks in the Generative AI ecosystem: **LangChain** (and LCEL) and **LlamaIndex**.

---

## 🦜 LangChain Masterclass (6 Notebooks)

| # | Notebook | Core Capability | Status |
| :-: | :--- | :--- | :-: |
| 01 | [`LangChain/01_langchain_introduction.ipynb`](./LangChain/01_langchain_introduction.ipynb) | LangChain architecture, LangChain Expression Language (LCEL) & Runnable protocol | Completed ✅ |
| 02 | [`LangChain/02_models_and_prompts.ipynb`](./LangChain/02_models_and_prompts.ipynb) | Chat models, polymorphic message types (`HumanMessage`, `AIMessage`, `SystemMessage`) | Completed ✅ |
| 03 | [`LangChain/03_chains_and_runnables.ipynb`](./LangChain/03_chains_and_runnables.ipynb) | `RunnableParallel`, `RunnablePassthrough`, branching logic & `.with_fallbacks()` | Completed ✅ |
| 04 | [`LangChain/04_retrievers.ipynb`](./LangChain/04_retrievers.ipynb) | VectorStoreRetriever, EnsembleRetriever & Contextual Compression | Completed ✅ |
| 05 | [`LangChain/05_langchain_rag.ipynb`](./LangChain/05_langchain_rag.ipynb) | Canonical LCEL RAG chain: `retriever | format_docs | prompt | model | parser` | Completed ✅ |
| 06 | [`LangChain/06_langchain_agents.ipynb`](./LangChain/06_langchain_agents.ipynb) | `@tool` decorator, `create_tool_calling_agent`, `AgentExecutor` & execution traces | Completed ✅ |

---

## 🦙 LlamaIndex Masterclass (5 Notebooks)

| # | Notebook | Core Capability | Status |
| :-: | :--- | :--- | :-: |
| 01 | [`LlamaIndex/01_llamaindex_introduction.ipynb`](./LlamaIndex/01_llamaindex_introduction.ipynb) | Data-centric framework, Document vs Node abstraction & relationship graph | Completed ✅ |
| 02 | [`LlamaIndex/02_data_connectors.ipynb`](./LlamaIndex/02_data_connectors.ipynb) | LlamaHub connectors: `SimpleDirectoryReader`, database readers & metadata parsing | Completed ✅ |
| 03 | [`LlamaIndex/03_indexing_and_retrieval.ipynb`](./LlamaIndex/03_indexing_and_retrieval.ipynb) | `VectorStoreIndex`, `SummaryIndex`, `TreeIndex` & node parsers | Completed ✅ |
| 04 | [`LlamaIndex/04_query_engines.ipynb`](./LlamaIndex/04_query_engines.ipynb) | Query engines vs Chat engines, Response synthesis modes (`refine`, `compact`) | Completed ✅ |
| 05 | [`LlamaIndex/05_llamaindex_rag.ipynb`](./LlamaIndex/05_llamaindex_rag.ipynb) | End-to-end LlamaIndex RAG application with `SimilarityPostprocessor` & source citations | Completed ✅ |
