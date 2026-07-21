from langgraph.graph import StateGraph,END
from state.state import AgentState
from agent.nodes import (
    rag_node,
    graph_node,
    generate_node
)
workflow=StateGraph(
    AgentState
)
workflow.add_node(
    "rag",
    rag_node
)
workflow.add_node(
    "graph",
    graph_node
)
workflow.add_node(
    "generate",
    generate_node
)
workflow.set_entry_point(
    "rag"
)
workflow.add_edge(
    "rag",
    "graph"
)
workflow.add_edge(
    "graph",
    "generate"
)
workflow.add_edge(
    "generate",
    END
)
app=workflow.compile()