from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)

template = PromptTemplate.from_template(
    """
    Answer the question based on the context below.
    If the question cannot be answered using the information provied ,
    answer with "I don`t know"
    
    Context :{context}
    
    Question : {question}
    
    Answer:"""
)

prompt = template.invoke({
    "context": """The most recent advancements in NLP are being driven by Large 
        Language Models (LLMs). These models outperform their smaller 
        counterparts and have become invaluable for developers who are creating 
        applications with NLP capabilities. Developers can tap into these 
        models through Hugging Face's `transformers` library, or by utilizing 
        OpenAI and Cohere's offerings through the `openai` and `cohere` 
        libraries, respectively.""",
"question": "Which model providers offer LLMs?"
})

result = model.invoke(prompt)

print(result.content)