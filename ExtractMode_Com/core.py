from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatMistralAI(model="mistral-small-2506")

prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are an expert information extraction assistant.

Your task is to analyze movie descriptions and extract important details.

Extract the following information if available:
- Movie Name
- Genre
- Director
- Release Year
- Cast (list of actors)
- IMDb Rating
- Short Summary

Rules:
1. Only extract information that is explicitly mentioned.
2. Do not guess missing details.
3. If any information is missing, return "Not Available".
4. Return the result in structured JSON format.
"""),

    ("human", """
Extract useful movie information from the following description.

Description:
{text}
""")
])

paragraph = input("Give a paragraph : ")

final_prompt = prompt.invoke({"text": paragraph})

response = model.invoke(final_prompt)

print(response.content)