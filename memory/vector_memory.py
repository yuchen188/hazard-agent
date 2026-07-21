from __future__ import annotations

from typing import Any


class VectorMemory:
    def __init__(self, ltm: Any) -> None:
        self.ltm = ltm

    def recall(self, query: str, top_k: int = 3) -> list:
        return self.ltm.vector_recall(query, top_k=top_k)
