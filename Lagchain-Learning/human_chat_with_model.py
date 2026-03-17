from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)

system_message = SystemMessage(
    """You are a helpful assistance that responed 
    to request to question with three exclamation mark"""
)

human_msg = HumanMessage("What is the capital of lucknow")

result = model.invoke([system_message,human_msg])
print(result.content)