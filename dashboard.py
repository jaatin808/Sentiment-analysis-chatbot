import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os

# Set page configuration
st.set_page_config(page_title="📊 Chatbot Analysis Dashboard", layout="wide")

# Custom CSS for better visuals
st.markdown(
    """
    <style>
    body { background-color: #121212; color: #e0e0e0; }
    .main-title { text-align: center; color: #1f7a8c; }
    .sentiment-box { padding: 10px; border-radius: 8px; color: white; text-align: center; font-size: 18px; }
    .positive { background-color: #2ECC71; }
    .negative { background-color: #E74C3C; }
    .neutral { background-color: #F1C40F; color: black; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='main-title'>📊 Chatbot Conversation Analysis</h1>", unsafe_allow_html=True)

# Load chat history CSV
file_path = "chat_history.csv"

if not os.path.exists(file_path):
    st.warning("⚠ No chat data found. Start chatting to see analysis!")
else:
    df = pd.read_csv(file_path, usecols=["message", "sentiment"], on_bad_lines="skip")  # Only load required columns

    # Display Chat History Table
    st.subheader("🗂 Chat History")
    st.dataframe(df.style.set_properties(**{'background-color': '#333', 'color': 'white'}))

    # Sentiment Distribution (Pie Chart)
    st.subheader("📊 Sentiment Distribution")
    sentiment_counts = df["sentiment"].value_counts()
    
    fig, ax = plt.subplots(figsize=(6, 4))
    colors = ["#2ECC71", "#E74C3C", "#F1C40F"]  # Green (Positive), Red (Negative), Yellow (Neutral)
    ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%", colors=colors, startangle=140)
    ax.set_title("Sentiment Analysis")
    st.pyplot(fig)

    # Word Cloud for Most Used Words
    st.subheader("☁️ Most Used Words in Conversations")
    all_text = " ".join(df["message"].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color="black", colormap="coolwarm").generate(all_text)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
