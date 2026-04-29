from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from rich import print

# 1. Tool
@tool
def get_text_length(text: str) -> int:
    """Returns the number of characters in a given text"""
    return len(text)

tools = {
    "get_text_length": get_text_length
}

# 2. LLM
llm = ChatMistralAI(model="mistral-small-2506")

# 3. Bind tool
llm_with_tool = llm.bind_tools([get_text_length])

# 4. Chat loop
messages = []

prompt = input("You: ")

messages.append(HumanMessage(content=prompt))

# First LLM call
result = llm_with_tool.invoke(messages)
messages.append(result)

# 5. Tool execution
if result.tool_calls:
    tool_call = result.tool_calls[0]

    tool_name = tool_call["name"]
    tool_args = tool_call["args"]

    # Run tool
    tool_output = tools[tool_name].invoke(tool_args)

    # VERY IMPORTANT: ToolMessage
    messages.append(
        ToolMessage(
            content=str(tool_output),
            tool_call_id=tool_call["id"]
        )
    )

    # Second LLM call
    result = llm_with_tool.invoke(messages)

# Final output
print(result.content)