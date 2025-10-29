import os
import nltk
import pandas as pd
from datetime import datetime
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from nltk.sentiment import SentimentIntensityAnalyzer

# -------------------------------
# 🧠 Model & Prompt Setup
# -------------------------------
model = OllamaLLM(model="llama3")

prompt_template = """
You are a friendly and emotionally intelligent assistant.

Analyze the user's sentiment and respond appropriately with empathy and insight.

Here’s the previous conversation:
{context}

User: {question}

Assistant:
"""

prompt = ChatPromptTemplate.from_template(prompt_template)
chain = prompt | model

# -------------------------------
# 💬 Sentiment Analysis Setup
# -------------------------------
nltk.download("vader_lexicon", quiet=True)
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(message: str) -> str:
    """Analyze sentiment using VADER and classify into meaningful categories."""
    scores = sia.polarity_scores(message)
    compound = scores["compound"]
    pos, neg = scores["pos"], scores["neg"]

    if compound >= 0.7:
        return "Strongly Positive 😀"
    elif 0.3 <= compound < 0.7:
        return "Positive 😊"
    elif -0.3 < compound < 0.3:
        return "Neutral 😐"
    elif -0.7 < compound <= -0.3:
        return "Negative 😔"
    else:
        return "Strongly Negative 😡"

# -------------------------------
# 📁 Chat Logging Function
# -------------------------------
def save_chat_to_csv(user_input: str, sentiment: str, response: str):
    """Save chat message, sentiment, and response to CSV file with timestamps."""
    file_path = "chat_history.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {"timestamp": timestamp, "user_message": user_input,
            "sentiment": sentiment, "ai_response": response}
    df = pd.DataFrame([data])

    # Append or create file
    df.to_csv(file_path, mode="a", header=not os.path.exists(file_path), index=False)

# -------------------------------
# 🤖 Main Chatbot Logic
# -------------------------------
def get_response(context: str, user_input: str):
    """Generate chatbot response using LLaMA model and sentiment context."""
    sentiment = analyze_sentiment(user_input)
    emotion_prompt = f"The user seems to be feeling {sentiment}. Respond with empathy and understanding."

    try:
        response = chain.invoke({
            "context": f"{context}\n{emotion_prompt}",
            "question": user_input
        })
    except Exception as e:
        response = f"⚠️ Error generating response: {e}"

    # Update conversation context
    updated_context = f"{context}\nUser ({sentiment}): {user_input}\nAI: {response}"

    # Save chat to file
    save_chat_to_csv(user_input, sentiment, response)

    return response, sentiment, updated_context
