import time
import numpy as np

def compute_context_coverage(query, documents):
    query_terms = query.lower().split()
    context = " ".join([doc["content"] for doc in documents]).lower()

    matched = sum(1 for term in query_terms if term in context)
    return round((matched / len(query_terms)) * 100, 2)

def retrieval_diversity(documents):
    sources = set(doc["source"] for doc in documents)
    return len(sources)