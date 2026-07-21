from typing import TypedDict, List

class AgentState(TypedDict):

    # 用户消息
    messages:List[str]

    # 当前任务
    task_id:str

    # 当前生产单元
    production_unit:str

    # RAG检索结果
    retrieved_docs:List[str]

    # 知识图谱结果
    graph_results:List[str]

    # 最终答案
    answer:str