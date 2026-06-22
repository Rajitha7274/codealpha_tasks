import streamlit as st
import random

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Hangman MASTER",
    page_icon="🎮",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #e9d5ff,
        #ddd6fe,
        #dbeafe,
        #fbcfe8
    );
}

/* Title */
.title{
    text-align:center;
    font-size:55px;
    font-weight:800;
    color:#5b21b6;
}

/* Word Card */
.card{
    background:rgba(255,255,255,0.75);

    backdrop-filter: blur(12px);

    border-radius:25px;

    padding:30px;

    border:2px solid rgba(255,255,255,0.5);

    box-shadow:0 8px 25px rgba(124,58,237,0.15);

    text-align:center;
}

.word{
    font-size:48px;
    font-weight:bold;
    letter-spacing:12px;
    color:#16a34a;
}

/* Stats */
.stats{
    text-align:center;
    font-size:22px;
    font-weight:600;
    color:#374151;
}

/* Circular Alphabet Buttons */
.stButton > button{

    width:50px !important;
    height:50px !important;

    border-radius:50% !important;

    border:none !important;

    background:linear-gradient(
        135deg,
        #8b5cf6,
        #a78bfa
    ) !important;

    color:white !important;

    font-weight:bold !important;

    font-size:18px !important;

    transition:0.3s !important;
}

.stButton > button:hover{

    transform:scale(1.15);

    box-shadow:0 0 15px #8b5cf6;
}

/* Footer */
.footer{
    text-align:center;
    color:#6b7280;
    margin-top:20px;
}
            
        /* Big Play Again Button */

div.stButton:nth-last-child(1) button{

    width:100% !important;
    height:60px !important;

    border-radius:15px !important;

    background:linear-gradient(
        135deg,
        #ec4899,
        #8b5cf6
    ) !important;

    color:white !important;

    font-size:22px !important;

    font-weight:bold !important;

    box-shadow:0 8px 20px rgba(139,92,246,.3);
}    

</style>
""", unsafe_allow_html=True)

# ---------------- WORDS ----------------
WORDS = [
    "table",
    "chair",
    "mango",
    "water",
    "watch",
    "smile",
    "river",
    "plant",
    "tiger",
    "apple"
]

# ---------------- SESSION STATE ----------------
if "word" not in st.session_state:
    st.session_state.word = random.choice(WORDS)

if "guessed" not in st.session_state:
    st.session_state.guessed = []

if "wrong" not in st.session_state:
    st.session_state.wrong = 0

# ---------------- TITLE ----------------
st.markdown(
    "<div class='title'>🎮 HANGMAN MASTER</div>",
    unsafe_allow_html=True
)

st.success(
    "✨ Guess the hidden word before your 6 lives run out!"
)

# ---------------- WORD DISPLAY ----------------
display_word = ""

for letter in st.session_state.word:
    if letter in st.session_state.guessed:
        display_word += letter.upper() + " "
    else:
        display_word += "_ "

st.markdown(
    f"""
    <div class="card">
        <div class="word">{display_word}</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- STATS ----------------
lives = 6 - st.session_state.wrong

st.markdown(
    f"""
    <div class='stats'>
        ❤️ Lives Left: {lives}
        <br>
        🔤 Used Letters:
        {' '.join(st.session_state.guessed)}
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- CHECK WIN ----------------
won = all(
    letter in st.session_state.guessed
    for letter in st.session_state.word
)

lost = st.session_state.wrong >= 6

if won:
    st.success(
        "🏆🎉 AMAZING! YOU CRACKED THE WORD! 🎉🏆"
    )

    st.balloons()
    st.snow()

if lost:
    st.error(
        f"💀 GAME OVER! The word was: {st.session_state.word.upper()}"
    )

# ---------------- LETTER BUTTONS ----------------
if not won and not lost:

    st.write("### 🎯 Choose a Letter")

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    cols = st.columns(13)

    for i, letter in enumerate(letters):

        lower = letter.lower()

        disabled = lower in st.session_state.guessed

        if cols[i % 13].button(
            letter,
            key=letter,
            disabled=disabled,
            use_container_width=True
        ):

            st.session_state.guessed.append(lower)

            if lower not in st.session_state.word:
                st.session_state.wrong += 1

            st.rerun()

# ---------------- RESTART ----------------
st.markdown("---")


col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button(
        "🔄 PLAY AGAIN",
        use_container_width=True
    ):
        st.session_state.word = random.choice(WORDS)
        st.session_state.guessed = []
        st.session_state.wrong = 0
        st.rerun()


# ---------------- FOOTER ----------------
st.markdown(
    """
    <div class='footer'>
    ✨ CodeAlpha Python Internship Project ✨
    </div>
    """,
    unsafe_allow_html=True
)