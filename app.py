# app.py

import streamlit as st
from scrapper import scrape_text_from_url
from chunker import chunk_text
from store import add_document
from query import retrieve_and_answer

st.title("🔍 Webpage Knowledgebase Chatbot")

st.subheader("Select Mode:")
mode = st.radio("Choose what you want to do:", ["Ingest URL", "Chat with Data"], horizontal=True)

if mode == "Ingest URL":
    st.subheader("📥 Add Website Content")
    url = st.text_input("Enter website URL")
    if st.button("Scrape & Index"):
        try:
            text = scrape_text_from_url(url)
            chunks = chunk_text(text)
            add_document(url, chunks)
            st.success(f"Indexed {len(chunks)} chunks from {url}")
        except Exception as e:
            st.error(f"Failed to ingest URL: {e}")

else:  # Chat mode
    st.subheader("💬 Ask Questions")
    q = st.text_input("Your question")
    if st.button("Ask"):
        try:
            answer = retrieve_and_answer(q)
            st.markdown(f"**Answer:** {answer}")
        except Exception as e:
            st.error(f"Failed to get answer: {e}")

st.write("Created by: ZAHOOR AHMAD | AI Developer")