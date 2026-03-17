from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model='llama-3.1-8b-instant',
    temperature=0.7
)

result = llm.invoke("What is langchain?")
print(result.content)