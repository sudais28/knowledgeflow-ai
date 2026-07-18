from langgraph.graph import StateGraph, START, END
from app.agents.state import AgentState

from app.agents.nodes import (
    rewrite_question,
    retrieve_documents,
    grade_documents,
    generate_answer,
    no_answer,
    should_answer,
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

# 👇 ADD THIS
builder.add_node(
    "grade_documents",
    grade_documents,
)

builder.add_node(
    "generate_answer",
    generate_answer,
)

builder.add_node(
    "no_answer",
    no_answer,
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
    "grade_documents",
)

builder.add_conditional_edges(
    "grade_documents",
    should_answer,
)

builder.add_edge(
    "generate_answer",
    END,
)

builder.add_edge(
    "no_answer",
    END,
)

graph = builder.compile()