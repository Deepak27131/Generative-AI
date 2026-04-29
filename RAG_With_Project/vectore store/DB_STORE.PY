from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# 📄 Load PDF
data = PyPDFLoader('Document_loader/deeplearning.pdf')
doc = data.load()

# ✅ (optional but recommended) remove empty pages
doc = [d for d in doc if d.page_content.strip() != ""]

# ✂️ Split into chunks (VERY IMPORTANT for RAG)
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

doc = splitter.split_documents(doc)

# 🔍 Embedding
# embeddings = GoogleGenerativeAIEmbeddings(
#     model="gemini-embedding-001"
# )

embedding_model = MistralAIEmbeddings(model="mistral-embed")

# 🧠 Vector Store
vectorstore = Chroma.from_documents(
    documents=doc,
    embedding=embedding_model,
    persist_directory="chroma-db"
)

result = vectorstore.similarity_search("what is main purpose of deep learning and what is working of CNN?",k=5)

for r in result:
    print(r.page_content)
print()
print("--------------------------------------")

# retriver retrive the question answer 
retriver = vectorstore.as_retriever()

result2 = retriver.invoke("Explain the RNN")

for d in result2:
    print(d.page_content)
    print(d.metadata)
# print("Total chunks:", len(doc))
# print(doc[0])