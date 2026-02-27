from rank_bm25 import BM25Okapi
import numpy as np

def bm25_search(query, documents, top_k):
    tokenized = [doc["content"].split() for doc in documents]
    bm25 = BM25Okapi(tokenized)

    scores = bm25.get_scores(query.split())
    top_indices = np.argsort(scores)[-top_k:]

    return [documents[i] for i in top_indices]