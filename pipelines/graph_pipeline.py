from __future__ import annotations

from typing import Any


class GraphPipeline:
    def __init__(self, agent: Any) -> None:
        self.agent = agent

    def run(self, query: str) -> dict:
        return self.agent.run(query)
