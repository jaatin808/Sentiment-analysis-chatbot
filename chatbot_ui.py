import streamlit as st
from datetime import datetime
from chatbot import get_response

# -------------------------------
# 🎨 Custom CSS for styling
# -------------------------------
def add_custom_css():
    st.markdown("""
        <style>
        body {
            background-color: #0e1117;
            color: #e0e0e0;
            font-family: 'Segoe UI', sans-serif;
        }
        .chat-container {
            padding: 1rem;
            max-width: 900px;
            margin: auto;
        }
        .chat-bubble {
            border-radius: 16px;
            padding: 10px 15px;
            margin: 6px 0;
            display: inline-block;
            max-width: 75%;
            word-wrap: break-word;
            font-size: 15px;
        }
        .user-msg {
            background-color: #1f7a8c;
            color: white;
            text-align: right;
            align-self: flex-end;
        }
        .ai-msg {
            background-color: #333333;
            color: white;
            text-align: left;
            align-self: flex-start;
        }
        .sentiment-box {
            background-color: #444;
            color: #fff;
            border-radius: 8px;
            padding: 6px 10px;
            font-weight: 600;
            font-size: 14px;
            margin: 4px 0;
            display: inline-block;
        }
        .timestamp {
            font-size: 12px;
            color: #999;
            margin-top: 2px;
        }
        .stTextInput > div > div > input {
            background-color: #2c2c2c;
            color: white;
            border: 1px solid #555;
            border-radius: 6px;
        }
        .stButton > button {
            background-color: #1f7a8c;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 6px;
            font-size: 16px;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #145864;
            transform: scale(1.03);
        }
        </style>
    """, unsafe_allow_html=True)

# -------------------------------
# 🚀 Streamlit App
# -------------------------------
def main():
    st.set_page_config(page_title="🤖 Chatbot with Sentiment Analysis", layout="wide")
    add_custom_css()

    # Sidebar
    with st.sidebar:
        st.header("💬 Chat Settings")
        st.write("This chatbot analyzes the sentiment of your messages.")
        if st.button("🗑️ Clear Chat"):
            st.session_state.clear()
            st.rerun()

    st.title("🤖 Chatbot with Sentiment Analysis")
    st.markdown("Type your message below — the bot will analyze its sentiment and reply intelligently.")

    # Initialize session state
    if "context" not in st.session_state:
        st.session_state.context = ""
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    for msg in st.session_state.messages:
        role = msg["role"]
        text = msg["text"]
        time = msg.get("time", "")
        if role == "user":
            st.markdown(f"<div class='chat-bubble user-msg'>{text}</div><div class='timestamp'>{time}</div>", unsafe_allow_html=True)
        elif role == "sentiment":
            st.markdown(f"<div class='sentiment-box'>Sentiment: {text}</div>", unsafe_allow_html=True)
        elif role == "ai":
            st.markdown(f"<div class='chat-bubble ai-msg'>{text}</div><div class='timestamp'>{time}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Input area
    with st.form("user_input_form", clear_on_submit=True):
        user_input = st.text_input("💭 Your message:", key="user_input", placeholder="Type something and press Enter...")
        submitted = st.form_submit_button("Send")

    # Handle user input
    if submitted and user_input.strip():
        now = datetime.now().strftime("%H:%M")
        response, sentiment, updated_context = get_response(st.session_state.context, user_input)

        st.session_state.context = updated_context
        st.session_state.messages.append({"role": "user", "text": user_input, "time": now})
        st.session_state.messages.append({"role": "sentiment", "text": sentiment})
        st.session_state.messages.append({"role": "ai", "text": response, "time": now})

        st.rerun()

if __name__ == "__main__":
    main()
