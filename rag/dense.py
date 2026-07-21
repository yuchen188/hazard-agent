from __future__ import annotations

import os
import pickle
from typing import Any

import faiss
import numpy as np

from sentence_transformers import SentenceTransformer


# 本地模型路径
MODEL_PATH = (
    "/root/autodl-tmp/hazard-agent/models/models/"
    "bge-small-zh-v1.5"
)


class DenseRetriever:
    """
    基于FAISS + Embedding模型的稠密检索器

    不使用fallback
    """

    def __init__(
        self,
        documents: list[str] | None = None,
        doc_ids: list[Any] | None = None,
        model_path: str = MODEL_PATH,
        index_path: str | None = None,
    ):

        self.index_path = index_path

        self.documents = []
        self.doc_ids = []

        # 加载embedding模型
        self.model = self._load_model(model_path)

        if index_path and self._index_exists(index_path):

            print("Loading existing FAISS index...")
            self._load(index_path)
        else:
            if documents is None:
                raise ValueError(
                    "首次创建索引必须提供documents"
                )
            self.documents = documents
            self.doc_ids = (
                doc_ids
                if doc_ids is not None
                else list(range(len(documents)))
            )
            self._build_index(
                documents
            )
            if index_path:
                self._save(index_path)
    def _load_model(
        self,
        model_path
    ):
        if not os.path.exists(model_path):

            raise FileNotFoundError(
                f"BGE模型不存在: {model_path}"
            )
        print(
            "Loading local embedding model..."
        )

        model = SentenceTransformer(
            model_path,
            device="cpu"
        )

        print(
            "Embedding model loaded"
        )

        return model

    def _encode(
        self,
        texts:list[str]
    ):

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
            show_progress_bar=False
        )
        embeddings = np.asarray(
            embeddings,
            dtype="float32"
        )

        print(
            "Embedding shape:",
            embeddings.shape
        )
        return embeddings
    def _build_index(
        self,
        documents:list[str]
    ):

        print(
            "Building FAISS index..."
        )
        embeddings = self._encode(
            documents
        )
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(
            dim
        )
        self.index.add(
            embeddings
        )
        print(
            f"FAISS index dimension:{dim}"
        )

    def search(
        self,
        query:str,
        top_k:int=3
    ):
        query_embedding = self._encode(
            [query]
        )
        scores, indices = self.index.search(
            query_embedding,
            top_k
        )
        results=[]
        for score,idx in zip(
            scores[0],
            indices[0]
        ):
            if idx == -1:
                continue
            results.append(
                {
                    "id":
                        self.doc_ids[idx],

                    "text":
                        self.documents[idx],

                    "score":
                        float(score)
                }
            )
        return results
    def add_documents(
        self,
        new_documents:list[str],
        new_doc_ids:list[Any]|None=None
    ):
        new_embeddings=self._encode(
            new_documents
        )

        self.index.add(
            new_embeddings
        )

        ids = (
            new_doc_ids
            if new_doc_ids is not None
            else
            list(
                range(
                    len(self.documents),
                    len(self.documents)+len(new_documents)
                )
            )
        )

        self.documents.extend(
            new_documents
        )
        self.doc_ids.extend(
            ids
        )

        if self.index_path:
            self._save(
                self.index_path
            )



    @staticmethod
    def _index_exists(
        index_path
    ):

        return (
            os.path.exists(
                os.path.join(index_path,"index.faiss")
            )
            and
            os.path.exists(
                os.path.join(index_path,"meta.pkl")
            )
        )



    def _save(
        self,
        index_path
    ):

        os.makedirs(
            index_path,
            exist_ok=True
        )
        faiss.write_index(
            self.index,
            os.path.join(
                index_path,
                "index.faiss"
            )
        )

        with open(
            os.path.join(
                index_path,
                "meta.pkl"
            ),
            "wb"
        ) as f:

            pickle.dump(
                {
                    "documents":self.documents,
                    "doc_ids":self.doc_ids
                },
                f
            )
    def _load(
        self,
        index_path
    ):
        self.index = faiss.read_index(
            os.path.join(
                index_path,
                "index.faiss"
            )
        )
        with open(
            os.path.join(
                index_path,
                "meta.pkl"
            ),
            "rb"
        ) as f:

            meta=pickle.load(f)

        self.documents=meta["documents"]
        self.doc_ids=meta["doc_ids"]

