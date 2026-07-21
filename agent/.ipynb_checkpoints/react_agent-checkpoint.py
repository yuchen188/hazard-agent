# agent/react_agent.py
from agent.router import Router
from agent.tools import (
    TextRetrievalTool,
    GraphTool
)

class ReactAgent:
    def __init__(
        self,
        llm
    ):
        self.llm = llm
        self.router = Router()
        self.tools = {
            "text":
                TextRetrievalTool(),
            "graph":
                GraphTool()
        }
    def run(self,query):
        print("\nQuestion:")
        print(query)
        # =========
        # Thought
        # =========
        route = self.router.route(query)
        print(
            "\nThought:",
            f"选择{route}检索路径"
        )
        observations=[]
        # ==================
        # Action
        # ==================
        if route=="text":
            result = self.tools["text"].run(
                query

            )
            observations.extend(result)
        elif route=="graph":
            result = self.tools["graph"].run(
                query
            )
            observations.extend(result)
        elif route=="both":
            text_result = self.tools["text"].run(
                query
            )
            graph_result = self.tools["graph"].run(
                query
            )
            observations.extend(text_result)
            observations.extend(graph_result)
        print(
            "\nObservation:"
        )
        for item in observations:
            print(item)
        # ============
        # Final
        # ============
        answer=self.generate_answer(
            query,
            observations
        )
        return answer
    def generate_answer(
        self,
        query,
        contexts
    ):

        prompt=f"""


            你是一名环境污染隐患排查专家。
            
            用户问题:
            
            {query}
            
            知识:
            {contexts}
            
            请根据知识回答。
            
            """
        answer = self.llm.generate(
            prompt
        )

        return answer