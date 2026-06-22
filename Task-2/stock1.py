import streamlit as st

st.set_page_config(
    page_title="Stock Portfolio Tracker",
    page_icon="💹",
    layout="wide"
)

# Background
st.markdown("""
<style>

/* Full Page Background */
.stApp {
    background: linear-gradient(
        135deg,
        #e0f7fa 0%,
        #d6eaff 25%,
        #e3f2fd 50%,
        #e8eaf6 75%,
        #f3e5f5 100%
    );
}

/* Main Title */
.title {
    text-align: center;
    font-size: 68px;
    font-weight: 900;
    color: #0d47a1;
    letter-spacing: 2px;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 22px;
    color: #37474f;
    font-weight: 500;
    margin-bottom: 30px;
}

/* Glass Card */
.glass {
    background: rgba(255,255,255,0.65);
    backdrop-filter: blur(12px);
    padding: 25px;
    border-radius: 25px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.1);
}

/* Result Card */
.result-card {
    background: linear-gradient(
        135deg,
        #90caf9,
        #64b5f6,
        #4fc3f7
    );
    color: #0d47a1;
    text-align: center;
    padding: 25px;
    border-radius: 20px;
    font-size: 32px;
    font-weight: bold;
    margin-top: 20px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
}

/* Button */
.stButton > button {
    width: 100%;
    border-radius: 15px;
    height: 55px;
    font-size: 18px;
    font-weight: bold;
    background: linear-gradient(
        135deg,
        #64b5f6,
        #42a5f5
    );
    color: white;
    border: none;
}

/* Hide Streamlit Elements */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

</style>
""", unsafe_allow_html=True)

#Title
st.markdown(
'<div class="title">💹 Stock Portfolio Tracker </div>',
unsafe_allow_html=True
)

stocks = {
    "AAPL":180,
    "TSLA":250,
    "GOOG":140,
}

st.markdown('<div class="card">', unsafe_allow_html=True)

stock = st.selectbox(
    "Choose a Stock",
    list(stocks.keys())
)

quantity = st.slider(
    "Select Quantity",
    1,100,1
)

if st.button("Analyze Investment 🚀"):

    investment = stocks[stock] * quantity

    st.metric(
        "Portfolio Value",
        f"${investment}"
    )

    if investment < 1000:
        level = "🟢 Small Investor"
    elif investment < 5000:
        level = "🟡 Medium Investor"
    else:
        level = "🔴 Large Investor"

    st.success(level)

    st.progress(
        min(investment/10000,1.0)
    )

    st.write("### Investment Summary")
    st.write(f"Stock : {stock}")
    st.write(f"Quantity : {quantity}")
    st.write(f"Current Price : ${stocks[stock]}")
    st.write(f"Total Value : ${investment}")

    with open("investment.txt","w") as file:
        file.write(f"Stock : {stock}\n")
        file.write(f"Quantity : {quantity}\n")
        file.write(f"Total Value : ${investment}")

st.markdown('</div>', unsafe_allow_html=True)