from __future__ import annotations

from typing import Any, List


def rerank(items: List[Any]) -> List[Any]:
    return sorted(items, key=lambda item: str(item), reverse=True)
