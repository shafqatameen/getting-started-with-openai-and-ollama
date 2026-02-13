import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#Langsmith Tracking 
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGSMITH_PROJECT"]=os.getenv("LANGSMITH_PROJECT")

##prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant."),
        ("user","Question:{questions}")
    ]
)
#stream lit framework
st.title("Langchain Demo with gemma")
input_text=st.text_input("Ask Question?")
##Ollama gemma:2b model
llm=Ollama(model="gemma:2b")
out_parser=StrOutputParser()

if input_text:
    st.write(chain.invoke({"questions":input_text}))