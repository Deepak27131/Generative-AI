import streamlit as st
import json
import pandas as pd
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# same model and prompt (logic unchanged)
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

# UI
st.set_page_config(page_title="Movie Info Extractor", page_icon="🎬", layout="centered")

st.title("🎬 AI Movie Information Extractor")
st.write("Paste any movie description and the AI will extract useful information.")

paragraph = st.text_area("Enter Movie Description", height=200)

if st.button("🚀 Extract Information"):

    if paragraph.strip() == "":
        st.warning("Please enter a movie description.")

    else:

        with st.spinner("Analyzing description..."):

            final_prompt = prompt.invoke({"text": paragraph})
            response = model.invoke(final_prompt)

            output = response.content

            try:
                clean = output.replace("```json","").replace("```","")
                data = json.loads(clean)

                df = pd.DataFrame(list(data.items()), columns=["Field","Value"])

                st.success("Information Extracted Successfully ✅")
                st.table(df)

            except:
                st.subheader("Raw Model Output")
                st.write(output)