import requests
import streamlit as st

GROQ_MODEL = "llama-3.1-8b-instant"

def generate_answer(query, documents):

    context = "\n\n".join(
        [f"[{doc['source']} - chunk {doc['chunk_id']}]\n{doc['content']}"
         for doc in documents[:3]]
    )

    prompt = f"""
You are a research assistant.

Answer ONLY using the context below.
If the answer is not present, say:
"I cannot find sufficient information."

Cite sources in brackets like [filename - chunk X].

Context:
{context}

Question:
{query}

Answer:
"""

    headers = {
        "Authorization": f"Bearer {st.secrets['GROQ_API_KEY']}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json={
            "model": GROQ_MODEL,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.2,
            "max_tokens": 500
        },
        timeout=60
    )

    result = response.json()

    if "choices" in result:
        return result["choices"][0]["message"]["content"]

    return f"Groq Error: {result}"