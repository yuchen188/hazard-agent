from __future__ import annotations


def plan_task(query: str) -> dict:
    return {
        "query": query,
        "steps": ["router", "memory", "retrieval", "fusion", "reasoning", "output"],
    }
