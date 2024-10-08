# 🤖 GenAI Toolkit
> A comprehensive collection of Generative AI implementations using LangChain, Groq, and Google Gemini Pro

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-green.svg)](https://python.langchain.com/)
[![Groq](https://img.shields.io/badge/Groq-API-orange.svg)](https://groq.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)

## 🎯 Project Overview

This repository showcases various implementations of Generative AI applications using modern frameworks and models. From job application generators to multi-RAG agents, this toolkit demonstrates the practical applications of AI in solving real-world problems.

## ✨ Key Features

### 📝 Off-Campus Application Generator
- Generates tailored skill sets based on job descriptions
- Creates custom cover letters using job descriptions and resumes
- Built with LangChain and Groq API
- Frontend: `client.py`, Backend: `api.py`

### 🔍 Multi-RAG Agent
- Implements multiple retrieval tools:
  - 📚 Wikipedia Retriever
  - 📖 Arxiv Retriever
  - 🌐 Custom LangChain Documentation Retriever
- Powered by Google's Gemini Pro
- Uses Google Generative AI embeddings
- FAISS vector database integration

### 📊 Advanced RAG Implementation
- Comprehensive RAG pipeline demonstration
- Multiple loader implementations:
  - Text-based loader
  - Web-based loader
  - PDF loader
- Vector database integration (FAISS)
- Custom chat prompt templates

### 💬 Groq Chatbot
- Streamlit-based interactive interface
- Web-based document loader
- LangChain documentation integration

## 🛠️ Setup Instructions

1. **Create and activate a Conda environment**
```bash
conda create -n chat_assist python=3.10 anaconda
conda activate chat_assist
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure Environment Variables**
```env
LANGCHAIN_API_KEY=xxx
LANGCHAIN_PROJECT=ProjectName
GOOGLE_API_KEY=xxx
GROQ_API_KEY=xxx
```

## 🎥 Demo

![Demo](https://github.com/RaghavMangla/Gen-AI/assets/GenAIVideo.mov)

## 📁 Project Structure
```
.
├── api/
│   ├── api.py          # Backend implementation
│   └── client.py       # Frontend implementation
├── agents.py           # Multi-RAG agent implementation
├── rag/
│   └── advanced_rag.ipynb  # RAG pipeline demonstration
├── groq/               # Groq-specific implementations
└── requirements.txt
```

## 🔧 Technologies Used

- LangChain Framework
- Groq API
- Google Gemini Pro
- FAISS and ChromaDB Vector Database
- Streamlit
- Google Generative AI
- Wikipedia Wrapper by Langchain
- Arxiv API Wrapper by Langchain
