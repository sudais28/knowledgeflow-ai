from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from app.agents.state import AgentState
from app.core.config import settings
from app.services.vector_service import load_vector_store


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=settings.GROQ_API_KEY,
)


def rewrite_question(state: AgentState):

    prompt = ChatPromptTemplate.from_template(
        """
You are an AI assistant that rewrites search queries.

Rules:
- Preserve the original meaning.
- Do not answer the question.
- Return only the rewritten question.
- If the question is already clear, return it unchanged.

Current Question:
{question}
"""
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "question": state["question"],
        }
    )

    return {
        "rewritten_question": response.content.strip(),
    }


def retrieve_documents(state: AgentState):

    vector_store = load_vector_store(state["user_id"])

    print("=" * 60)
    print("Original Question:", state["question"])
    print("Rewritten Question:", state["rewritten_question"])
    print("=" * 60)

    docs = vector_store.similarity_search(
        state["rewritten_question"],
        k=4,
    )

    print("=" * 60)
    print(f"Retrieved {len(docs)} documents")

    for i, doc in enumerate(docs):
        print(f"\nDocument {i + 1}")
        print("Metadata:", doc.metadata)
        print(doc.page_content[:300])

    print("=" * 60)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    return {
        "documents": docs,
        "context": context,
    }



def generate_answer(state: AgentState):

    prompt = ChatPromptTemplate.from_template(
        """
You are KnowledgeFlow AI.

You MUST answer ONLY using the provided context.

If the context contains the answer,
answer naturally.

If the answer truly cannot be found in the context,
reply exactly:

I don't know based on the uploaded documents.

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
            "context": state["context"],
            "question": state["rewritten_question"],
        }
    )

    print("=" * 60)
    print("LLM ANSWER")
    print(response.content)
    print("=" * 60)

    return {
        "answer": response.content.strip(),
    }
