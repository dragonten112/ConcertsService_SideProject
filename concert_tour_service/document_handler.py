from transformers import pipeline
from retriever import add_document
import serpapi

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

RELEVANT_KEYWORDS = [
    "concert", "tour", "venue", "schedule", "performance", "2025", "2026", "logistics", "guest", "artist"
]

def is_relevant(document: str) -> bool:
    doc_lower = document.lower()
    return any(keyword in doc_lower for keyword in RELEVANT_KEYWORDS)

def summarize_document(document: str, max_length=130) -> str:
    summary = summarizer(document, max_length=max_length, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def handle_document(document: str) -> str:
    if not is_relevant(document):
        return "❌ Sorry, I cannot ingest documents with other themes."
    
    summary = summarize_document(document)
    add_document(summary, metadata={})
    
    return (
        "✅ Thank you for sharing! Your document has been successfully added to the database.\n\n"
        f"📄 Here is a brief summary of the data from the document:\n{summary}"
    )
