import streamlit as st
import time

from core.hybrid_retriever import hybrid_search
from core.reranker import rerank
from core.agent import agentic_pipeline
from core.config import TOP_K
from utils.document_loader import load_documents
from evaluation.metrics import compute_context_coverage, retrieval_diversity
from evaluation.dashboard import show_dashboard


# =============================
# PAGE CONFIG
# =============================
st.set_page_config(layout="wide")

# =============================
# CUSTOM STYLING
# =============================
st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: 800;
}
.author-name {
    font-size: 22px;
    font-weight: 600;
    color: #2e7d32;
}
.stButton>button {
    background-color: #2e7d32;
    color: white;
    font-weight: 600;
    border-radius: 8px;
    height: 3em;
    width: 150px;
}
.stButton>button:hover {
    background-color: #1b5e20;
    color: white;
}
</style>
""", unsafe_allow_html=True)


# =============================
# TITLE
# =============================
st.markdown('<div class="main-title">📚 Enterprise Multi-Agent Research RAG System</div>', unsafe_allow_html=True)
st.markdown('<div class="author-name">Built by Trinadh Kolluboyina</div>', unsafe_allow_html=True)

st.markdown("---")


# =============================
# FILE UPLOAD
# =============================
uploaded_files = st.file_uploader(
    "Upload Research PDFs",
    type="pdf",
    accept_multiple_files=True
)


# =============================
# QUESTION INPUT
# =============================
query = st.text_input("Ask a question")

submit = st.button("Submit")


# =============================
# MAIN PIPELINE
# =============================
if uploaded_files and query and submit:

    start = time.time()

    documents = load_documents(uploaded_files)

    retrieved = hybrid_search(query, documents, TOP_K)
    reranked = rerank(query, retrieved)

    # =============================
    # RETRIEVED EVIDENCE (Clean Fix)
    # =============================
    st.subheader("🔎 Retrieved Evidence")

    for doc in reranked[:3]:
        with st.expander(f"📄 {doc['source']} — Chunk {doc['chunk_id']}"):
            st.write(doc["content"][:1000])

    # =============================
    # GENERATION
    # =============================
    st.subheader("🧠 Generating Answer...")
    answer, faith_score = agentic_pipeline(query, reranked)

    # =============================
    # FINAL ANSWER
    # =============================
    st.subheader("🧠 Final Answer")
    st.success(answer)

    # =============================
    # DASHBOARD
    # =============================
    coverage = compute_context_coverage(query, reranked)
    diversity = retrieval_diversity(reranked)

    metrics_dict = {
        "faithfulness": faith_score,
        "coverage": coverage,
        "diversity": diversity,
        "latency": round(time.time() - start, 2)
    }

    show_dashboard(metrics_dict)