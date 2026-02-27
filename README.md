# 📚 Enterprise Multi-Agent Research RAG System

### Built by Trinadh Kolluboyina

An enterprise-grade, cloud-deployable Multi-Agent Retrieval-Augmented Generation (RAG) system designed for research document analysis.

---

## 🚀 Overview

This project implements a production-style RAG architecture with:

- Hybrid Retrieval (Dense + BM25)
- Cross-Encoder Reranking
- Multi-Agent Architecture (Planner + Generator + Critic)
- Faithfulness Scoring
- Evaluation Dashboard
- Cloud LLM Integration (Groq – LLaMA 3.1)
- Streamlit Deployment Ready

The system enables users to upload multiple research PDFs and ask contextual questions grounded in document evidence.

---

## 🧠 System Architecture

User Query  
→ Planner Agent (Query Optimization)  
→ Hybrid Retrieval (Dense + Sparse)  
→ Cross-Encoder Reranking  
→ Generator Agent (Groq LLM)  
→ Critic Agent (Self-evaluation)  
→ Faithfulness Scoring  
→ Evaluation Dashboard  

---

## 📊 Evaluation Metrics

The system computes:

- Faithfulness Score (Groundedness)
- Context Coverage
- Source Diversity
- End-to-End Latency

This ensures responses are explainable and low-risk for hallucination.

---

## 🏗 Project Structure
enterprise-research-rag/
│
├── app.py
├── requirements.txt
├── core/
├── utils/
├── evaluation/



---

## ⚙️ Installation (Local Setup)

1. Clone the repository:
git clone: 

cd enterprise-research-rag

2. Install dependencies:
3. pip install -r requirements.txt

Create `.streamlit/secrets.toml` (for local testing only):
GROQ_API_KEY="your_api_key_here"

4. Run the app:
streamlit run app.py

---

## ☁ Deployment (Streamlit Cloud)

1. Push project to GitHub.
2. Go to Streamlit Cloud.
3. Create New App.
4. Select repository.
5. Set main file to `app.py`.
6. Add secret in Streamlit Cloud:

---

## ☁ Deployment (Streamlit Cloud)

1. Push project to GitHub.
2. Go to Streamlit Cloud.
3. Create New App.
4. Select repository.
5. Set main file to `app.py`.
6. Add secret in Streamlit Cloud:
GROQ_API_KEY = your_api_key_here

7. Deploy.

---

## 🛠 Tech Stack

- Python
- Streamlit
- FAISS
- BM25 (rank-bm25)
- SentenceTransformers
- CrossEncoder
- Groq API (LLaMA 3.1)
- Multi-Agent Design Pattern

---

## 🎯 Key Highlights

- Modular enterprise architecture
- Agentic reasoning pipeline
- Cloud-ready inference
- Evaluation-focused design
- Production-grade RAG implementation

---

## 📌 Author

Trinadh Kolluboyina  
AI Engineer | Robotics | NLP | Agentic Systems | RAG Architectures

---

