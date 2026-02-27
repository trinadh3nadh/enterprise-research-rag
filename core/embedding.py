from sentence_transformers import SentenceTransformer
from core.config import EMBED_MODEL_NAME

model = SentenceTransformer(EMBED_MODEL_NAME)

def embed(texts):
    return model.encode(texts, convert_to_numpy=True).astype("float32")