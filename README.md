# 🦜🔗 LangChain Applications Practice

A repository containing hands-on practice projects, implementations, and experiments built with **LangChain**, exploring multi-provider LLM integrations, prompt structuring, and generative AI application workflows.

---

## 📁 Repository Structure

```text
Langchain Applications/
│
├── Travel Guide Assistant/
│   └── app.py               # Multi-LLM Travel recommendation assistant (Gemini, Groq, OpenAI)
├── Python Tutor Assistant/
│   └── app.py               # Python concept tutor assistant (Groq LLaMA-3.3)
│
├── .env.example             # Example environment variables template
├── .gitignore               # Ignored files (virtual environments, keys, .env)
└── README.md                # Project documentation
```

---

## 🚀 Projects Overview

### 1. 🧳 Travel Guide Assistant

An AI-powered travel recommendation assistant demonstrating model comparison and multi-provider abstraction using LangChain's unified `init_chat_model` API.

- **Features**:
  - Leverages `SystemMessage` for persona roleplay and `HumanMessage` for prompt formulation.
  - Multi-provider LLM inference in parallel workflows:
    - **Google GenAI**: `gemini-2.5-flash`
    - **Groq**: `llama-3.3-70b-versatile`
    - **OpenAI**: `gpt-5.4-mini`
  - Demonstrates response variation and speed across top frontier and open-weight models.

### 2. 🐍 Python Tutor Assistant

An interactive AI programming tutor designed to explain Python programming concepts with clear, concise code examples.

- **Features**:
  - Role-based system prompting configured for educational code explanations.
  - Fast inference powered by **Groq** (`llama-3.3-70b-versatile`).

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

Install the required packages using pip:

```bash
pip install langchain langchain-[llm_provider_name] python-dotenv
```

### 4. Configure API Keys

Create a `.env` file in the root directory (refer to `.env.example`):

```env
GEMINI_API_KEY=your_gemini_api_key_here
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

> [!TIP]
>
> - Get a Google Gemini API Key from [Google AI Studio](https://aistudio.google.com/).
> - Get a Groq API Key from the [Groq Console](https://console.groq.com/).
> - Get an OpenAI API Key from the [OpenAI Console](https://platform.openai.com/account/api-keys).

---

## 🏃 Running Applications

```bash
python "Travel Guide Assistant/app.py"
```

## 🧰 Tech Stack

- **Framework**: [LangChain](https://www.langchain.com/)
- **LLM Providers**:
  - [Google Gemini API](https://ai.google.dev/) (`google_genai`)
  - [Groq Cloud](https://groq.com/) (`groq`)
  - [OpenAI](https://openai.com/) (`openai`)
- **Environment Management**: `python-dotenv`
- **Language**: Python 3.10+

---

## 📜 License

This project is for educational and practice purposes.
