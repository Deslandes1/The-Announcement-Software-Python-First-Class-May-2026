import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="TikTok Live – Build Software Easily",
    page_icon="🎈",
    layout="centered"
)

# ---------- Animated CSS: stars, balloons, gradients ----------
st.markdown(
    """
    <style>
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        100% { transform: translateY(-20px) rotate(5deg); }
    }
    @keyframes starGlow {
        0% { text-shadow: 0 0 2px gold; }
        100% { text-shadow: 0 0 20px orange; }
    }
    .balloon {
        animation: float 3s ease-in-out infinite;
        display: inline-block;
        font-size: 2.5rem;
        margin: 0 0.2rem;
    }
    .star {
        animation: starGlow 1s alternate infinite;
        display: inline-block;
        font-size: 2rem;
    }
    .main-title {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(135deg, #ffd89b, #c7e9fb);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0;
    }
    .subtitle {
        text-align: center;
        font-size: 1.5rem;
        color: #ffecb3;
    }
    .highlight {
        background: rgba(255,215,0,0.2);
        padding: 0.8rem;
        border-radius: 30px;
        text-align: center;
        margin: 1rem 0;
    }
    .engineer {
        text-align: center;
        font-size: 1.3rem;
        font-family: monospace;
        margin-top: 2rem;
        border-top: 2px dashed gold;
        padding-top: 1rem;
        color: #ffd966;
    }
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    }
    h1, h2, h3, p, div {
        color: white;
    }
    .stButton button {
        background-color: #ff6f61 !important;
        color: white !important;
        border-radius: 50px !important;
        font-weight: bold;
        font-size: 1.2rem;
        padding: 0.5rem 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- Header with floating balloons & stars ----------
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown(
        '<div style="text-align:center;">'
        '<span class="balloon">🎈</span> <span class="star">✨</span> '
        '<span class="balloon">🎈</span> <span class="star">⭐</span> '
        '<span class="balloon">🎈</span> <span class="star">🌟</span> '
        '<span class="balloon">🎈</span>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown('<h1 class="main-title">🔥 𝐋𝐈𝐕𝐄 𝐓𝐎𝐃𝐀𝐘 🔥</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">🧬 𝘽𝙪𝙞𝙡𝙙 𝙔𝙤𝙪𝙧 𝙊𝙬𝙣 𝙎𝙤𝙛𝙩𝙬𝙖𝙧𝙚 – 𝙀𝙖𝙨𝙮 & 𝙁𝙧𝙚𝙚 🧬</p>', unsafe_allow_html=True)

st.markdown("---")

# ---------- Course details ----------
st.markdown(
    """
    <div class="highlight">
    ✨ <strong>1‑hour simple course</strong> – no coding experience needed ✨
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("### 📌 What you will learn to sign up for:")
cols = st.columns(2)
with cols[0]:
    st.markdown("✅ **GitHub** – store your code")
    st.markdown("✅ **Streamlit** – deploy web apps for free")
with cols[1]:
    st.markdown("✅ **Deepseek** – AI code assistant")
    st.markdown("✅ **Gemini (Google)** – ask technical questions")

st.markdown("✅ **Grok (xAI)** – another powerful AI helper")

st.markdown(
    """
    <div class="highlight">
    🎈 <strong>Everyone is welcome – absolute beginners too!</strong> 🎈
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- Live info ----------
today_date = datetime.now().strftime("%A, %B %d, %Y")
st.info(f"📅 **Live today:** {today_date} – 🔗 Link in my TikTok bio")

# ---------- Call to action button (just for fun) ----------
if st.button("🎉 I'm coming! 🎉"):
    st.balloons()
    st.success("See you there! Bring your excitement 🧬✨")

# ---------- Signature ----------
st.markdown(
    f"""
    <div class="engineer">
    🧑‍💻 <strong>Gesner Deslandes</strong><br>
    Python Software Engineer
    </div>
    """,
    unsafe_allow_html=True
)

# Footer with floating stars
st.markdown(
    '<div style="text-align:center; margin-top:2rem;">'
    '<span class="star">✨</span> <span class="balloon">🎈</span> '
    '<span class="star">⭐</span> <span class="balloon">🎈</span> '
    '<span class="star">🌟</span> <span class="balloon">🎈</span> '
    '<span class="star">✨</span>'
    '</div>',
    unsafe_allow_html=True
)
