from __future__ import annotations

GRAPH_NODES = ["router_node", "memory_node", "retrieval_node", "fusion_node", "reasoning_node", "output_node"]
GRAPH_EDGES = [
    ("router_node", "memory_node"),
    ("memory_node", "retrieval_node"),
    ("retrieval_node", "fusion_node"),
    ("fusion_node", "reasoning_node"),
    ("reasoning_node", "output_node"),
]
