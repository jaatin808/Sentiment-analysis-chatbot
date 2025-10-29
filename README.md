# 🤖 Streamlit Sentiment Chatbot

An AI-powered chatbot built using **Streamlit**, **LangChain**, and **VADER Sentiment Analysis**.  
This chatbot analyzes the emotional tone of user messages and responds empathetically with context-aware replies.

---

## 🚀 Features

- 💬 Real-time conversational chatbot
- 🧠 Sentiment detection using **VADER**
- 🤖 Llama3 model integration via **LangChain**
- 🎨 Modern dark-themed Streamlit UI
- 💾 Saves chat history to CSV
- ⚡ Contextual and empathetic responses

---

## 🏗️ Project Structure

📦 sentiment-chatbot/
├── chatbot_ui.py # Streamlit user interface
├── chatbot.py # Chat logic, sentiment analysis, and response generation
├── dashboard.py # Optional dashboard (if applicable)
├── requirements.txt # List of dependencies
├── chat_history.csv # Auto-generated chat logs
└── .gitignore # Ignored files/folders (like venv)


---

## 🧩 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

2️⃣ Create a virtual environment
    
    python -m venv chatbot

3️⃣ Activate the virtual environment

    chatbot\Scripts\activate

4️⃣ Install dependencies

    pip install -r requirements.txt

▶️ Run the App

    streamlit run chatbot_ui.py




🧠 Sentiment Categories

| Sentiment Type            | Emoji | Description                |
| ------------------------- | ----- | -------------------------- |
| Strongly Positive         | 😀    | Very happy or excited tone |
| Positive / Optimistic     | 😊    | Happy or hopeful mood      |
| Neutral                   | 😐    | Balanced or calm           |
| Negative / Disappointment | 😔    | Mildly sad or dissatisfied |
| Anger                     | 😡    | Frustrated or angry tone   |


🧰 Tech Stack

Python
Streamlit
LangChain
Ollama Llama3
VADER Sentiment Analyzer
Pandas

💡 Future Enhancements

Add multi-user conversation history
Integrate Hugging Face models for deeper emotion detection
Add authentication and dashboard analytics
Deploy using Render, Streamlit Cloud, or Docker



🧑‍💻 Author

Jatin Balodi
📍 Built with ❤️ using Python, Streamlit, and LangChain



    
