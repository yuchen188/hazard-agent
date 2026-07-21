from state.state import AgentState

from rag.fusion import HybridRetriever

retriever=HybridRetriever(
    chunks_path=
    "../knowledge/reports/chunks.json"
)
def rag_node(
    state:AgentState
):

    query=state["messages"][-1]

    results=retriever.search(
        query,
        top_k=5
    )

    state["retrieved_docs"]=[
        r["text"]
        for r in results
    ]

    return state
    
from knowledge.graph import GraphRetriever
graph=GraphRetriever(
    "knowledge/triples.json"
)

def graph_node(
    state
):
    query=state["messages"][-1]
    result=graph.search(
        query
    )
    state["graph_results"]=result
    return state
from langchain_openai import ChatOpenAI
llm=ChatOpenAI(
    model="gpt-4o",
    temperature=0.2
)
def generate_node(state):
    prompt=f"""
你是环境风险专家。

参考资料：
{state["retrieved_docs"]}

知识图谱：
{state["graph_results"]}

生成：
{state["messages"][-1]}

"""
    response=llm.invoke(prompt)

    state["answer"]=response.content

    return state