import streamlit as st
from st_pages import add_page_title, get_nav_from_toml, hide_pages

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

primaryColor = "#575fe8"
backgroundColor = "#f5f7f3"
secondaryBackgroundColor = "#c9eab8"
textColor = "#262730"
font = "sans-serif"
title_size = 40
heading_size = 28
caption_size = 12
content_size = 16

# Set background color and font family for body and sidebar
st.markdown(
    """
"""
)

# Colors
color_ds = '#3ead20'
color_sc = '#1d67c2'
color_gd = '#f73e77'

hide_pages(["Banking Dynamics", "Mental Health Discourse Classifier"])

def my_widget(key):
    return st.button(key)

st.image("images/Portfolio.png")
st.title("""⛅ About Me""")
textcol, imagecol = st.columns([0.5, 0.5], gap = "medium")
with textcol:
    st.write(""":violet[I'm a **data scientist** and **researcher** from Metro Manila. I like to learn, solve problems, and tinker.]""")
    st.subheader("""I'm interested in the intersection of **data** with **mobility** 🚅 and **(sustainable!) development** 🌱""")
    st.write("""I want to use data science to :violet[unravel patterns that derive actional insights].""") 
    st.write("""In my spare time, I watch films, play video games, and try my hand at mathematical and programming mini-projects.""")
    st.write("""Thank you for taking the time to check out my portfolio! If you have any questions or comments, feel free to shoot me an email at diannecyumol@gmail.com.""")
    container = st.container(border=True)
    container.page_link("https://drive.google.com/file/d/1mzKGFkiQDqgd0JY-7a6e7dQv8PhMZlW5/view?usp=sharing", label="Looking for my resume? Check it out here!", icon="📃")

with imagecol:
    st.image("images/Portfolio_1.png")

expand = False

#st.subheader("🚀 Let's Explore!")
#col1, col2, col3 = st.columns(3)

#with col1:
    #st.page_link("pages/Data_Science_Projects.py", label = "Data Science Projects", icon="📊")

#with col2:
    #st.page_link("pages/Work_Experience.py", label = "Work Experience", icon="💼")

#with col3:
    #st.page_link("pages/Other_Projects.py", label = "Other Projects", icon="📦")

#st.caption("This website is an open notebook for a fictional depiction of Earth in the 21st Century. It includes a a wiki called 📓Factbook, hundreds of illustrated 📗Stories, and a collection of essays, notes and journals under the 📓MillMint category. To get started, visit the 📕Intro, FAQ, or just have a look around.")
