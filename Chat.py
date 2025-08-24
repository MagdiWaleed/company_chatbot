import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
import asyncio
import requests

BASE_URL = "https://5000-dep-01k3dct5xvdwnmrmj5vyyrnx3g-d.cloudspaces.litng.ai"

def chat(message:str):
    global BASE_URL
    url = f"{BASE_URL}/chatbot_agent/"
    token =st.session_state.token
    
    parameter = {
        "token":token,
        "message":message
        }
    response = requests.post(url, json=parameter)

    return response.json()["message"]
if "token" not in st.session_state:
    token = "not-authorized"
else:
    token = st.session_state['token']

st.set_page_config(page_title="Amazon", layout="centered")
st.title("Amazon Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your message..."):
    if  token == "not-authorized":
        st.error("Your Are Not Authorized")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    result = chat(prompt)
                except Exception as e:
                    result = f"Error: {e}"

        st.session_state.messages.append({"role": "assistant", "content": result})
        st.rerun()