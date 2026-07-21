from __future__ import annotations


def split_text(text: str, chunk_size: int = 200) -> list[str]:
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
