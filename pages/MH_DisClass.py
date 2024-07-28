import streamlit as st
from st_pages import add_page_title, get_nav_from_toml, hide_pages

st.set_page_config(
    page_title="Mental Health Discourse Classifier",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

sections = st.sidebar.toggle("Sections", value=True, key="use_sections")

nav = get_nav_from_toml(".streamlit/pages.toml")

pg = st.navigation(nav)

add_page_title(pg)

pg.run()

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