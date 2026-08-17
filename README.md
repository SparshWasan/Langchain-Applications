# 🦜🔗 LangChain Applications Practice

A repository containing hands-on practice projects, implementations, and experiments built with **LangChain**, exploring multi-provider LLM integrations, prompt structuring, document processing, text splitters, and generative AI application workflows.

---

## 📁 Repository Structure

```text
Langchain Applications/
│
├── Travel Guide Assistant/
│   └── app.py                         # Multi-LLM Travel recommendation assistant (Gemini, Groq, OpenAI)
├── Python Tutor Assistant/
│   └── app.py                         # Python concept tutor assistant (Groq LLaMA-3.3)
├── PDF Content Previewer/
│   └── app.py                         # PDF content previewer using PyPDFLoader
├── PDF Document Splitter/
│   └── app.py                         # PDF document chunking with RecursiveCharacterTextSplitter
├── Python Code Splitter/
│   ├── app.py                         # Language-aware Python code splitter using RecursiveCharacterTextSplitter
│   └── tool_calling.py                # Sample Code for Code splitting
├── attention_is_all_you_need.pdf      # Sample research paper document for PDF loaders & splitters
├── .env.example                       # Example environment variables template
├── .gitignore                         # Ignored files (virtual environments, keys, .env)
└── README.md                          # Project documentation
```

---

## 🚀 Projects Overview

### 1. 🧳 Travel Guide Assistant

An AI-powered travel recommendation assistant demonstrating model comparison and multi-provider abstraction using LangChain's unified `init_chat_model` API.

- **Features**:
  - Leverages `SystemMessage` for persona roleplay and `HumanMessage` for prompt formulation.
  - Multi-provider LLM inference across top frontier and open-weight models:
    - **Google GenAI**: `gemini-2.5-flash`
    - **Groq**: `llama-3.3-70b-versatile`
    - **OpenAI**: `gpt-5.4-mini`
  - Demonstrates response variation, formatting differences, and output generation across providers.

---

### 2. 🐍 Python Tutor Assistant

An interactive AI programming tutor designed to explain Python programming concepts with clear, concise code examples.

- **Features**:
  - Role-based system prompting configured for educational code explanations.
  - Fast inference powered by **Groq** (`llama-3.3-70b-versatile`).

---

### 3. 📄 PDF Content Previewer

A PDF content previewer that extracts and displays the raw text content and metadata of a PDF document.

- **Features**:
  - Extracts content from local PDF files using `PyPDFLoader`.
  - Displays document metadata and page content.
  - No external LLM API keys required for document extraction.

---

### 4. 📑 PDF Document Splitter

A document chunking pipeline for PDF documents using LangChain's text splitting utilities.

- **Features**:
  - Loads PDF documents with `PyPDFLoader`.
  - Splits documents into manageable chunks using `RecursiveCharacterTextSplitter` (chunk size: 1000, overlap: 200).
  - Preserves document metadata across chunk splits.

---

### 5. 💻 Python Code Splitter & Tool Calling

Language-aware code parsing and function-calling implementations.

- **Features**:
  - **Python Code Splitting (`app.py`)**:
    - Loads Python source files using `TextLoader`.
    - Employs `RecursiveCharacterTextSplitter.from_language(Language.PYTHON)` for syntax-aware code chunking (chunk size: 500, overlap: 50).

---

## 🛠️ Prerequisites & Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd "Langchain Applications"
```

### 2. Set Up Virtual Environment (Recommended)

```bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the core LangChain library, provider integrations, and document loader dependencies:

```bash
pip install langchain langchain-[llm_provider_name] python-dotenv langchain-community pypdf
```

### 4. Configure API Keys

Create a `.env` file in the root directory (refer to `.env.example`):

```env
GEMINI_API_KEY=your_gemini_api_key_here
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

> [!TIP]
> - Get a Google Gemini API Key from [Google AI Studio](https://aistudio.google.com/).
> - Get a Groq API Key from the [Groq Console](https://console.groq.com/).
> - Get an OpenAI API Key from the [OpenAI Platform](https://platform.openai.com/api-keys).

---

## 🏃 Running Applications

Make sure to run the scripts from the repository root directory:

```bash
# 1. Travel Guide Assistant
python "Travel Guide Assistant/app.py"

# 2. Python Tutor Assistant
python "Python Tutor Assistant/app.py"

# 3. PDF Content Previewer
python "PDF Content Previewer/app.py"

# 4. PDF Document Splitter
python "PDF Document Splitter/app.py"

# 5. Python Code Splitter
python "Python Code Splitter/app.py"
```

---

## 🧰 Tech Stack

- **Frameworks & Libraries**: [LangChain](https://www.langchain.com/) (`langchain`, `langchain-community`, `langchain-text-splitters`)
- **Document & Code Loaders**: `PyPDFLoader`, `TextLoader`
- **Text Splitters**: `RecursiveCharacterTextSplitter` (with Python language syntax awareness)
- **LLM Providers & SDKs**:
  - [Google Gemini API](https://ai.google.dev/) (`langchain-google-genai`)
  - [Groq Cloud](https://groq.com/) (`langchain-groq`)
  - [OpenAI](https://openai.com/) (`langchain-openai`)
- **Environment Management**: `python-dotenv`
- **Language**: Python 3.10+

---

## 📜 License

This project is for educational and practice purposes.