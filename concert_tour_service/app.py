import streamlit as st
from document_handler import handle_document
from qa import answer_question
from online_search import search_upcoming_concerts
import serpapi


st.set_page_config(page_title="Concert Tour Info Bot")

st.title("🎤 Concert Tour Info Assistant")

mode = st.radio("Choose an action:", ["Add a document", "Ask a question", "Search for upcoming concerts"])

if mode == "Add a document":
    doc_text = st.text_area("Paste your document about concert tours:")
    if st.button("Submit Document"):
        if doc_text.strip():
            result = handle_document(doc_text)
            st.success(result)
        else:
            st.warning("Please paste some content before submitting.")

elif mode == "Ask a question":
    question = st.text_input("What do you want to know?")
    if st.button("Get Answer"):
        if question.strip():
            answer = answer_question(question)
            st.info(answer)
        else:
            st.warning("Please enter a question first.")

elif mode == "Search for upcoming concerts":
    artist = st.text_input("Enter the artist or band name:")
    if st.button("Search Concerts"):
        if artist.strip():
            result = search_upcoming_concerts(artist)
            st.markdown(result)
        else:
            st.warning("Please enter an artist or band name.")

