import os
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.chains.question_answering import load_qa_chain
 

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH","db")

embedding_model = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
vector_db = Chroma(persist_directory=CHROMA_DB_PATH , embedding_function=embedding_model)
retriever = vector_db.as_retriever()


llm = ChatGroq(model = "gemma2-9b-it")

qa_chain = load_qa_chain(
    llm = llm,
    chain_type="stuff"
)

def get_response(query):
    docs = retriever.get_relevant_documents(query)  
    return qa_chain.run(input_documents = docs, question = query)