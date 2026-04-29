from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader("Document_loader/GRU.pdf")

doc = data.load()


print(len(doc))