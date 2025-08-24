import streamlit as st
import requests

BASE_URL = "http://192.168.100.14:5000"


def signIn(email:str,password:str):
    global BASE_URL
    url = f"{BASE_URL}/sign-in/"
    parameter = {
        "email":email,
        "password":password
        }
    response = requests.post(url, json=parameter)
    data = response.json()
    if "token" in data.keys():
        st.success("Sign In Successfully.")
        st.session_state['token']= data['token']
        st.session_state['email']= email
        st.session_state['password'] = password
        if "messages" in st.session_state:
            st.session_state['messages'] = []
    else:
        st.error(data['error'])
    

def signUp(email:str,password:str,name:str,money:float):
    global BASE_URL
    url = f"{BASE_URL}/sign-up/"
    parameter = {
        "email":email,
        "password":password,
        "name":name,
        "money":money
        }
    response = requests.post(url, json=parameter)
    data = response.json()
    if "message" in data.keys():
        st.success(data['message'])
    else:
        st.error(data['error'])

if "email" in st.session_state:
    email =st.text_input("Enter Your Email",value=st.session_state.email)
else:
    email =st.text_input("Enter Your Email")

if "password" in st.session_state:
    password =st.text_input("Enter Your Password",value=st.session_state.password)
else:
    password =st.text_input("Enter Your Password")

colum1,colum2 = st.columns(2)
signInButton = st.button("Sign In")
if signInButton:
    signIn(email,password)

@st.dialog("Create Account")
def create_account():
    name = st.text_input("Enter Your Name")
    email =st.text_input("Enter Your Email")
    password =st.text_input("Enter Your Password")
    money =st.number_input("Enter Your money")

    if st.button("Submit"):
        signUp(email,password,name,money)


if st.button("You Don't Have Account"):
    create_account()
