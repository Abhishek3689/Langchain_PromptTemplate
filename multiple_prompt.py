import os
from dotenv import load_dotenv
import streamlit as st
from langchain.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.chains import SequentialChain

load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv('open_api_key')
llm=openai.OpenAI(temperature=.3)

st.title("Welcome to Our Chat Assistance! I will be happy to help you")
input=st.text_input("Enter the Topic You want to Search")

#prompt Templates
first_input_prompt=PromptTemplate(
    input_variables=['country'],
    template="Tell me  in brief about country {country} ")

chain=LLMChain(llm=llm,prompt=first_input_prompt,verbose=True,output_key='place')

second_input_prompt=PromptTemplate(
    input_variables=['place'],
    template="when was this country got independence  {place} ")
chain2=LLMChain(llm=llm,prompt=second_input_prompt,verbose=True,output_key='date')


third_input_prompt=PromptTemplate(
    input_variables=['date'],
    template="mention 5 major events happened around this  {date} in the world")
chain3=LLMChain(llm=llm,prompt=third_input_prompt,verbose=True,output_key='events')

parent_chain=SequentialChain(
    chains=(chain,chain2,chain3),input_variables=['country'],output_variables=['place','date','events'],
    verbose=True)
if st.button('Submit'):
    if input:
        st.write(parent_chain({'country':input}))