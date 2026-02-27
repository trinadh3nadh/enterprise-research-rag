import re

def compute_faithfulness(answer, documents):
    context_text = " ".join([doc["content"] for doc in documents]).lower()
    words = re.findall(r'\w+', answer.lower())

    if not words:
        return 0

    matched = sum(1 for w in words if w in context_text)
    return round((matched / len(words)) * 100, 2)