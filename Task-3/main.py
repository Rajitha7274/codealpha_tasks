import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Smart Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ------------------ CSS Styling ------------------ #
st.markdown("""
<style>

/* Beautiful Yellow Multi-Color Background */
.stApp {
    background: linear-gradient(
        135deg,
        #fff9c4 0%,
        #ffe082 20%,
        #ffecb3 40%,
        #ffd54f 60%,
        #fff3e0 80%,
        #f8bbd0 100%
    );
}

/* Hide Streamlit Branding */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Title */
.title {
    text-align: center;
    font-size: 70px;
    font-weight: 900;
    color: #5d4037;
    letter-spacing: 2px;
    text-shadow: 2px 2px 8px rgba(255,255,255,0.7);
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #6d4c41;
    margin-bottom: 30px;
}

/* User Bubble */
.user-msg {
    background: linear-gradient(
        135deg,
        #ffca28,
        #ffb300
    );
    color: #3e2723;
    padding: 12px;
    border-radius: 20px;
    margin: 10px 0;
    text-align: right;
    font-weight: bold;
}

/* Bot Bubble */
.bot-msg {
    background: white;
    color: #4e342e;
    padding: 12px;
    border-radius: 20px;
    margin: 10px 0;
    border-left: 5px solid #ffca28;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
}

/* Input Box */
.stTextInput > div > div > input {
    border-radius: 15px;
    border: 2px solid #ffd54f;
}

/* Buttons */
div.stButton > button {
    background: linear-gradient(
        135deg,
        #ffca28,
        #ff8f00
    );
    color: #3e2723;
    font-weight: bold;
    border-radius: 25px;
    height: 55px;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# ------------------ Title ------------------ #

st.markdown("""
<div class="title">
🤖 Smart Chatbot
</div>

<div class="subtitle">
Ask me anything about technology and programming 💡
</div>
""", unsafe_allow_html=True)

# ------------------ Responses Dictionary ------------------ #

responses = {
    "hello": "👋 Hello! Nice to meet you.",
    "hi": "😊 Hi! How can I help you today?",
    "how are you": "😄 I'm doing great! Thanks for asking.",
    "what is your name": "🤖 My name is Smart Chatbot.",
    "who are you": "🤖 I am Smart Chatbot, your virtual assistant.",
    "who made you": "💻 I was created using Python and Streamlit.",
    "what is python": "🐍 Python is a popular programming language.",
    "what is ai": "🤖 Artificial Intelligence enables machines to learn and make decisions.",
    "what is ml": "📈 Machine Learning is a branch of AI that learns from data.",
    "what is data science": "📊 Data Science is the process of analyzing data to gain insights.",
    "what is html": "🌐 HTML is used to structure web pages.",
    "what is css": "🎨 CSS is used to style web pages.",
    "what is javascript": "⚡ JavaScript adds interactivity to websites.",
    "what is java": "☕ Java is an object-oriented programming language.",
    "what is c++": "💻 C++ is widely used in software and game development.",
    "what is github": "🔗 GitHub is a platform used to store and manage code repositories.",
    "what is sql": "🗄️ SQL is used to manage databases.",
    "what is cloud computing": "☁️ Cloud Computing provides computing services over the internet.",
    "what is cyber security": "🔒 Cyber Security protects systems and data from online threats.",
    "what is internship": "🎓 An internship helps students gain practical work experience.",
    "thank you": "😊 You're welcome!",
    "help": "🤝 I can answer questions about programming and technology.",
    "good morning": "🌞 Good Morning! Have a wonderful day.",
    "good afternoon": "☀️ Good Afternoon!",
    "good evening": "🌆 Good Evening!",
    "bye": "👋 Goodbye! Have a great day."
}

# ------------------ Chat Function ------------------ #

def chatbot_response(user_input):

    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "👋 Hello! Nice to meet you."

    elif "python" in user_input:
        return "🐍 Python is a beginner-friendly programming language."

    elif "ai" in user_input:
        return "🤖 AI enables machines to learn and make decisions."

    elif "name" in user_input:
        return "🤖 My name is Smart Chatbot."

    elif "streamlit" in user_input:
        return "🚀 Streamlit helps create web apps using Python."

    elif "how are you" in user_input:
        return "😊 I'm doing great! Thanks for asking."

    elif "your name" in user_input or "what is your name" in user_input:
        return "🤖 My name is Smart Chatbot."

    elif "who made you" in user_input:
        return "💻 I was created using Python and Streamlit."

    elif "python" in user_input:
        return "🐍 Python is a powerful and beginner-friendly programming language."

    elif "streamlit" in user_input:
        return "🚀 Streamlit helps create beautiful web apps using Python."

    elif "college" in user_input:
        return "🎓 College life is a great opportunity to learn and grow."

    elif "course" in user_input:
        return "📚 There are many courses available for programming and technology."

    elif "project" in user_input:
        return "💡 Projects help improve your practical coding skills."

    elif "html" in user_input:
        return "🌐 HTML is used to create web page structures."

    elif "css" in user_input:
        return "🎨 CSS is used to style web pages."

    elif "javascript" in user_input:
        return "⚡ JavaScript makes web pages interactive."

    elif "java" in user_input:
        return "☕ Java is a popular object-oriented programming language."

    elif "c++" in user_input:
        return "💻 C++ is widely used for system and application development."

    elif "ai" in user_input or "artificial intelligence" in user_input:
        return "🤖 AI enables machines to learn and make decisions."

    elif "machine learning" in user_input:
        return "📈 Machine Learning is a branch of AI that learns from data."

    elif "data science" in user_input:
        return "📊 Data Science involves analyzing and interpreting data."

    elif "thank you" in user_input:
        return "😊 You're welcome!"

    elif "help" in user_input:
        return "🤝 I can answer questions about programming, technology, and myself."

    elif "good morning" in user_input:
        return "🌞 Good Morning! Have a wonderful day."

    elif "good afternoon" in user_input:
        return "☀️ Good Afternoon!"

    elif "good evening" in user_input:
        return "🌆 Good Evening!"

    elif "bye" in user_input:
        return "👋 Goodbye! Have a great day."

    else:
        return "❓ Sorry, I don't understand that."

# ------------------ Session State ------------------ #

if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------ User Input ------------------ #

user_input = st.text_input(
    "Type your message here..."
)

# ------------------ Buttons ------------------ #

col1, col2 = st.columns(2)

with col1:
    send = st.button("🚀 Send")

with col2:
    clear = st.button("🗑️ Clear")

# Send Button Action
if send and user_input:

    bot_reply = chatbot_response(user_input)

    st.session_state.messages.append(
        ("user", user_input)
    )

    st.session_state.messages.append(
        ("bot", bot_reply)
    )

# Clear Button Action
if clear:
    st.session_state.messages = []
    st.rerun()

# ------------------ Display Chat ------------------ #

for sender, msg in st.session_state.messages:

    if sender == "user":
        st.markdown(
            f'<div class="user-msg">👤 {msg}</div>',
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            f'<div class="bot-msg">🤖 {msg}</div>',
            unsafe_allow_html=True
        )