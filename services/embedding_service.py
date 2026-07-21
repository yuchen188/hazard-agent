from __future__ import annotations


class EmbeddingService:
    def __init__(self) -> None:
        self.model_name = "text-embedding-3-small"

    def embed(self, text: str) -> list:
        return [float(len(text))]
