# Concert Tour Info Service

This is a Python service that helps manage and retrieve information from domain-specific documents related to concert tours in 2025–2026.

## How to Use

1. Install dependencies:
    pip install -r requirements.txt

2. Run the service:
    python main.py

3. Commands:
- Add a document: `add Lady Gaga will tour Europe in Autumn 2025. She will perform in Paris, Berlin, and Rome.`
- Ask a question: `Where is Lady Gaga planning to give concerts during autumn 2025?`

## Notes

- All answers are grounded in the ingested documents.
- Only documents related to concert tours will be accepted.