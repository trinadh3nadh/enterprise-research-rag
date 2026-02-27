from sentence_transformers import CrossEncoder
from core.config import RERANK_MODEL_NAME

model = CrossEncoder(RERANK_MODEL_NAME)

def rerank(query, documents):
    pairs = [[query, doc["content"]] for doc in documents]
    scores = model.predict(pairs)

    ranked = sorted(zip(documents, scores),
                    key=lambda x: x[1],
                    reverse=True)

    return [doc for doc, _ in ranked]