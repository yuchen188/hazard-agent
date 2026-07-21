from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List
import json
try:
    from .bm25 import BM25Retriever
    from .dense import DenseRetriever

except ImportError:
    from bm25 import BM25Retriever
    from dense import DenseRetriever



PROJECT_ROOT = Path(__file__).resolve().parent.parent

CHUNKS_PATH = PROJECT_ROOT / "knowledge" / "reports" / "chunks.json"


FAISS_PATH = (
    Path(__file__).parent / "faiss_index"
)

def load_documents(path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        chunks = json.load(f)

    documents = [
        chunk["text"]
        for chunk in chunks
    ]

    return documents

class HybridRetriever:
    def __init__(self, chunks_path):

        with open(chunks_path, "r", encoding="utf-8") as f:
            self.chunks = json.load(f)

        self.documents = [
            chunk["text"]
            for chunk in self.chunks
        ]

        print("Loading BM25...")
        self.bm25 = BM25Retriever(
            documents=self.documents
        )

        print("Loading Dense...")
        self.dense = DenseRetriever(
            documents=self.documents,
            index_path=str(FAISS_PATH)
        )

        print("Retriever loaded")

    def rrf(
        self,
        dense_results,
        bm25_results,
        k=60
    ):
        scores={}
        docs={}

        for result_list in [
            dense_results,
            bm25_results
        ]:
            for rank,item in enumerate(
                result_list,
                start=1
            ):
                doc_id=item["id"]
                scores[doc_id]=(
                    scores.get(doc_id,0)
                    +
                    1/(k+rank)
                )

                docs[doc_id]=item

        ranked=sorted(
            scores.items(),
            key=lambda x:x[1],
            reverse=True
        )
        output=[]
        for doc_id,score in ranked:
            output.append(
                {
                    "id":doc_id,
                    "text":
                    docs[doc_id]["text"],
                    "score":
                    score
                }
            )
        return output

    def search(
        self,
        query,
        top_k=3
    ):

        dense_results = self.dense.search(
            query,
            top_k
        )

        bm25_results = self.bm25.search(
            query,
            top_k
        )

        results=self.rrf(
            dense_results,
            bm25_results
        )

        return results[:top_k]



if __name__=="__main__":


    retriever=HybridRetriever(
        CHUNKS_PATH
    )

    query="国家相关法律法规、技术规范等"

    results=retriever.search(
        query,
        top_k=3
    )
    print(
        "\n查询:",
        query
    )
    for r in results:
        print(
            f"id={r['id']} "
            f"score={r['score']:.4f} "
            f"text={r['text']}"
        )