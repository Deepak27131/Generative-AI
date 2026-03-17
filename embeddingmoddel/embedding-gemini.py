from dotenv import load_dotenv
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    # google_api_key=os.getenv("GOOGLE_API_KEY")
)

text = [
    'Hello this is deepak here',
    "hello my name is hero",
    "Hello how are you"
]

vector = embeddings.embed_query(text)
print(vector)