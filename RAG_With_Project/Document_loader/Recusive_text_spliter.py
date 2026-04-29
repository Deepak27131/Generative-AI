from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


data = PyPDFLoader("Document_loader\GRU.pdf")

splitter = RecursiveCharacterTextSplitter (
    # separator="",
    chunk_size = 100,
    chunk_overlap = 10
)

doc = data.load()

chunks = splitter.split_documents(doc)

print(len(chunks))

for i in chunks:
    print(i.page_content)
    print()