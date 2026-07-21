# agent/tools.py


from pathlib import Path

from rag.fusion import HybridRetriever

from rag.graph import GraphRetriever

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CHUNKS_PATH = (
    PROJECT_ROOT
    /
    "knowledge"
    /
    "reports"
    /
    "chunks.json"
)
TRIPLE_PATH = (

    PROJECT_ROOT
    /
    "knowledge"
    /
    "triples.json"
)

class TextRetrievalTool:

    """
    文本知识检索

    内部:
    BM25
    +
    Dense
    +
    RRF

    """

    def __init__(self):
        self.retriever = HybridRetriever(
            CHUNKS_PATH
        )


    def run(self,query):
        results = self.retriever.search(
            query,
            top_k=5
        )
        return results
class GraphTool:
    """
    知识图谱检索
    """
    def __init__(self):

        self.retriever = GraphRetriever(
            TRIPLE_PATH
        )

    def run(self,query):
        results = self.retriever.search(
            query,
            top_k=5
        )
        return results