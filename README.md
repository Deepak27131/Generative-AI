# 🚀 Generative AI & LangChain Projects

This repository contains a collection of hands-on projects and experiments built using **LangChain**, **LLMs**, and modern **Generative AI tools**. The goal of this repo is to learn, implement, and demonstrate real-world AI applications such as tool calling, RAG systems, chat models, and runnable pipelines.

---

# 📂 Project Structure

```
.
├── ChatBoots/                # Chatbot implementations
├── ExtractMode_Com/          # Extraction mode experiments
├── Lagchain-Learning/        # Core LangChain learning modules
├── RAG_With_Project/         # Retrieval-Augmented Generation project
├── Runnable/                 # LangChain runnable pipelines
├── Tool_Calling/             # Tool binding with LLM examples
├── chatmodels/               # Different chat model integrations
├── chroma_db2/               # Vector database (ChromaDB) usage
├── embeddingmoddel/          # Embedding models experiments
├── main.py                   # Entry point script
├── test.py                   # Testing scripts
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation
```

---

# 🧠 Key Concepts Covered

### 1️⃣ LangChain Fundamentals

* Chains and Runnables
* Prompt Templates
* Message handling (Human, AI, Tool)

### 2️⃣ Tool Calling

* Creating custom tools using decorators
* Binding tools with LLMs
* Tool execution flow:

  ```
  User → LLM → Tool Call → Tool Execution → LLM Response
  ```

### 3️⃣ RAG (Retrieval-Augmented Generation)

* Document loading
* Text splitting
* Embeddings generation
* Vector database (ChromaDB)
* Context-aware answering

### 4️⃣ Chat Models

* Mistral AI integration
* Prompt engineering
* Multi-turn conversations

### 5️⃣ Runnable Pipelines

* LCEL (LangChain Expression Language)
* Pipeline chaining using `|` operator
* Modular AI workflows

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

## 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory:

```
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

# ▶️ How to Run

## Run main script

```bash
python main.py
```

## Run tool calling example

```bash
python Tool_Calling/tool_binding_with_llm.py
```

## Run RAG project

```bash
python RAG_With_Project/your_script.py
```

---

# 💡 Example: Tool Calling

```python
@tool
def get_text_length(text: str) -> int:
    return len(text)
```

This tool can be used by the LLM to dynamically compute text length during conversation.

---

# 🧪 Features

* ✅ Tool Binding with LLM
* ✅ Multi-step reasoning
* ✅ RAG pipeline implementation
* ✅ Vector database integration
* ✅ Modular runnable architecture

---

# 🚧 Future Improvements

* Add UI using Streamlit
* Deploy as API service
* Add memory to chatbot
* Improve multi-tool orchestration

---

# 🤝 Contribution

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Make changes
4. Submit a pull request

---

# 📜 License

This project is for learning and educational purposes.

---

# 🙌 Acknowledgment

* LangChain Documentation
* Mistral AI
* Open-source AI community

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
