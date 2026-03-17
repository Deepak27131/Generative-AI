from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatMistralAI(
    model = "mistral-small",
    temperature=0.8
)


print("Choose your AI Mode")
print('Press 1 for funny mode ')
print('Press 2 for angry mode ')
print('Press 3 for sad mode ')

choice = int(input("Tell  your response mode :--> "))

if choice == 1:
    mode = "You are an angry Ai agent .You respond agressively and impatiently"
elif choice == 2:
    mode = "You are an funny Ai agent .You respond with humor and joke"
elif choice == 3:
    mode = "You are a very sad AI agent .You responed like very sad like that"

messages = [
    SystemMessage(content=mode)
]

print("--------------Welcome Type 0 zero to exit the application ----------")

while True:
   
    prompt = input("You : ")
    
    messages.append(HumanMessage(content=prompt))
    
    if prompt == "0":
        break
    response =model.invoke(messages)
    messages.append(AIMessage(content= response.content))
    
    print("Bots : ",response.content)

print(messages)