
🎤 Concert Tour Info Assistant

This project is an intelligent assistant for answering questions about concert tours based on uploaded documents or artist names. It combines document ingestion, summarization, semantic retrieval, and LLM-based Q&A using a RAG architecture. Optionally, it can perform online searches using SerpAPI.

------------------------------------------------------------------------------------------------------------------

 🚀 Features

-  Upload plain-text documents about concert tours
-  Automatic summarization using BART
-  Intelligent question answering using Flan-T5
-  RAG-based semantic search with SentenceTransformers
-  Optional: Online concert search using SerpAPI if no document is provided
-  Simple and modern user interface using **Streamlit**

------------------------------------------------------------------------------------------------------------------

 🧠 Approach

 🔹 Core Functionality (RAG):

1. Document Ingestion:
   - Plain text is uploaded via UI.
   - Document is validated (checks for keywords like "concert", "2025", etc.).
   - Summarized using `facebook/bart-large-cnn`.

2. Storage & Retrieval:
   - Summaries are embedded using `all-MiniLM-L6-v2`.
   - Stored in-memory with NumPy arrays.
   - Semantic similarity is computed using cosine distance.

3. Question Answering:
   - User question is matched against stored summaries.
   - A Flan-T5 model answers the question based on the retrieved context.

 🔹 Bonus Feature (Optional - Dual Functionality):

If no document is uploaded and a user types an artist name:
- Performs online search via SerpAPI.
- Extracts relevant concert events (if any).
- Displays structured information about concert dates, locations, and ticket links.

------------------------------------------------------------------------------------------------------------------

 🛠️ Setup Instructions

 🔧 Requirements

- Python 3.8+
- `pip install -r requirements.txt` OR manually all dependencies in command prompt

> If missing, create `requirements.txt` with:
--------------------------------------
streamlit
transformers
sentence-transformers
numpy
python-dotenv
serpapi
--------------------------------------

 🧪 Local Setup

--------------------------------------
git clone https://github.com/your-username/concert-tour-bot.git
cd concert-tour-bot
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
--------------------------------------

 🔐 Environment Variables

Create a `.env` file in the root directory with:

SERPAPI_API_KEY=your_real_api_key_here


> This is only needed if you enable the optional online search feature.

----------------------------------------------------------------------------

▶️ How to Run

--------------------------------------
In command prompt, type : streamlit run app.py
--------------------------------------

It will open the app in your browser at `http://localhost:8501`.

----------------------------------------------------------------------------

 🌐 Deployment (Streamlit Cloud)

To deploy on Streamlit Cloud:

1. Push the project to GitHub.
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub repo.
4. In the **Secrets** tab, add:
   --------------------------------------
   SERPAPI_API_KEY = "your_real_api_key"
   --------------------------------------
5. Click **Deploy**.

------------------------------------------------------------------------------------------------------------------



- The assistant currently supports plain text documents. PDFs or other formats can be added with minor updates.
- All ML models used are lightweight and can run on CPU.
- Online concert info may not always be structured; fallback links are provided instead.