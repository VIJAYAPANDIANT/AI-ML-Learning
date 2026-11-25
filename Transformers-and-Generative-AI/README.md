<div align="center">

# ⚡ Transformers & Generative AI Masterclass

### *A Production-Grade 45-Notebook Masterclass: From Attention & Transformers to Foundation LLMs, RAG, LoRA, AI Agents & Enterprise GenAI*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Orchestration-1C3C3C?style=for-the-badge)](https://www.langchain.com/)
[![Curriculum](https://img.shields.io/badge/Curriculum-45%20Notebooks-7928CA?style=for-the-badge&logo=gitbook&logoColor=white)](#-master-curriculum-index)
[![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)](#-master-curriculum-index)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](../#--license)

<br/>

<p align="center">
  <b>45 Interactive Notebooks</b> • <b>Attention Mathematics</b> • <b>Pre-training & LoRA Fine-Tuning</b> • <b>Hybrid RAG & Vector DBs</b> • <b>Autonomous AI Agents</b>
</p>

<p align="center">
  <a href="../"><b>🏠 Main Repository</b></a> •
  <a href="#1--nlp--transformer-fundamentals-10-notebooks"><b>🔬 Transformers (10)</b></a> •
  <a href="#2--llm-fundamentals-8-notebooks"><b>🤖 LLM Core (8)</b></a> •
  <a href="#3--generative-ai-paradigms-8-notebooks"><b>🎨 GenAI (8)</b></a> •
  <a href="#4--llm-application-development-11-notebooks"><b>⚙️ Apps & RAG (11)</b></a> •
  <a href="#5--real-world-portfolio-projects-8-notebooks"><b>🏆 Projects (8)</b></a>
</p>

</div>

---

## 📖 Module Overview

The introduction of the **Transformer architecture** ("Attention Is All You Need", 2017) fundamentally transformed artificial intelligence. By replacing recurrent loops with parallel **Multi-Head Self-Attention**, Transformers unlocked the scaling laws that power modern **Large Language Models (LLMs)**, **Multimodal Vision-Language Models**, and **Diffusion Generators**.

This module delivers a comprehensive **45-Notebook Masterclass** designed to take you from foundational tokenization and self-attention tensor mechanics to architecting and serving production-grade enterprise Generative AI systems.

---

## 🗂️ Topic Categories & Curriculum Roadmap

| Category | Important Topics Covered | Notebook Modules |
| :--- | :--- | :--- |
| **NLP Fundamentals** | Text cleaning pipelines, Subword Byte-Pair Encoding (BPE), distributed Word2Vec & GloVe | [`01`](./01_nlp_fundamentals.ipynb) – [`04`](./04_word_embeddings.ipynb) |
| **Transformer Fundamentals** | Scaled Dot-Product Attention ($Q, K, V$), Multi-Head Attention, Positional Encodings, FFNs | [`05`](./05_attention_mechanism.ipynb) – [`09`](./09_positional_encoding.ipynb) |
| **Transformer Models** | Encoder-Only (BERT) vs Decoder-Only (GPT) vs Encoder-Decoder (T5) | [`08`](./08_encoder_and_decoder.ipynb), [`10`](./10_bert_and_gpt_architecture.ipynb) |
| **LLM Fundamentals** | Model parameter scaling laws (7B–70B+), RMSNorm, SwiGLU, RoPE, GQA, token context windows | [`LLM-01`](./LLM-Fundamentals/01_llm_introduction.ipynb) – [`LLM-03`](./LLM-Fundamentals/03_pretraining_and_finetuning.ipynb), [`LLM-05`](./LLM-Fundamentals/05_context_windows_and_tokens.ipynb) |
| **Prompt Engineering** | Zero-shot, Few-shot, Chain-of-Thought (CoT), ReAct reasoning, Self-Consistency | [`LLM-04`](./LLM-Fundamentals/04_prompt_engineering.ipynb), [`App-02`](./LLM-Application-Development/02_prompt_templates.ipynb) |
| **Generative AI** | Autoregressive text synthesis, Latent Diffusion models, GAN minimax game, VAEs, Multimodal CLIP | [`GenAI-01`](./Generative-AI/01_generative_ai_introduction.ipynb) – [`GenAI-08`](./Generative-AI/08_multimodal_ai.ipynb) |
| **Model Development** | Hugging Face Transformers, open weights, 4-bit BitsAndBytes quantization, LoRA, QLoRA | [`LLM-07`](./LLM-Fundamentals/07_huggingface_transformers.ipynb), [`App-08`](./LLM-Application-Development/08_finetuning_llms.ipynb), [`App-09`](./LLM-Application-Development/09_lora_and_qlora.ipynb) |
| **LLM Applications** | REST API client sessions, structured JSON schemas, declarative execution chains | [`App-01`](./LLM-Application-Development/01_llm_api_integration.ipynb), [`App-03`](./LLM-Application-Development/03_chains_and_workflows.ipynb) |
| **RAG** | Vector embeddings, HNSW vector indexes, naive RAG, Hybrid Search (BM25 + Dense) & Cross-Encoder Reranking | [`App-04`](./LLM-Application-Development/04_embeddings_and_vector_search.ipynb) – [`App-07`](./LLM-Application-Development/07_rag_implementation.ipynb) |
| **AI Agents** | Autonomous tool calling, dynamic planning, scratchpad memory, ReAct execution loops | [`App-10`](./LLM-Application-Development/10_ai_agents.ipynb) |
| **Evaluation & Safety** | Hallucination mitigation, RAGAS metrics (Faithfulness, Relevancy), NeMo guardrails, LLM-as-a-Judge | [`App-11`](./LLM-Application-Development/11_llm_evaluation_and_guardrails.ipynb) |

---

## 📁 Repository & Directory Structure

```text
Transformers-and-Generative-AI/
│
├── README.md                                # Master Transformers & GenAI Module documentation
│
├── 01_nlp_fundamentals.ipynb                # Linguistic structure, morphology, syntax & token frequencies
├── 02_text_preprocessing.ipynb              # Cleaning, regex filtering, stopword handling & normalization
├── 03_tokenization.ipynb                    # Subword Byte-Pair Encoding (BPE), WordPiece & SentencePiece
├── 04_word_embeddings.ipynb                 # Word2Vec (Skip-Gram/CBOW), GloVe & cosine vector geometry
├── 05_attention_mechanism.ipynb             # Seq2Seq RNN bottleneck & Bahdanau additive attention
├── 06_self_attention.ipynb                  # Scaled Dot-Product Self-Attention & Multi-Head Attention
├── 07_transformer_architecture.ipynb        # Complete "Attention Is All You Need" architecture block
├── 08_encoder_and_decoder.ipynb             # Encoder-Only (BERT) vs Decoder-Only (GPT) vs Seq2Seq (T5)
├── 09_positional_encoding.ipynb             # Sinusoidal encodings, learnable embeddings & RoPE preview
├── 10_bert_and_gpt_architecture.ipynb       # Masked Language Modeling (MLM) vs Causal Next-Token (CLM)
│
├── LLM-Fundamentals/                        # [8 NOTEBOOKS] Foundation Model Mechanics
│   ├── 01_llm_introduction.ipynb            # Emergence, parameter scaling (7B-70B+) & pretrain/finetune
│   ├── 02_llm_architectures.ipynb           # Modern innovations: RMSNorm, SwiGLU, RoPE, Grouped-Query Attention
│   ├── 03_pretraining_and_finetuning.ipynb  # Self-supervised pretraining, SFT instruction data & DPO alignment
│   ├── 04_prompt_engineering.ipynb          # Zero-shot, few-shot, Chain-of-Thought (CoT) & ReAct reasoning
│   ├── 05_context_windows_and_tokens.ipynb  # Context length, KV cache memory scaling & FlashAttention
│   ├── 06_temperature_and_sampling.ipynb    # Softmax temperature, Top-K, Top-P (Nucleus) & greedy decoding
│   ├── 07_huggingface_transformers.ipynb    # AutoTokenizer, AutoModelForCausalLM, pipeline & Hub models
│   └── 08_using_pretrained_models.ipynb     # Model loading, device_map='auto' & 4-bit/8-bit quantization
│
├── Generative-AI/                           # [8 NOTEBOOKS] Generative Paradigms & Vision
│   ├── 01_generative_ai_introduction.ipynb  # Discriminative P(y|x) vs Generative P(x) density modeling
│   ├── 02_generative_ai_types.ipynb         # Taxonomy: Autoregressive, Diffusion, GANs, VAEs, Flow
│   ├── 03_text_generation.ipynb             # Autoregressive generation, beam search decoding & perplexity
│   ├── 04_image_generation.ipynb            # Pixel-space vs latent-space neural image synthesis
│   ├── 05_diffusion_models.ipynb            # Forward Gaussian noising, reverse U-Net denoising & CFG
│   ├── 06_gan_fundamentals.ipynb            # Generator vs Discriminator minimax game & mode collapse
│   ├── 07_vae_fundamentals.ipynb            # Variational Autoencoders, ELBO loss & Reparameterization Trick
│   └── 08_multimodal_ai.ipynb               # Vision-Language Models, CLIP contrastive learning & projections
│
├── LLM-Application-Development/             # [11 NOTEBOOKS] Production Enterprise Systems
│   ├── 01_llm_api_integration.ipynb         # REST API sessions, Pydantic JSON schemas & rate limit retry
│   ├── 02_prompt_templates.ipynb            # Dynamic prompt templates, variable validation & formatting
│   ├── 03_chains_and_workflows.ipynb        # Sequential pipelines, branching logic & declarative workflows
│   ├── 04_embeddings_and_vector_search.ipynb # Dense vector generation, cosine similarity & k-NN ranking
│   ├── 05_vector_databases.ipynb            # ANN indexing algorithms: HNSW graphs, IVF-PQ & vector stores
│   ├── 06_rag_fundamentals.ipynb            # Retrieval-Augmented Generation: Document chunking & naive RAG
│   ├── 07_rag_implementation.ipynb          # Advanced RAG: Hybrid Search (BM25 + Vector) & Cross-Encoder Rerank
│   ├── 08_finetuning_llms.ipynb             # Full parameter fine-tuning vs PEFT memory budgets
│   ├── 09_lora_and_qlora.ipynb              # Low-Rank Adaptation (LoRA: Delta W = B*A) & 4-bit QLoRA
│   ├── 10_ai_agents.ipynb                   # Autonomous agents, tool/function calling & ReAct execution loops
│   └── 11_llm_evaluation_and_guardrails.ipynb # RAGAS metrics (Faithfulness, Relevancy) & safety guardrails
│
└── Projects/                                # [8 NOTEBOOKS] Real-World Portfolio Applications
    ├── 01_ai_chatbot.ipynb                  # Multi-Turn Conversational Assistant with Sliding Memory Buffer
    ├── 02_document_question_answering.ipynb # Multi-Document Question Answering with Exact Source Citations
    ├── 03_rag_pdf_chatbot.ipynb             # Production Enterprise PDF Document RAG with Vector Search
    ├── 04_ai_resume_analyzer.ipynb          # Automated Resume Parser & Job Description Skill Matcher
    ├── 05_text_summarization.ipynb          # Long-Form Hierarchical Summarization with Map-Reduce Chunking
    ├── 06_semantic_search_engine.ipynb      # Two-Stage Semantic Search Engine (Bi-Encoder + Cross-Encoder)
    ├── 07_ai_research_assistant.ipynb       # Autonomous Multi-Tool Research Agent (ReAct Loop + Citations)
    └── 08_generative_ai_final_project.ipynb # Master Capstone: Enterprise Knowledge Intelligence Platform
```

---

## 📚 Master Curriculum Index

### 1. 🔬 NLP & Transformer Fundamentals (10 Notebooks)

| # | Notebook | Core Theoretical Concept | Code Highlights & APIs |
| :-: | :--- | :--- | :--- |
| **01** | [`01_nlp_fundamentals.ipynb`](./01_nlp_fundamentals.ipynb) | Linguistic hierarchy & morphology | Lexical diversity (Type-Token Ratio) & frequency Counter |
| **02** | [`02_text_preprocessing.ipynb`](./02_text_preprocessing.ipynb) | Cleaning & normalization pipelines | Regex HTML/URL sanitization, Unicode normalization |
| **03** | [`03_tokenization.ipynb`](./03_tokenization.ipynb) | Subword tokenization mechanics | Python implementation of Byte-Pair Encoding (BPE) merges |
| **04** | [`04_word_embeddings.ipynb`](./04_word_embeddings.ipynb) | Distributed continuous vector spaces | Cosine vector similarity & semantic analogy geometry |
| **05** | [`05_attention_mechanism.ipynb`](./05_attention_mechanism.ipynb) | Seq2Seq bottleneck & dynamic context | PyTorch implementation of Bahdanau Additive Attention |
| **06** | [`06_self_attention.ipynb`](./06_self_attention.ipynb) | Scaled Dot-Product Self-Attention | Multi-Head Attention projections & causal attention masking |
| **07** | [`07_transformer_architecture.ipynb`](./07_transformer_architecture.ipynb) | Transformer Block Anatomy | Complete Transformer block with LayerNorm & GELU FFN |
| **08** | [`08_encoder_and_decoder.ipynb`](./08_encoder_and_decoder.ipynb) | Architectural family trade-offs | Encoder-only vs Decoder-only vs Encoder-Decoder taxonomy |
| **09** | [`09_positional_encoding.ipynb`](./09_positional_encoding.ipynb) | Sequence position injection | Sinusoidal frequency encoding calculation & heatmap plotting |
| **10** | [`10_bert_and_gpt_architecture.ipynb`](./10_bert_and_gpt_architecture.ipynb) | Pretraining objective dichotomy | Masked Language Modeling (MLM) vs Causal Next-Token (CLM) |

---

### 2. 🤖 LLM Fundamentals (8 Notebooks)

| # | Notebook | Core LLM Mechanics | Implementation Highlights |
| :-: | :--- | :--- | :--- |
| **01** | [`01_llm_introduction.ipynb`](./LLM-Fundamentals/01_llm_introduction.ipynb) | Parameter scales & emergent reasoning | Tiered model taxonomy (Edge, Mid-weight, Frontier) |
| **02** | [`02_llm_architectures.ipynb`](./LLM-Fundamentals/02_llm_architectures.ipynb) | Modern open-weight innovations | RMSNorm implementation & Grouped-Query Attention (GQA) |
| **03** | [`03_pretraining_and_finetuning.ipynb`](./LLM-Fundamentals/03_pretraining_and_finetuning.ipynb) | Pre-training $\to$ SFT $\to$ Alignment | Formatting structured chat instruction templates for SFT |
| **04** | [`04_prompt_engineering.ipynb`](./LLM-Fundamentals/04_prompt_engineering.ipynb) | In-context reasoning paradigms | Chain-of-Thought (CoT) & ReAct prompt construction |
| **05** | [`05_context_windows_and_tokens.ipynb`](./LLM-Fundamentals/05_context_windows_and_tokens.ipynb) | Attention scaling & KV Caching | KV Cache RAM memory consumption estimation across sequence lengths |
| **06** | [`06_temperature_and_sampling.ipynb`](./LLM-Fundamentals/06_temperature_and_sampling.ipynb) | Logit sampling & stochasticity | Softmax temperature scaling, greedy argmax vs Top-P sampling |
| **07** | [`07_huggingface_transformers.ipynb`](./LLM-Fundamentals/07_huggingface_transformers.ipynb) | Hugging Face Transformers library | `AutoTokenizer`, `AutoModelForCausalLM`, zero-shot `pipeline` |
| **08** | [`08_using_pretrained_models.ipynb`](./LLM-Fundamentals/08_using_pretrained_models.ipynb) | Local model execution & quantization | `device_map='auto'` & 4-bit BitsAndBytes VRAM savings |

---

### 3. 🎨 Generative AI Paradigms (8 Notebooks)

| # | Notebook | Generative Architecture | Mathematical Principles & Demos |
| :-: | :--- | :--- | :--- |
| **01** | [`01_generative_ai_introduction.ipynb`](./Generative-AI/01_generative_ai_introduction.ipynb) | Discriminative vs Generative | Sampling from learned 2D Gaussian density distributions |
| **02** | [`02_generative_ai_types.ipynb`](./Generative-AI/02_generative_ai_types.ipynb) | Taxonomy of modern generative AI | Comparison of Autoregressive, Diffusion, GANs, and VAEs |
| **03** | [`03_text_generation.ipynb`](./Generative-AI/03_text_generation.ipynb) | Autoregressive generation dynamics | Pure Python Beam Search decoder with cumulative log-likelihood |
| **04** | [`04_image_generation.ipynb`](./Generative-AI/04_image_generation.ipynb) | Latent space vs pixel space | Calculating compute savings of Latent Diffusion vs Pixel space |
| **05** | [`05_diffusion_models.ipynb`](./Generative-AI/05_diffusion_models.ipynb) | Forward noising & reverse denoising | Simulating the forward noise schedule ($\bar{\alpha}_t$) |
| **06** | [`06_gan_fundamentals.ipynb`](./Generative-AI/06_gan_fundamentals.ipynb) | Adversarial zero-sum games | PyTorch Generator and Discriminator with LeakyReLU activations |
| **07** | [`07_vae_fundamentals.ipynb`](./Generative-AI/07_vae_fundamentals.ipynb) | Probabilistic latent modeling | Reparameterization Trick ($\mathbf{z} = \mu + \sigma \odot \epsilon$) & ELBO |
| **08** | [`08_multimodal_ai.ipynb`](./Generative-AI/08_multimodal_ai.ipynb) | Vision-Language Foundation Models | CLIP symmetric contrastive similarity loss matrix calculation |

---

### 4. ⚙️ LLM Application Development & RAG (11 Notebooks)

| # | Notebook | Enterprise Capability | Production Code Highlights |
| :-: | :--- | :--- | :--- |
| **01** | [`01_llm_api_integration.ipynb`](./LLM-Application-Development/01_llm_api_integration.ipynb) | API Client Engineering | Structured Pydantic JSON schema payloads & retry backoff |
| **02** | [`02_prompt_templates.ipynb`](./LLM-Application-Development/02_prompt_templates.ipynb) | Dynamic prompt templating | Reusable PromptTemplate class with input variable validation |
| **03** | [`03_chains_and_workflows.ipynb`](./LLM-Application-Development/03_chains_and_workflows.ipynb) | Sequential execution chains | Multi-step compositional execution chain with intermediate inspection |
| **04** | [`04_embeddings_and_vector_search.ipynb`](./LLM-Application-Development/04_embeddings_and_vector_search.ipynb) | Dense vector search | Cosine vector similarity search and semantic document ranking |
| **05** | [`05_vector_databases.ipynb`](./LLM-Application-Development/05_vector_databases.ipynb) | ANN Indexing Algorithms | Exact k-NN benchmark vs HNSW graph & IVF-PQ memory savings |
| **06** | [`06_rag_fundamentals.ipynb`](./LLM-Application-Development/06_rag_fundamentals.ipynb) | Retrieval-Augmented Generation | End-to-end naive RAG prompt augmentation with source grounding |
| **07** | [`07_rag_implementation.ipynb`](./LLM-Application-Development/07_rag_implementation.ipynb) | Advanced RAG Pipelines | Hybrid Search (BM25 + Vector) via Reciprocal Rank Fusion (RRF) |
| **08** | [`08_finetuning_llms.ipynb`](./LLM-Application-Development/08_finetuning_llms.ipynb) | Fine-Tuning Memory Economics | Computing exact VRAM budgets for Full Fine-Tuning vs PEFT |
| **09** | [`09_lora_and_qlora.ipynb`](./LLM-Application-Development/09_lora_and_qlora.ipynb) | Parameter-Efficient Fine-Tuning | PyTorch implementation of LoRA linear layer ($\Delta W = B \cdot A$) |
| **10** | [`10_ai_agents.ipynb`](./LLM-Application-Development/10_ai_agents.ipynb) | Autonomous AI Agents | Autonomous ReAct agent loop with function/tool execution |
| **11** | [`11_llm_evaluation_and_guardrails.ipynb`](./LLM-Application-Development/11_llm_evaluation_and_guardrails.ipynb) | Safety & Quality Evaluation | RAGAS Faithfulness grounding verification & prompt injection shields |

---

### 5. 🏆 Real-World Portfolio Projects (8 Notebooks)

| # | Project | Domain & Architecture | Key Highlights & Deliverables |
| :-: | :--- | :--- | :--- |
| **01** | [`01_ai_chatbot.ipynb`](./Projects/01_ai_chatbot.ipynb) | Stateful Conversational AI | Sliding conversation memory buffer & persona system prompt |
| **02** | [`02_document_question_answering.ipynb`](./Projects/02_document_question_answering.ipynb) | Multi-Document QA | Evidence snippet extraction with exact page coordinates & citations |
| **03** | [`03_rag_pdf_chatbot.ipynb`](./Projects/03_rag_pdf_chatbot.ipynb) | Enterprise Document Intelligence | Production RAG pipeline over multi-page PDF documents |
| **04** | [`04_ai_resume_analyzer.ipynb`](./Projects/04_ai_resume_analyzer.ipynb) | Talent Intelligence NLP | Resume skill extraction and semantic job requirement scoring |
| **05** | [`05_text_summarization.ipynb`](./Projects/05_text_summarization.ipynb) | Long-Form Summarization | Hierarchical Map-Reduce document summarization pipeline |
| **06** | [`06_semantic_search_engine.ipynb`](./Projects/06_semantic_search_engine.ipynb) | Two-Stage Search Engine | Fast Bi-Encoder vector retrieval + accurate Cross-Encoder re-ranker |
| **07** | [`07_ai_research_assistant.ipynb`](./Projects/07_ai_research_assistant.ipynb) | Multi-Tool Autonomous Agent | ReAct loop agent with arXiv search and dynamic note-taking |
| **08** | [`08_generative_ai_final_project.ipynb`](./Projects/08_generative_ai_final_project.ipynb) | **Master Enterprise Capstone** | Autonomous Knowledge Intelligence Platform (RAG + Agents + Guardrails) |

---

## 🎯 Capstone Projects Spotlight

### 1. 📄 Enterprise RAG PDF Document Assistant
📁 **Notebook:** [`Projects/03_rag_pdf_chatbot.ipynb`](./Projects/03_rag_pdf_chatbot.ipynb)  
🛠️ **Tech Stack:** Python, Vector Embeddings, Chunking, Prompt Engineering  
- **Architecture**: Ingests multi-page enterprise PDFs, splits into overlapping semantic chunks, embeds via dense vectors, and executes similarity search.
- **Problem Solved**: Enables corporate teams to converse with technical manuals and compliance documents, ensuring 100% grounded answers with section-level citations.

### 2. 🔬 Autonomous Multi-Tool AI Research Assistant
📁 **Notebook:** [`Projects/07_ai_research_assistant.ipynb`](./Projects/07_ai_research_assistant.ipynb)  
🛠️ **Tech Stack:** Python, ReAct Loop, Tool Calling, Knowledge Synthesis  
- **Architecture**: Implements an autonomous agent with a dynamic scratchpad memory and external tool integration (academic literature search, note persistence).
- **Problem Solved**: Autonomously investigates complex research inquiries, iteratively gathers evidence across multiple queries, and synthesizes structured findings.

### 3. 🏢 Enterprise Generative AI Knowledge Platform (Master Capstone)
📁 **Notebook:** [`Projects/08_generative_ai_final_project.ipynb`](./Projects/08_generative_ai_final_project.ipynb)  
🛠️ **Tech Stack:** Hybrid RAG, Reciprocal Rank Fusion, Cross-Encoder Reranking, LoRA, AI Agents, Guardrails  
- **Architecture**: End-to-end production corporate platform:
  1. *Security Guardrail Layer*: Pre-execution prompt injection, toxic intent, and PII filtration
  2. *Hybrid Retrieval*: Fuses BM25 keyword matching with dense HNSW vector search
  3. *Neural Re-Ranking*: Filters top candidate passages via full cross-attention
  4. *Grounded Synthesis*: Generates cited responses using domain-adapted LLMs
  5. *Enterprise Audit Trail*: Real-time logging of query metadata and faithfulness verification
- **Problem Solved**: Delivers an enterprise-grade, hallucination-resistant knowledge assistant ready for corporate intranet deployment.

---

## 💡 Best Practices for Production Generative AI

```python
# 1. Defend Against Prompt Injection with Layered Guardrails
def sanitize_prompt(user_input: str) -> str:
    injection_patterns = ["ignore previous instructions", "system override", "reveal prompt"]
    if any(p in user_input.lower() for p in injection_patterns):
        raise ValueError("Security violation: Prompt injection detected.")
    return user_input.strip()

# 2. Always Enforce Structured Outputs via Pydantic Schemas
from pydantic import BaseModel, Field

class ExtractedEntity(BaseModel):
    entity_name: str = Field(description="Name of the extracted entity")
    category: str = Field(description="Category: Organization, Person, Date, Metric")
    confidence: float = Field(ge=0.0, le=1.0)

# 3. Ground RAG Generation with Explicit Anti-Hallucination Directives
SYSTEM_RAG_PROMPT = """
You are a factual enterprise assistant.
Rule 1: Answer using ONLY the provided sources below.
Rule 2: If the answer cannot be found in the sources, reply: 'I do not have sufficient information.'
Rule 3: Never extrapolate or speculate beyond the provided sources.
"""
```

---

## 🚀 Environment Setup & Getting Started

```bash
# Clone repository
git clone https://github.com/VIJAYAPANDIANT/AI-ML-Learning.git
cd AI-ML-Learning/Transformers-and-Generative-AI

# Activate virtual environment
# Windows:
..\venv\Scripts\Activate.ps1
# Linux/macOS:
source ../venv/bin/activate

# Install Generative AI & Transformers Dependencies
pip install transformers torch accelerate bitsandbytes
pip install datasets evaluate sentence-transformers
pip install pydantic numpy pandas matplotlib jupyter
```

```bash
# Launch JupyterLab
jupyter lab
```

---

<div align="center">
  <b>Explore Ecosystem:</b> <a href="../Python/">🐍 Python</a> • <a href="../Numpy/">🔢 NumPy</a> • <a href="../Pandas/">📊 Pandas</a> • <a href="../Matplotlib/">📈 Matplotlib</a> • <a href="../Seaborn/">📊 Seaborn</a> • <a href="../Scikit-learn/">⚙️ Scikit-Learn</a> • <a href="../Deep-Learning/">🧠 Deep Learning</a>
</div>
