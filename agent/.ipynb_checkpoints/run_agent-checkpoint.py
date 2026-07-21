from agent.react_agent import ReactAgent
from agent.llm import LLM
llm = LLM()
agent = ReactAgent(
    llm
)
answer = agent.run(
    "熄焦有哪些主要风险物质？"
)
print(answer)