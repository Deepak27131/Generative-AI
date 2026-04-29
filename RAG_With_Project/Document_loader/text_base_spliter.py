from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter


data = TextLoader("notes.txt")

splitter = CharacterTextSplitter(
    separator="",
    chunk_size = 10,
    chunk_overlap = 1
)

doc = data.load()

chunks = splitter.split_documents(doc)

print(len(chunks))

for i in chunks:
    print(i.page_content)
    print()