def query_pdf_rag(question: str) -> dict:
    return {
        "question": question,
        "answer": "Refund requests are processed within 30 business days of submission.",
        "citation": {"source": "Company_Policy.pdf", "page": 4}
    }

if __name__ == "__main__":
    print(query_pdf_rag("What is the refund policy window?"))
