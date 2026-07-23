from langgraph.graph import StateGraph, START, END

from app.agents.state import AgentState
from app.agents.nodes import (
    rewrite_question,
    retrieve_documents,
    generate_answer,
)

builder = StateGraph(AgentState)

builder.add_node(
    "rewrite_question",
    rewrite_question,
)

builder.add_node(
    "retrieve_documents",
    retrieve_documents,
)

builder.add_node(
    "generate_answer",
    generate_answer,
)

builder.add_edge(
    START,
    "rewrite_question",
)

builder.add_edge(
    "rewrite_question",
    "retrieve_documents",
)

builder.add_edge(
    "retrieve_documents",
    "generate_answer",
)

builder.add_edge(
    "generate_answer",
    END,
)

graph = builder.compile()