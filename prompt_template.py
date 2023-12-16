import os
from dotenv import load_dotenv
import streamlit as st
from langchain.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv('open_api_key')
llm=openai.OpenAI(temperature=.3)

st.title("Welcome to Our Chat Assistance! I will be happy to help you")
input=st.text_input("Enter the Topic You want to Search")

#prompt Templates
first_input_prompt=PromptTemplate(
    input_variables=['country'],
    template="Tell me in 5 to 10 lines about country {country} ")

chain=LLMChain(llm=llm,prompt=first_input_prompt,verbose=True)

if input:
    st.write(chain.run(input))