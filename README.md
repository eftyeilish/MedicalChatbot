# MedicalChatbot
# 🩺 Medical RAG Chatbot

A **Retrieval-Augmented Generation (RAG)** based medical chatbot built using  
**LangChain, Pinecone, and a local LLM (Ollama – Llama 3)**.

This project allows users to ask medical questions, and the chatbot answers
**strictly based on provided medical PDFs**, ensuring grounded and contextual responses.

---

## 🚀 Features

- 📄 Uses medical PDFs as a knowledge base  
- 🔍 Vector search with **Pinecone**
- 🧠 Local LLM using **Ollama (Llama 3)** – no OpenAI API required
- 💬 Context-aware question answering (RAG)
- 🔒 No data sent to external LLM APIs
- ⚠️ Educational use only (non-diagnostic)

---

## 🏗️ Project Structure


#clone the repository

git clonehttps://github.com/eftyeilish/MedicalChatbot.git
#create virtual enviroment
conda create -n medibot python = 3.10 -y

pip install -r requirement.txt