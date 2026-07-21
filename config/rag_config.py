from __future__ import annotations

DEFAULT_TOP_K = 3
DEFAULT_FUSION_K = 60
DEFAULT_RERANK_TOP_K = 5


def get_rag_config() -> dict:
    return {
        "top_k": DEFAULT_TOP_K,
        "fusion_k": DEFAULT_FUSION_K,
        "rerank_top_k": DEFAULT_RERANK_TOP_K,
    }
