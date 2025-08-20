import streamlit as st
from agent.agent import get_agent
from langchain_core.messages import HumanMessage,AIMessage
import asyncio

st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 LangGraph Chatbot")

if "agent" not in st.session_state:
    with st.spinner("Initializing agent, please wait... (~10 sec)"):
        st.session_state.agent = get_agent()

agent = st.session_state.agent

if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your message..."):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                messages = [
                    HumanMessage(content=content["content"]) 
                    if content["role"] == "user" 
                    else AIMessage(content=content["content"]) 
                    for content in st.session_state.messages
                ]
                result = asyncio.run(agent.ainvoke({"messages": messages}))
            except Exception as e:
                result = f"Error: {e}"

    st.session_state.messages.append({"role": "assistant", "content": result['messages'][-1].content})
    st.rerun()