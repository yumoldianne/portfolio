import streamlit as st
from st_pages import Page, add_page_title, show_pages, hide_pages

st.set_page_config(
    page_title="Other Projects",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

show_pages(
    [
        Page("pages/Home.py", "Home", "🏠"),
        Page("pages/Data_Science_Projects.py", "Data Science Projects", "📊"),
        Page("pages/Work_Experience.py", "Work Experience", "💼"),
        Page("pages/Other_Projects.py", "Other Projects", "📦"),
        Page("pages/Banking_Dynamics.py", "Banking Dynamics", "🏦"),
        Page("pages/MH_DisClass.py", "Mental Health Discourse Classifier", "🧠")
    ]
)

hide_pages(["Banking Dynamics", "Mental Health Discourse Classifier"])

st.title("📦 Other Projects")
st.write("Here are some of my other projects that do not involve data science.")

st.subheader("🖊️ Narrative Design")
st.write("""One of the things I love the most is writing. Whether it be character narratives or personal essays, I love weaving words to create meaning.""")

st.subheader("🖌️ Graphic Design")
st.write("""Recently, I have gotten into graphic design using Figma. I wanted to utilize Figma to create illustrations and better data visualizations. This section is a work-in-progress since I just recently ventured into this foray.""")

with st.sidebar:
    st.subheader("Currently, I'm...")
    st.write("Working on a forecasting project 📈")
    st.write("Playing Hades ⚔️")

    st.subheader("""Let's connect!""")
    st.page_link("https://www.linkedin.com/in/yumoldianne/", label="LinkedIn", icon="🤝")
    st.page_link("https://github.com/yumoldianne", label="GitHub", icon="🤖")