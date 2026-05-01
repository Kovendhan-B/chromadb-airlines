import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "src"))
from query import search
from llm import answer_question

st.title("Chroma Airlines RAG")
st.write("Ask a question about airline reviews and get an answer powered by LLM and ChromaDB.")

user_query = st.text_input("Enter your question:")

if st.button("Get Answer") and user_query:
    with st.spinner("Searching and generating answer..."):
        results = search(user_query)
        docs = [doc for doc, _ in results]
        if docs:
            answer = answer_question(user_query, docs)
            st.subheader("Answer:")
            st.write(answer)
            st.subheader("Top Relevant Documents:")
            for i, doc in enumerate(docs, 1):
                st.markdown(f"**Doc {i}:** {doc}")
        else:
            st.warning("No relevant documents found.")
