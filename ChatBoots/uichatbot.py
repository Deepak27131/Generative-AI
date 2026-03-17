import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="AI Personality Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Personality Chatbot")

# Sidebar for mode selection
st.sidebar.title("Choose AI Mode")

mode_choice = st.sidebar.selectbox(
    "Select Personality",
    ["Funny 😄", "Angry 😡", "Sad 😢"]
)

if mode_choice == "Angry 😡":
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif mode_choice == "Funny 😄":
    mode = "You are a funny AI agent. You respond with humor and jokes."
else:
    mode = "You are a very sad AI agent. You respond emotionally and sadly."

model = ChatMistralAI(
    model="mistral-small",
    temperature=0.8
)

# Session memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

# Show previous messages
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# Chat input
prompt = st.chat_input("Type your message...")

if prompt:

    st.session_state.messages.append(HumanMessage(content=prompt))

    with st.chat_message("user"):
        st.write(prompt)

    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(AIMessage(content=response.content))

    with st.chat_message("assistant"):
        st.write(response.content)

# Clear chat button
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = [SystemMessage(content=mode)]