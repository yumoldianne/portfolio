import streamlit as st
from st_pages import Page, add_page_title, show_pages, hide_pages

st.set_page_config(
    page_title="Mental Health Discourse Classifier",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

show_pages(
    [
        Page("Home.py", "Home", "🏠"),
        Page("pages/Data_Science_Projects.py", "Data Science Projects", "📊"),
        Page("pages/Work_Experience.py", "Work Experience", "💼"),
        Page("pages/Other_Projects.py", "Other Projects", "📦"),
        Page("pages/Banking_Dynamics.py", "Banking Dynamics", "🏦"),
        Page("pages/MH_DisClass.py", "Mental Health Discourse Classifier", "🧠")
    ]
)

hide_pages(["Banking Dynamics", "Mental Health Discourse Classifier"])

st.image("images/MindInsight Classifier.jpg")

st.header("🧠 Mental Health Discourse Classifier")
col1, col2, col3= st.columns([0.2, 0.2, 0.6], gap = "small")
with col1:
    st.page_link("https://github.com/yumoldianne/mh-discourse-classifier", label="View in Github", icon="🤖")
with col2:
    st.page_link("https://drive.google.com/file/d/1FbBBTKXseJayLFEY9hXMVm2f8Zx7qp3j/view?usp=sharing", label ="Read the report", icon="📄")

container = st.container(border=True)
container.write("✅ **Conclusion**")
container.write("From this project, I learned the fundamentals of deep learning. I still have a long way to go in understanding neural networks but I'm proud of this first project in predictive modeling.")

with st.sidebar:
    st.subheader("Currently, I'm...")
    st.write("Working on a forecasting project 📈")
    st.write("Playing Hades ⚔️")

    st.subheader("""Let's connect!""")
    st.page_link("https://www.linkedin.com/in/yumoldianne/", label="LinkedIn", icon="🤝")
    st.page_link("https://github.com/yumoldianne", label="GitHub", icon="🤖")