from __future__ import annotations

from typing import Any


class KGMemory:
    def __init__(self, ltm: Any) -> None:
        self.ltm = ltm

    def query(self, entity: str, top_k: int = 3) -> list:
        return self.ltm.kg_query(entity, top_k=top_k)

    def expand(self, entity: str, top_k: int = 3) -> list:
        return self.ltm.kg_expand(entity, top_k=top_k)
