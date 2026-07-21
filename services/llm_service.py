from __future__ import annotations

from typing import Any, Optional


class LLMService:
    def __init__(self, llm: Optional[Any] = None) -> None:
        self.llm = llm

    def invoke(self, prompt: Any) -> Any:
        if self.llm is None:
            return {"content": str(prompt)}
        return self.llm.invoke(prompt)
