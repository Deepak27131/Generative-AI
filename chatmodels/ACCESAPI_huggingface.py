from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-R1'
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("what is data science ?")

print(result.content)