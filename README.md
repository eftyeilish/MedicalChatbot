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



---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/MedicalChatbot.git
cd MedicalChatbot

#Create Python Environment
conda create -n medicalbot python=3.10 -y
conda activate medicalbot
pip install -r requirement.txt

#Install Ollama (Local LLM)
ollama pull llama3


#Add Environment Variables
PINECONE_API_KEY=your_pinecone_api_key_here

#Run the Application
python app.py

