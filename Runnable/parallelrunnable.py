from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain_core.runnables import RunnableLambda

#  model
model = ChatMistralAI(model='mistral-small-2506')

# output parser
parser = StrOutputParser()

# two difference prompt
short_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in 1-2 lines"
)

detail_prompt = ChatPromptTemplate.from_template(
    'Explain {topic} in detail'
)



chain = RunnableParallel({
    'short':RunnableLambda(lambda x:x['short']) |short_prompt | model | parser,
    'detailed':RunnableLambda(lambda x:x['detailed']) | detail_prompt | model | parser
})

result = chain.invoke({
    'short': {'topic':'Machine learning'},
    'detailed': {'topic':'deep learning'}
})

print(result['short'])
print(result['detailed'])

# result = chain.invoke({'topic':'Deep learning'})
# print(result)