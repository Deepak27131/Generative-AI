from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    
)

template = ChatPromptTemplate([
    ('system',"""Answer the question based on the context below. If the 
        question cannot be answered using the information provided, answer with 
        "I don\'t know"."""),
    ('human','Context:{context}'),
    ('human', 'Question: {question}'),
])

result = template.invoke({
"context": """The most recent advancements in NLP are being driven by Large 
        Language Models (LLMs). These models outperform their smaller 
        counterparts and have become invaluable for developers who are creating 
        applications with NLP capabilities. Developers can tap into these 
        models through Hugging Face's `transformers` library, or by utilizing 
        OpenAI and Cohere's offerings through the `openai` and `cohere` 
        libraries, respectively.""",
"question": "Which model providers offer LLMs?"
})

print(result)