from transformers import pipeline
from retriever import search
import serpapi

qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

def answer_question(question: str):
    docs = search(question)
    if not docs or all(doc['summary'].strip() == '' for doc in docs):
        return "I'm sorry, I couldn't find any relevant information related to your question."
    
    context = " ".join(doc["summary"] for doc in docs)
    prompt = f"Answer the question based on this context: {context}\nQuestion: {question}"
    response = qa_pipeline(prompt, max_length=100)
    return response[0]['generated_text']
