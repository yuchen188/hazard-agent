from __future__ import annotations

from app.rag import HybridRAG


class RAGPipeline:
    def __init__(self, retriever: HybridRAG | None = None) -> None:
        self.retriever = retriever or HybridRAG()

    def run(self, query: str) -> dict:
        return self.retriever.run(query)
