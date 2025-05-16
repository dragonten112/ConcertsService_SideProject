from document_handler import is_relevant, summarize_document
from retriever import add_document
from qa import answer_question


def ingest_document(doc_text: str):
    if not is_relevant(doc_text):
        return "Sorry, I cannot ingest documents with other themes."
    summary = summarize_document(doc_text)
    add_document(summary, metadata={})
    return f"Thank you for sharing! Your document has been successfully added to the database.\nHere is a brief summary of the data from the document:\n{summary}"

def main():
    print("Welcome to the Concert Tour Info Service!")
    while True:
        user_input = input("Enter command (or 'exit'): ")
        if user_input.lower() == 'exit':
            break
        elif user_input.lower().startswith("add "):
            doc = user_input[4:]
            print(ingest_document(doc))
        else:
            print(answer_question(user_input))

if __name__ == "__main__":
    main()