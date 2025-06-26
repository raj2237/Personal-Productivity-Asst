import os
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH","db")

documents = [
    Document(page_content="Meeting Notes: Discuss project X deliverables"),
    Document(page_content = "Reminder: Submit report by Friday"),
    Document(page_content="Tech conference Next Wednesday!"),
]

embedding_model = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")

text_splitter = CharacterTextSplitter(chunk_size= 200, chunk_overlap = 50)
docs = text_splitter.split_documents(documents)


vector_db = Chroma.from_documents(docs, embedding=embedding_model, persist_directory=CHROMA_DB_PATH)

print("Documents successfully indexed")