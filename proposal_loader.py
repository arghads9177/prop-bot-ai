from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI API key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Define file paths
PROPOSALS_DIR = "knowledge_base/proposals"
CHROMADB_DIR = "proposal_db"

# Function to load and preprocess past proposals
def load_proposals():
    documents = []
    for filename in os.listdir(PROPOSALS_DIR):
        if filename.endswith(".txt"):
            file_path = os.path.join(PROPOSALS_DIR, filename)
            loader = TextLoader(file_path)
            documents.extend(loader.load())
    return documents

# Function to chunk text
def chunk_documents(documents, chunk_size=500, chunk_overlap=50):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunked_docs = text_splitter.split_documents(documents)
    return chunked_docs

# Store embeddings in ChromaDB
def store_in_chromadb(documents):
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(documents, embeddings, persist_directory=CHROMADB_DIR)
    # vectorstore.persist()
    return vectorstore

if __name__ == "__main__":
    print("Loading documents...")
    proposals = load_proposals()
    
    print("Chunking documents...")
    chunked_proposals = chunk_documents(proposals)
    
    print("Storing documents in ChromaDB...")
    vectorstore = store_in_chromadb(chunked_proposals)
    
    print("Document loading pipeline completed successfully!")
