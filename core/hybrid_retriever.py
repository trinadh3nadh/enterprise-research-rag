from core.dense_retriever import dense_search
from core.sparse_retriever import bm25_search

def hybrid_search(query, documents, top_k):
    dense_results = dense_search(query, documents, top_k)
    sparse_results = bm25_search(query, documents, top_k)

    merged = {id(doc): doc for doc in dense_results + sparse_results}
    return list(merged.values())