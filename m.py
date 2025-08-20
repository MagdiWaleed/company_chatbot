from agent.agent import get_agent
from langchain_core.messages import HumanMessage,AIMessage

agent = get_agent()

print(agent.invoke({"messages":[HumanMessage("hi")]}))