# 🚀 RAG & LLM Applications Masterclass

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![RAG](https://img.shields.io/badge/Architecture-RAG%20%26%20Agents-8A2BE2?style=for-the-badge)]()
[![Notebooks](https://img.shields.io/badge/Curriculum-71%20Completed%20Notebooks-success?style=for-the-badge)]()
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)]()

Welcome to the **RAG & LLM Applications** curriculum of the AI/ML portfolio repository. This module provides a complete, production-grade guide to engineering enterprise Generative AI systems — spanning API integration, embedding theory, vector database indexing, advanced Hybrid RAG, LangChain, LlamaIndex, autonomous AI agents, evaluation frameworks (RAGAS), and production optimization.

---

## 🧭 Topic Categories & Learning Matrix

| Category | Core Architectural Competencies | Notebooks |
| :--- | :--- | :---: |
| **1. LLM Application Foundations** | REST APIs, authentication, sampling parameters, resilient retry backoff, prompt templates, structured output, sliding memory, and real-time streaming generators | 8 |
| **2. Embeddings & Semantic Search** | Metric spaces, $L_2$ normalization, SBERT mean pooling, MTEB benchmarks, cosine distance, and vector search engines | 6 |
| **3. Vector Databases** | Exact $k$-NN vs ANN (HNSW, IVF, PQ), ChromaDB persistence, Meta FAISS, Pinecone namespaces, CRUD storage lifecycles, metadata filtering, and Reciprocal Rank Fusion | 7 |
| **4. RAG Architecture & Ingestion** | Ingestion pipelines, layout analysis, recursive chunking, batch embedding pipelines, and vector store integration | 7 |
| **5. Advanced RAG & Retrieval** | Dynamic score thresholding, multi-query expansion, Cross-Encoder neural re-ranking, Hybrid RAG, conversational RAG, CRAG, Self-RAG, and RAG Triad evaluation | 9 |
| **6. LLM Frameworks** | LangChain Expression Language (LCEL), runnables, custom retrievers, tools, LlamaIndex node hierarchy, query engines, and response synthesizers | 11 |
| **7. AI Agents & Autonomy** | ReAct reasoning loops, JSON Schema tool declarations, native function calling, multi-tiered memory scratchpads, HITL approval gates, and multi-agent coordination | 7 |
| **8. Optimization & Evaluation** | LLM-as-a-Judge, RAGAS metrics, hallucination detection (CoVe), prompt compression, semantic caching, safety guardrails (PII masking), and OpenTelemetry tracing | 7 |
| **9. Portfolio Projects & Capstone** | Conversational assistants, PDF QA with citations, ChromaDB doc bots, web scrapers, research agents, talent matching, multi-corpus routing, and **Master Enterprise Capstone** | 9 |
| **Total Completed Curriculum** | **Complete Beginner-to-Advanced Production AI Application Engineering** | **71** |

---

## 🗂️ Complete Curriculum Index (71 Notebooks)

### Phase 1: LLM Application Foundations (8 Notebooks)
| # | Notebook | Core Focus & Architecture | Status |
| :-: | :--- | :--- | :-: |
| 01 | [`01_llm_application_introduction.ipynb`](./01_llm_application_introduction.ipynb) | LLM application architecture, Foundation models, Prompting vs Fine-tuning vs RAG | Completed ✅ |
| 02 | [`02_llm_api_fundamentals.ipynb`](./02_llm_api_fundamentals.ipynb) | REST APIs, Temperature, Top-P, Presence/Frequency penalties, Request payloads | Completed ✅ |
| 03 | [`03_api_integration.ipynb`](./03_api_integration.ipynb) | Production API integration, Exponential backoff with jitter, Async batching | Completed ✅ |
| 04 | [`04_prompt_engineering.ipynb`](./04_prompt_engineering.ipynb) | Systematic prompt design, XML delimiter fencing, Few-shot prompting, Chain-of-Thought | Completed ✅ |
| 05 | [`05_prompt_templates.ipynb`](./05_prompt_templates.ipynb) | Dynamic prompt templating, Variable validation schemas, Composable prompt catalogs | Completed ✅ |
| 06 | [`06_structured_output.ipynb`](./06_structured_output.ipynb) | JSON Mode, Pydantic data validation, Function calling schemas & repair loops | Completed ✅ |
| 07 | [`07_conversation_memory.ipynb`](./07_conversation_memory.ipynb) | Conversation memory: Sliding window buffers, Summary memory, Vector-backed history | Completed ✅ |
| 08 | [`08_streaming_responses.ipynb`](./08_streaming_responses.ipynb) | Server-Sent Events (SSE), Streaming token generators, Real-time UI rendering simulation | Completed ✅ |

---

### Phase 2: Embeddings & Semantic Search (6 Notebooks)
| # | Notebook | Vector Metric Space | Status |
| :-: | :--- | :--- | :-: |
| 01 | [`Embeddings/01_embeddings_introduction.ipynb`](./Embeddings/01_embeddings_introduction.ipynb) | Metric spaces, Directional semantics, Word & sentence vector geometry | Completed ✅ |
| 02 | [`Embeddings/02_text_embeddings.ipynb`](./Embeddings/02_text_embeddings.ipynb) | Generating text embeddings, $L_2$ normalization & Matryoshka dimensionality reduction | Completed ✅ |
| 03 | [`Embeddings/03_sentence_transformers.ipynb`](./Embeddings/03_sentence_transformers.ipynb) | Sentence-BERT (SBERT) Siamese architecture & attention-weighted mean pooling | Completed ✅ |
| 04 | [`Embeddings/04_embedding_models.ipynb`](./Embeddings/04_embedding_models.ipynb) | MTEB retrieval leaderboard benchmarks: BGE, E5, GTE & OpenAI models | Completed ✅ |
| 05 | [`Embeddings/05_similarity_search.ipynb`](./Embeddings/05_similarity_search.ipynb) | Distance metrics: Cosine similarity vs Euclidean ($L_2$) distance vs Dot Product | Completed ✅ |
| 06 | [`Embeddings/06_semantic_search.ipynb`](./Embeddings/06_semantic_search.ipynb) | In-memory semantic search engine: Ingestion, Query vectorization & Top-$K$ ranking | Completed ✅ |

---

### Phase 3: Vector Databases Masterclass (7 Notebooks)
*Detailed module guide: [`Vector-Databases/README.md`](./Vector-Databases/README.md)*

| # | Notebook | Index Structure & Engine | Status |
| :-: | :--- | :--- | :-: |
| 01 | [`Vector-Databases/01_vector_database_introduction.ipynb`](./Vector-Databases/01_vector_database_introduction.ipynb) | Vector DB vs Traditional RDBMS/NoSQL, ANN vs Exact $k$-NN, Index structures (HNSW, IVF, PQ) | Completed ✅ |
| 02 | [`Vector-Databases/02_chroma_db.ipynb`](./Vector-Databases/02_chroma_db.ipynb) | ChromaDB architecture, Client setup, Collections, CRUD operations, SQLite/DuckDB persistence | Completed ✅ |
| 03 | [`Vector-Databases/03_faiss.ipynb`](./Vector-Databases/03_faiss.ipynb) | Meta FAISS: IndexFlatL2, IndexFlatIP, Voronoi cells (`IndexIVFFlat`), Product Quantization (`IndexIVFPQ`) | Completed ✅ |
| 04 | [`Vector-Databases/04_pinecone.ipynb`](./Vector-Databases/04_pinecone.ipynb) | Managed cloud vector search: Serverless indexes, Namespaces, Metadata schemas & top-$K$ queries | Completed ✅ |
| 05 | [`Vector-Databases/05_vector_storage_and_retrieval.ipynb`](./Vector-Databases/05_vector_storage_and_retrieval.ipynb) | Document chunk lifecycle, Deterministic UUIDs, Batch upsert pipelines, Versioned updates | Completed ✅ |
| 06 | [`Vector-Databases/06_metadata_filtering.ipynb`](./Vector-Databases/06_metadata_filtering.ipynb) | Pre-filtering, Post-filtering, Single-stage filtered ANN, Boolean expressions (`$eq`, `$in`, `$gte`) | Completed ✅ |
| 07 | [`Vector-Databases/07_hybrid_search.ipynb`](./Vector-Databases/07_hybrid_search.ipynb) | Fusing sparse BM25 keyword matching with dense vector search, Reciprocal Rank Fusion (RRF) | Completed ✅ |

---

### Phase 4: Retrieval-Augmented Generation (RAG) (16 Notebooks)
*Detailed module guide: [`RAG/README.md`](./RAG/README.md)*

| # | Notebook | Core Ingestion & Retrieval Pipeline | Status |
| :-: | :--- | :--- | :-: |
| 01 | [`RAG/01_rag_introduction.ipynb`](./RAG/01_rag_introduction.ipynb) | What is RAG? Hallucination mitigation, Grounded knowledge & RAG benefits | Completed ✅ |
| 02 | [`RAG/02_rag_architecture.ipynb`](./RAG/02_rag_architecture.ipynb) | End-to-End System Architecture: Offline Ingestion vs Online Query planes | Completed ✅ |
| 03 | [`RAG/03_document_loading.ipynb`](./RAG/03_document_loading.ipynb) | Loading multi-format sources: PDF, DOCX, Markdown, HTML, CSV & JSON | Completed ✅ |
| 04 | [`RAG/04_document_parsing.ipynb`](./RAG/04_document_parsing.ipynb) | Layout analysis, Table linearization & extracting structured metadata | Completed ✅ |
| 05 | [`RAG/05_text_chunking.ipynb`](./RAG/05_text_chunking.ipynb) | Chunking strategies: Recursive character splitting, semantic boundaries & overlap | Completed ✅ |
| 06 | [`RAG/06_embedding_generation.ipynb`](./RAG/06_embedding_generation.ipynb) | Batch embedding generation, Token pre-checks & rate-limit throttling | Completed ✅ |
| 07 | [`RAG/07_vector_database_integration.ipynb`](./RAG/07_vector_database_integration.ipynb) | Ingesting chunks into vector stores with persistent metadata enrichment | Completed ✅ |
| 08 | [`RAG/08_document_retrieval.ipynb`](./RAG/08_document_retrieval.ipynb) | Query similarity search, Distance scores & minimum similarity thresholding | Completed ✅ |
| 09 | [`RAG/09_context_augmentation.ipynb`](./RAG/09_context_augmentation.ipynb) | Context injection into prompts, XML delimiter fencing & context budgeting | Completed ✅ |
| 10 | [`RAG/10_rag_pipeline.ipynb`](./RAG/10_rag_pipeline.ipynb) | Building a production, modular, object-oriented RAG pipeline class | Completed ✅ |
| 11 | [`RAG/11_retrieval_strategies.ipynb`](./RAG/11_retrieval_strategies.ipynb) | Advanced retrieval: Multi-Query synthesis, Step-Back prompting & Parent Document | Completed ✅ |
| 12 | [`RAG/12_reranking.ipynb`](./RAG/12_reranking.ipynb) | Two-stage retrieval: Bi-Encoder broad recall (Top-50) + Cross-Encoder re-ranking (Top-5) | Completed ✅ |
| 13 | [`RAG/13_hybrid_rag.ipynb`](./RAG/13_hybrid_rag.ipynb) | Hybrid RAG architecture: Dense HNSW + Sparse BM25 + Reciprocal Rank Fusion | Completed ✅ |
| 14 | [`RAG/14_conversational_rag.ipynb`](./RAG/14_conversational_rag.ipynb) | Conversational RAG with Chat History: Multi-turn query contextualization | Completed ✅ |
| 15 | [`RAG/15_advanced_rag.ipynb`](./RAG/15_advanced_rag.ipynb) | Corrective RAG (CRAG), Self-RAG reflection tokens & Adaptive query routing | Completed ✅ |
| 16 | [`RAG/16_rag_evaluation.ipynb`](./RAG/16_rag_evaluation.ipynb) | RAG Triad evaluation: Context Relevance, Faithfulness & Answer Relevance | Completed ✅ |

---

### Phase 5: LLM Frameworks: LangChain & LlamaIndex (11 Notebooks)
*Detailed module guide: [`LLM-Frameworks/README.md`](./LLM-Frameworks/README.md)*

| # | Notebook | Framework Capability | Status |
| :-: | :--- | :--- | :-: |
| 01 | [`LLM-Frameworks/LangChain/01_langchain_introduction.ipynb`](./LLM-Frameworks/LangChain/01_langchain_introduction.ipynb) | LangChain architecture, LangChain Expression Language (LCEL) & Runnable protocol | Completed ✅ |
| 02 | [`LLM-Frameworks/LangChain/02_models_and_prompts.ipynb`](./LLM-Frameworks/LangChain/02_models_and_prompts.ipynb) | Chat models, polymorphic message types (`HumanMessage`, `AIMessage`, `SystemMessage`) | Completed ✅ |
| 03 | [`LLM-Frameworks/LangChain/03_chains_and_runnables.ipynb`](./LLM-Frameworks/LangChain/03_chains_and_runnables.ipynb) | `RunnableParallel`, `RunnablePassthrough`, branching logic & `.with_fallbacks()` | Completed ✅ |
| 04 | [`LLM-Frameworks/LangChain/04_retrievers.ipynb`](./LLM-Frameworks/LangChain/04_retrievers.ipynb) | VectorStoreRetriever, EnsembleRetriever & Contextual Compression | Completed ✅ |
| 05 | [`LLM-Frameworks/LangChain/05_langchain_rag.ipynb`](./LLM-Frameworks/LangChain/05_langchain_rag.ipynb) | Canonical LCEL RAG chain: `retriever | format_docs | prompt | model | parser` | Completed ✅ |
| 06 | [`LLM-Frameworks/LangChain/06_langchain_agents.ipynb`](./LLM-Frameworks/LangChain/06_langchain_agents.ipynb) | `@tool` decorator, `create_tool_calling_agent`, `AgentExecutor` & execution traces | Completed ✅ |
| 07 | [`LLM-Frameworks/LlamaIndex/01_llamaindex_introduction.ipynb`](./LLM-Frameworks/LlamaIndex/01_llamaindex_introduction.ipynb) | Data-centric framework, Document vs Node abstraction & relationship graph | Completed ✅ |
| 08 | [`LLM-Frameworks/LlamaIndex/02_data_connectors.ipynb`](./LLM-Frameworks/LlamaIndex/02_data_connectors.ipynb) | LlamaHub connectors: `SimpleDirectoryReader`, database readers & metadata parsing | Completed ✅ |
| 09 | [`LLM-Frameworks/LlamaIndex/03_indexing_and_retrieval.ipynb`](./LLM-Frameworks/LlamaIndex/03_indexing_and_retrieval.ipynb) | `VectorStoreIndex`, `SummaryIndex`, `TreeIndex` & node parsers | Completed ✅ |
| 10 | [`LLM-Frameworks/LlamaIndex/04_query_engines.ipynb`](./LLM-Frameworks/LlamaIndex/04_query_engines.ipynb) | Query engines vs Chat engines, Response synthesis modes (`refine`, `compact`) | Completed ✅ |
| 11 | [`LLM-Frameworks/LlamaIndex/05_llamaindex_rag.ipynb`](./LLM-Frameworks/LlamaIndex/05_llamaindex_rag.ipynb) | End-to-end LlamaIndex RAG application with `SimilarityPostprocessor` & source citations | Completed ✅ |

---

### Phase 6: Autonomous AI Agents (7 Notebooks)
| # | Notebook | Agent Mechanism | Status |
| :-: | :--- | :--- | :-: |
| 01 | [`AI-Agents/01_ai_agents_introduction.ipynb`](./AI-Agents/01_ai_agents_introduction.ipynb) | Autonomous Agent architecture, Perception-Reasoning-Action loop & ReAct traces | Completed ✅ |
| 02 | [`AI-Agents/02_tool_calling.ipynb`](./AI-Agents/02_tool_calling.ipynb) | Standardized tool schemas, JSON Schema generation, tool execution safety | Completed ✅ |
| 03 | [`AI-Agents/03_function_calling.ipynb`](./AI-Agents/03_function_calling.ipynb) | Native model function calling, Parallel function calls & tool response handling | Completed ✅ |
| 04 | [`AI-Agents/04_agent_memory.ipynb`](./AI-Agents/04_agent_memory.ipynb) | Agent working memory vs Episodic memory vs Semantic memory & thought scratchpads | Completed ✅ |
| 05 | [`AI-Agents/05_agent_workflows.ipynb`](./AI-Agents/05_agent_workflows.ipynb) | Agentic design patterns, Reflection, Planning loops & Human-in-the-loop approval gates | Completed ✅ |
| 06 | [`AI-Agents/06_multi_agent_systems.ipynb`](./AI-Agents/06_multi_agent_systems.ipynb) | Multi-agent architectures: Supervisor routing, peer collaboration & synthesis | Completed ✅ |
| 07 | [`AI-Agents/07_agent_evaluation.ipynb`](./AI-Agents/07_agent_evaluation.ipynb) | Trajectory evaluation: Tool call accuracy, step count efficiency & goal success rates | Completed ✅ |

---

### Phase 7: LLM Optimization, Safety & Evaluation (7 Notebooks)
| # | Notebook | Operational Discipline | Status |
| :-: | :--- | :--- | :-: |
| 01 | [`LLM-Optimization-and-Evaluation/01_llm_evaluation.ipynb`](./LLM-Optimization-and-Evaluation/01_llm_evaluation.ipynb) | LLM evaluation paradigms: Human eval, Benchmark suites & LLM-as-a-Judge rubrics | Completed ✅ |
| 02 | [`LLM-Optimization-and-Evaluation/02_rag_evaluation_metrics.ipynb`](./LLM-Optimization-and-Evaluation/02_rag_evaluation_metrics.ipynb) | RAGAS framework: Faithfulness, Answer Relevance, Context Precision & Context Recall | Completed ✅ |
| 03 | [`LLM-Optimization-and-Evaluation/03_hallucination_detection.ipynb`](./LLM-Optimization-and-Evaluation/03_hallucination_detection.ipynb) | Detecting hallucinations: Chain-of-Verification (CoVe), Self-Consistency & NLI entailment | Completed ✅ |
| 04 | [`LLM-Optimization-and-Evaluation/04_latency_and_token_optimization.ipynb`](./LLM-Optimization-and-Evaluation/04_latency_and_token_optimization.ipynb) | Prompt compression (LLMLingua), Speculative decoding, KV Cache reuse & Quantization | Completed ✅ |
| 05 | [`LLM-Optimization-and-Evaluation/05_caching.ipynb`](./LLM-Optimization-and-Evaluation/05_caching.ipynb) | Exact SHA-256 caching vs Semantic embedding vector caching with Redis / GPTCache | Completed ✅ |
| 06 | [`LLM-Optimization-and-Evaluation/06_guardrails_and_safety.ipynb`](./LLM-Optimization-and-Evaluation/06_guardrails_and_safety.ipynb) | Ingress & Egress guardrails: Prompt injection shields, Jailbreak defense & PII redaction | Completed ✅ |
| 07 | [`LLM-Optimization-and-Evaluation/07_llm_observability.ipynb`](./LLM-Optimization-and-Evaluation/07_llm_observability.ipynb) | Observability: OpenTelemetry distributed tracing, Token usage accounting & Latency profiling | Completed ✅ |

---

### Phase 8: Portfolio Projects & Master Capstone (9 Notebooks)
| # | Project | Domain & Application Architecture | Status |
| :-: | :--- | :--- | :-: |
| 01 | [`Projects/01_ai_chatbot.ipynb`](./Projects/01_ai_chatbot.ipynb) | Multi-Turn Conversational Assistant with Context Management & Sliding Memory Window | Completed ✅ |
| 02 | [`Projects/02_pdf_question_answering.ipynb`](./Projects/02_pdf_question_answering.ipynb) | Multi-PDF Question Answering with Exact Page & Paragraph Citations | Completed ✅ |
| 03 | [`Projects/03_rag_document_chatbot.ipynb`](./Projects/03_rag_document_chatbot.ipynb) | Enterprise Document Intelligence RAG Assistant with ChromaDB Vector Store | Completed ✅ |
| 04 | [`Projects/04_website_knowledge_chatbot.ipynb`](./Projects/04_website_knowledge_chatbot.ipynb) | Web Crawler & Sitemap Knowledge Ingestion RAG Assistant | Completed ✅ |
| 05 | [`Projects/05_ai_research_assistant.ipynb`](./Projects/05_ai_research_assistant.ipynb) | Autonomous Multi-Tool Research Assistant (Web Search + Internal RAG + Citations) | Completed ✅ |
| 06 | [`Projects/06_resume_analysis_system.ipynb`](./Projects/06_resume_analysis_system.ipynb) | Automated Talent Intelligence: Resume Parsing, Skill Graph Extraction & Job Match Scoring | Completed ✅ |
| 07 | [`Projects/07_multi_document_rag.ipynb`](./Projects/07_multi_document_rag.ipynb) | Cross-Document Multi-Corpus RAG Engine with Hierarchical Routing | Completed ✅ |
| 08 | [`Projects/08_ai_agent_assistant.ipynb`](./Projects/08_ai_agent_assistant.ipynb) | Autonomous Tool-Calling Agent Assistant with Human-in-the-Loop Approval & Execution Logging | Completed ✅ |
| 09 | [`Projects/09_final_rag_llm_application.ipynb`](./Projects/09_final_rag_llm_application.ipynb) | **Master Enterprise Capstone:** Production-Ready Multi-Agent Enterprise Knowledge Intelligence Platform | Completed ✅ |
