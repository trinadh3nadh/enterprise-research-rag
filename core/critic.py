import requests
import streamlit as st

def critique_answer(answer):

    prompt = f"""
Evaluate the following answer.
Is it fully grounded in context? Respond YES or NO.

Answer:
{answer}
"""

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {st.secrets['GROQ_API_KEY']}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.1-8b-instant",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0
        }
    )

    result = response.json()
    return result["choices"][0]["message"]["content"]