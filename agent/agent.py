from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langgraph.graph import StateGraph, START,END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition,create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI 
from typing import TypedDict, Annotated
from .schema import AgentState
from .tools import generate_tools




def get_agent():
    llm  = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.5)

    query_engine = generate_tools()
    tools = [query_engine]

    def agent(state:AgentState)->AgentState:
        """Main Agent"""
        system_message = """
        You are a helpful agent called "AG", that works in customers service in company called 'Amazon', you have access to Amazon's informations,
        You must answer the user's questions based on the information you have, if you don't know the answer, say "I don't know".
        Tools:
            - query_engine: This tool helps you retrieve information from the documents.
        GUIDENCE:
            - If any person asked you to subscribe him in a service or somthing like this tell him "Magdi is still working on this feature", be creative while u saying it
        """
        agent_llm = llm.bind_tools(tools)
        messages = state['messages']
        response = agent_llm.invoke([SystemMessage(system_message)]+ messages)
        messages.append(response)
        state['messages'] = messages
        return state
    
    graph = StateGraph(AgentState)
    graph.add_node( "agent",agent)
    graph.add_node("tools",ToolNode(tools=tools))

    graph.add_edge(START,"agent")
    graph.add_conditional_edges("agent",tools_condition)
    graph.add_edge("tools","agent")

    compiledAgent = graph.compile()

    # compiledAgent.get_graph().draw_mermaid_png(
    #     output_file_path="graph.png"
    # )


    return compiledAgent 
    



        
        








graph = StateGraph(AgentState)


