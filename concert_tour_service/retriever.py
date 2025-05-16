from sentence_transformers import SentenceTransformer
import numpy as np
import serpapi

model = SentenceTransformer('all-MiniLM-L6-v2')
stored_docs = []

def add_document(summary: str, metadata: dict):
    embedding = model.encode(summary)
    stored_docs.append({
        "summary": summary,
        "embedding": embedding,
        "metadata": metadata
    })

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search(query: str, top_k: int = 3):
    query_embedding = model.encode(query)
    similarities = []
    for doc in stored_docs:
        sim = cosine_similarity(query_embedding, doc["embedding"])
        similarities.append((sim, doc))
    similarities.sort(key=lambda x: x[0], reverse=True)
    return [doc for _, doc in similarities[:top_k]]