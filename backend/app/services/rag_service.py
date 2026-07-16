from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from app.core.config import settings
from app.services.vector_service import load_vector_store


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=settings.GROQ_API_KEY,
)


def ask_question(question: str):

    # Load FAISS
    vector_store = load_vector_store()

    # Retrieve relevant chunks
    docs = vector_store.similarity_search(
        question,
        k=4
    )
    print("=" * 60)

    for i, doc in enumerate(docs):
        print(f"Retrieved Chunk {i + 1}")
        print(doc.page_content[:200])

    print("=" * 60)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )


    prompt = ChatPromptTemplate.from_template(
    """
You are an AI assistant.

Answer ONLY using the provided context.

If the answer cannot be found in the context, reply:

"I don't know based on the uploaded documents."

Context:
{context}

Question:
{question}

Answer:
"""
)

    chain = prompt | llm


    response = chain.invoke(
        {
            "context": context,
            "question": question,
        }
    )


    return {
        "answer": response.content,
        "sources": [
            doc.page_content[:200]
            for doc in docs
        ]
    }