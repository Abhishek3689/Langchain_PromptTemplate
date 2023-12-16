import os
from dotenv import load_dotenv
import streamlit as st
from langchain.llms import openai


load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv('open_api_key')

llm=openai.OpenAI(temperature=.3)

st.set_page_config(page_title="Welcome to Home Page of Openai LLM")
st.header("Chat with Open Ai Model with Ease")
input=st.text_input("Please ask the question")

if st.button('Submit'):
    if input:
        st.write(llm(input))
    else:
        st.write('please enter the question')