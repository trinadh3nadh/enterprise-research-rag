import requests
import streamlit as st

def plan_query(query):

    prompt = f"""
Break down this research question into a focused retrieval query:

{query}

Optimized Query:
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
            "temperature": 0.1
        }
    )

    result = response.json()
    return result["choices"][0]["message"]["content"]