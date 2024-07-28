import streamlit as st
from st_pages import add_page_title, get_nav_from_toml, hide_pages

st.set_page_config(layout="wide")

nav = get_nav_from_toml(".streamlit/pages.toml")

pg = st.navigation(nav)

add_page_title(pg)

pg.run()

st.set_page_config(
    page_title="Other Projects",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

from st_pages import add_page_title, get_nav_from_toml, hide_pages

st.set_page_config(layout="wide")

nav = get_nav_from_toml(".streamlit/pages_sections.toml")

pg = st.navigation(nav)

add_page_title(pg)

pg.run()

hide_pages(["Banking Dynamics", "Mental Health Discourse Classifier"])

st.title("📦 Other Projects")
st.write("Here are some of my other projects that I've worked on!")

st.subheader("🖊️ Narrative Design")
st.write("""One of the things I love the most is writing. Whether it be character narratives or personal essays, I love weaving words to create meaning.""")
#expand = False
#with st.expander():
    #st.write 

st.subheader("🖌️ Graphic Design")
st.write("""Recently, I have gotten into graphic design using Figma. I wanted to utilize Figma to create illustrations and better data visualizations. This section is a work-in-progress since I just recently ventured into this foray.""")
#expand = False
#with st.expander():
    #st.write 

st.subheader("🌍 Web Applications")
st.write("""Streamlit allowed me to create web apps with ease. Here are some of those apps:""")
#expand = False
#with st.expander():
    #st.write 

with st.sidebar:
    st.subheader("Currently, I'm...")
    st.write("Working on a forecasting project 📈")
    st.write("Playing Hades ⚔️")

    st.subheader("""Let's connect!""")
    st.page_link("https://www.linkedin.com/in/yumoldianne/", label="LinkedIn", icon="🤝")
    st.page_link("https://github.com/yumoldianne", label="GitHub", icon="🤖")