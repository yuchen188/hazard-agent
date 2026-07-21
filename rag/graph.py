from __future__ import annotations

import json
from pathlib import Path


class GraphRetriever:

    def __init__(self, triples_path):

        with open(
            triples_path,
            "r",
            encoding="utf-8"
        ) as f:

            self.triples = json.load(f)

        print(
            f"Loaded {len(self.triples)} triples."
        )

    def search(
        self,
        query,
        top_k=10
    ):

        results=[]

        for idx,triple in enumerate(self.triples):

            head=triple["head"]

            relation=triple["relation"]

            tail=triple["tail"]

            score=0

            if head in query:

                score+=2

            if tail in query:

                score+=1

            if relation in query:

                score+=1

            if score>0:

                results.append(

                    {

                        "id":idx,

                        "text":f"{head} -> {relation} -> {tail}",

                        "score":score

                    }

                )

        results.sort(

            key=lambda x:x["score"],

            reverse=True
        )
        return results[:top_k]

if __name__=="__main__":

    PROJECT_ROOT=Path(__file__).resolve().parent.parent

    triples_path=PROJECT_ROOT/"knowledge"/"triples.json"

    retriever=GraphRetriever(triples_path)

    query="熄焦有哪些主要风险物质"

    results=retriever.search(query)

    print(results)