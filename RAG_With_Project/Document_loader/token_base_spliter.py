from langchain_text_splitters import TokenTextSplitter

from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader('GRU.pdf')

splitter = TokenTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 100
)

doc = data.load()

chunk = splitter.split_documents(doc)

print(len(chunk))

for i in chunk:
    print(i.page_content)
    print()
    print()