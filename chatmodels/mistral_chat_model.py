from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

model = ChatMistralAI(
    model = "mistral-small",
    temperature=0.1
)

result = model.invoke("What is langchain?")
print(result.content)