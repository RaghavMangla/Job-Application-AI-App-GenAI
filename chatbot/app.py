from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama # Correct the import
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Creating prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please provide response to the user queries"),
        ("user", "Question:{question}")
    ]
)

# Streamlit framework
st.title("Langchain Demo with Llama 3 API")
input_text = st.text_input("Search the topic you want")

# Correctly instantiate the Ollama LLM
llm = Ollama(model="llama3:8b-instruct-q3_K_M")
output_parser = StrOutputParser()

# Chain the prompt, LLM, and parser
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
