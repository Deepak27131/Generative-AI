# load data or pdf
# split into chunks
# create embedding 
#store embeddding into vectore store is chroma 

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

# 📄 Load PDF
data = PyPDFLoader('Document_loader/deeplearning.pdf')
docs = data.load()

# splitting data into chunk
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)

chunks = splitter.split_documents(docs)

# create embedding of each chunks

embedding_model = MistralAIEmbeddings(model = "mistral-embed")


# store each chunks and embedding vector in store vectore are called chroma 

vectorestore = Chroma.from_documents(
    documents=chunks,
    embedding= embedding_model,
    persist_directory='chroma_db1'
)