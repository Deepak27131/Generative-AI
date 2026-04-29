from langchain.tools import tool

@tool
def get_greating(name: str)-> str:
    """Generate a greating message for a users"""
    
    return f'Hello {name} ,Welcome to AI ara of words'

result = get_greating.invoke({'name':'Deepak'})

print(result)

print(get_greating.name)
print(get_greating.description)
print(get_greating.args)
