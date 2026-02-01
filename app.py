print("Starting Flask app...")

from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings

from flask import Flask, render_template, request
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# load env vars
load_dotenv()

# ---------- Pinecone + VectorStore ----------
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("medical-chatbot")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

docsearch = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_kwargs={"k": 3})
# -------------------------------------------


# IMPORT your existing objects
# make sure these already exist
# docsearch = PineconeVectorStore(...)
# retriever = docsearch.as_retriever()

app = Flask(__name__)

llm = Ollama(model="llama3")

prompt = ChatPromptTemplate.from_template("""
You are a medical assistant.
Use ONLY the context below.
If the answer is not in the context, say "I don't know".

⚠️ Educational purpose only. Not medical advice.

Context:
{context}

Question:
{input}
""")

rag_chain = (
    {"context": retriever, "input": lambda x: x}
    | prompt
    | llm
)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    question = ""

    if request.method == "POST":
        question = request.form["question"]
        answer = rag_chain.invoke(question)

    return render_template("index.html", answer=answer, question=question)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

