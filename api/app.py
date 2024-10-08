from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="API Server"
)

llm = Ollama(model="llama3:8b-instruct-q3_K_M")


prompt_coverletter = ChatPromptTemplate.from_template(
    "Write me a cover letter in less than 200 words for Company based on its {description} and my resume {resume}"
)
prompt_skills = ChatPromptTemplate.from_template(
    "Mention the skills in the present market scenario required for this job description {description}"
)

add_routes(
    app,
    prompt_coverletter | llm,
    path='/coverletter'
)

add_routes(
    app,
    prompt_skills | llm,
    path='/skillsToMention'
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)


#  python3 -m streamlit run app.py