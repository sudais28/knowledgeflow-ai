from app.services.document_loader import load_document


docs = load_document(
    "uploads/aicvfinal.pdf"
)


print("Number of pages:", len(docs))

print(
    docs[0].page_content[:500]
)