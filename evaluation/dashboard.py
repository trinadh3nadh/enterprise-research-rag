import streamlit as st

def show_dashboard(metrics_dict):

    st.subheader("📊 RAG Evaluation Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Faithfulness", f"{metrics_dict['faithfulness']}%")
    col2.metric("Context Coverage", f"{metrics_dict['coverage']}%")
    col3.metric("Source Diversity", metrics_dict['diversity'])

    st.write("Latency (seconds):", metrics_dict["latency"])