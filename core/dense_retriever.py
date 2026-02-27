import faiss
import numpy as np
from core.embedding import embed

def dense_search(query, documents, top_k):
    embeddings = embed([doc["content"] for doc in documents])

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    q_vec = embed([query])
    _, indices = index.search(q_vec, top_k)

    return [documents[i] for i in indices[0]]