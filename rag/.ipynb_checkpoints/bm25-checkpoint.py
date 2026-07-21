from __future__ import annotations

import re
from typing import Any

try:
    import jieba  # 中文分词，如果是英文可以不用
except ImportError:  # pragma: no cover
    jieba = None
from rank_bm25 import BM25Okapi


class BM25Retriever:
    """基于 rank_bm25 的稀疏检索实现。"""

    def __init__(self, documents: list[str], doc_ids: list[Any] | None = None) -> None:
        """documents: 原始文档文本列表；doc_ids: 与 documents 对应的 id。"""
        self.documents = documents
        self.doc_ids = doc_ids or list(range(len(documents)))
        self.tokenized_corpus = [self._tokenize(doc) for doc in documents]
        self.bm25 = BM25Okapi(self.tokenized_corpus)

    @staticmethod
    def _tokenize(text: str) -> list[str]:
        if jieba is not None:
            return list(jieba.cut(text))
        return re.findall(r"\w+", text.lower())

    def search(self, query: str, top_k: int = 3) -> list[dict]:
        tokenized_query = self._tokenize(query)
        scores = self.bm25.get_scores(tokenized_query)

        ranked_idx = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]
        return [
            {
                "id": self.doc_ids[i],
                "text": self.documents[i],
                "score": float(scores[i]),
            }
            for i in ranked_idx
        ]


