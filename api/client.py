import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
def get_llama_response(description, resume):
    response = requests.post(
        "http://localhost:8000/coverletter/invoke",
        json={'input': {'description': description, 'resume': resume}}
    )
    return response.json()['output']

def get_mistral_response(description):
    response = requests.post(
        "http://localhost:8000/skillsToMention/invoke",
        json={'input': {'description': description}}
    )
    return response.json()['output']

st.title("Application Form Offcampus - Content Generator")

description = st.text_input("Job Description")
resume = st.text_input("Resume")

if st.button("Generate Cover Letter"):
    if description and resume:
        response = get_llama_response(description, resume)
        st.write("Cover Letter: ")
        st.write(response)
    else:
        st.write("Please fill in both Job Description and Resume.")

if st.button("Generate Required Skills"):
    if description:
        response = get_mistral_response(description)
        st.write("Required Skills:")
        st.write(response)
    else:
        st.write("Please provide a Job Description.")


# streamlit run client.py