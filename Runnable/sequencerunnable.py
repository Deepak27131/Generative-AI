from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# prompt TempaLTE
prompt = ChatPromptTemplate.from_template(
    'Explain {topic} in simple words'
)

#  model
model = ChatMistralAI(model='mistral-small-2506')

# output parser
parser = StrOutputParser()

# #formate the prompt 
# formatted_prompt = prompt.format_messages(topic='Mchine learning')

# # call the model manually
# response = model.invoke(formatted_prompt)

# # praser 
# final_output = parser.parse(response.content)

# print(final_output)

# using chain to easy way to handle mutiple method to single line

chain = prompt | model | parser
result = chain.invoke({'topic':'deep learning'})
print(result)