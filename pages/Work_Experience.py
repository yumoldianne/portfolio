import streamlit as st
from st_pages import Page, add_page_title, show_pages, hide_pages

st.set_page_config(
    page_title="Work Experience",
    page_icon="💼",
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

def my_widget(key):
    return st.button(key)

st.title('💼 Work Experience')
st.write("""Take a look at the work I've been doing.""")
expand=False
with st.expander('💵 **Undisclosed Hedge Fund** - Data Operator Intern (March 2024 - Present)', expanded=expand):
     st.write('As a data operator intern, I utilized Selenium and BeautifulSoup to scrape economic calendar data from multiple websites and ensured data integrity and addressed potential issues for historical sentiment accuracy.')
     st.caption('Skills: Web Scraping, Data Processing, Data Cleaning')
with st.expander('⚡ **Energy Innovation Capital** - VC Industry Research and Data Analytics Extern (December 2023 - February 2024)', expanded=expand):
     st.write('As an extern, I conducted basic exploratory research on one of the emerging segments within the energy sector (geothermal energy) and identified interesting players, including public companies, private companies, and startups, in the industry that are developing innovations and dominating the market share. I also used data analytics tools to discover insights about the emerging markets in energy sector, learned to organize, analyze, and visualize data, and delivered a compelling presentation showcasing insights into the market landscape.')
     st.caption('Skills: Market Research, Data Analysis, Deal Sourcing, Project Management')
with st.expander('📰 **The Guidon** - Research and Development Analyst (June 2023 - Present)', expanded=expand):
     st.write('As an R&D analyst, I conducted in-depth research and analysis using Microsoft Excel, synthesizing data from diverse sources to generate quantitative reports for two groups, each with 15+ members. I also implemented data visualization techniques, resulting in an increase in the clarity and accessibility of information for staff teams, thereby enhancing the decision-making process.')
     st.caption('Skills: Data Analysis, Data Visualization, Data Collection')

st.title('🎒 Co-Curricular Activities & Competitions')
st.write("""Explore the projects I've been involved with at different organizations.""")
with st.expander('🧑‍🤝‍🧑 **Ateneo Mathematics Society** - Member Relations Department Head (June 2023 - Present)', expanded=expand):
     st.write('As a member relations department head, I oversee and lead the Member Relations Department, ensuring effective communication and collaboration between the organization and its members. I also selected and currently manage a team of heads to smoothly operate the department.')
     st.caption('Skills: Project Management')
with st.expander('📃 **Ateneo Mathematics Society** - Leadership Training Seminar Logistics-Platforms Committee (February 2024 - Present)', expanded=expand):
     st.write('As a logistics-platforms committee member, I am in charge of handling the onsite logistics of the event, which includes but not limited to contingencies and mobility plans.')
     st.caption('Skills: Project Management')
with st.expander('💻 **Philippines Junior Data Science Challenge** - Finalist (Top 10 out of 160 teams) (August 2023 - November 2023)', expanded=expand):
     st.write('Our team secured 10th place out of 160 teams nationwide, showcasing top-tier analytical skills and problem-solving abilities in a highly competitive environment. We applied advanced machine learning techniques to analyze and interpret data for Core Mass clients of the Bank of the Philippine Islands (BPI), resulting in the identification of actionable business insights.')
     st.caption('Skills: Data Analysis, Machine Learning (Clustering), Time Series Analysis and Forecasting, Hypothesis Testing')

#st.title('🛠️ Skills & Tools')
#st.write("""Peek at the skills and tools I've been refining!""")
#expand=False
#with st.expander('**Data Science**', expanded=expand):
     #st.write('Python (Pandas, Numpy)')
#with st.expander('**Statistics**', expanded=expand):
     #st.write('Statistical Analysis (Hypothesis Testing), Time Series Analysis and Forecasting, Probability Theory')

st.title("📑 Research")
st.write("""Here are some research I was part of!""")
with st.expander('💉 **3rd DLSU Senior High School Congress** - Spatial Mapping and Modeling of Reported Dengue Incidences in Luzon', expanded=expand):
     st.write('In this paper, we aimed to determine the significant correlates that affect dengue incidences, mapped the incidence rate of dengue cases, and explored the clustering of recorded dengue cases through the use of Poisson and Negative Binomial regression analyses and Multiple Linear Regression Models.')

def my_widget(key):
    return st.button(key)

with st.sidebar:
    st.subheader("Currently, I'm...")
    st.write("Working on a forecasting project 📈")
    st.write("Playing Hades ⚔️")

    st.subheader("""Let's connect!""")
    st.page_link("https://www.linkedin.com/in/yumoldianne/", label="LinkedIn", icon="🤝")
    st.page_link("https://github.com/yumoldianne", label="GitHub", icon="🤖")