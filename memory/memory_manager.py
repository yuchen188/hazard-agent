from __future__ import annotations

from typing import Any

from .kg_memory import KGMemory
from .stm import STM
from .vector_memory import VectorMemory


class MemoryManager:
    def __init__(self, ltm: Any) -> None:
        self.stm = STM()
        self.vector = VectorMemory(ltm)
        self.kg = KGMemory(ltm)
