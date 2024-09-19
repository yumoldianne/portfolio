import streamlit as st
from st_pages import add_page_title, get_nav_from_toml, hide_pages

st.set_page_config(
    page_title="Work Experience",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

sections = st.sidebar.toggle("Sections", value=True, key="use_sections")

#nav = get_nav_from_toml(".streamlit/pages.toml")

#pg = st.navigation(nav)

add_page_title(pg)

hide_pages(["Banking Dynamics", "Mental Health Discourse Classifier"])

def my_widget(key):
    return st.button(key)

st.title('💼 Work Experience')
st.write("""Take a look at the work I've been doing.""")
expand=False
with st.expander('🥤 **Coca-Cola Beverages Philippines, Inc.** - Analytics and Insights Intern (May 2024 - Present)', expanded=expand):
     st.write("""As an analytics and insights intern, I work under the Modern Trade Commercial Analytics & Insights team. I perform E2E analysis of data from key accounts to support cross-functional business planning.""")
     st.caption('Skills: Data Analysis')
with st.expander('💵 **Undisclosed Hedge Fund** - Data Operator Intern (March 2024 - April 2024)', expanded=expand):
     st.write("""As a data operator intern, I utilized Python for web-scraping and data processing tasks and employing libraries such as:""")
     st.write("""- Selenium and BeautifulSoup to scrape economic calendar data from multiple websites and collected and organized event data by country, impact level, and asset type and, """) 
     st.write("""- Pandas and Numpy to enhance data manipulation efficiency.""")
     st.caption('Skills: Web Scraping, Data Processing, Data Cleaning')
with st.expander('⚡ **Energy Innovation Capital** - VC Industry Research and Data Analytics Extern (December 2023 - February 2024)', expanded=expand):
     st.write('As an extern, I conducted basic exploratory research on one of the emerging segments within the energy sector (geothermal energy) and identified interesting players, including public companies, private companies, and startups, in the industry that are developing innovations and dominating the market share. I also used data analytics tools to discover insights about the emerging markets in energy sector, learned to organize, analyze, and visualize data, and delivered a compelling presentation showcasing insights into the market landscape.')
     st.caption('Skills: Market Research, Data Analysis, Deal Sourcing, Project Management')
with st.expander('📰 **The Guidon** - Research and Development Analyst (June 2023 - Present)', expanded=expand):
     st.write('As an R&D analyst, I conducted in-depth research and analysis using Microsoft Excel, synthesizing data from diverse sources to generate quantitative reports for two groups, each with 15+ members. I also implemented data visualization techniques, resulting in an increase in the clarity and accessibility of information for staff teams, thereby enhancing the decision-making process.')
     st.caption('Skills: Data Analysis, Data Visualization, Data Collection')

st.title('🎒 Co-Curricular Activities & Competitions')
st.write("""Explore the projects I've been involved with at different organizations.""")
with st.expander('🧑‍🤝‍🧑 **Ateneo Mathematics Society** - Internals Associate (June 2024 - Present)', expanded=expand):
     st.write('As an interals associate, I Facilitated the distribution and collection of evaluation forms and feedback reports across all Ateneo Mathematics Society projects and pools, ensuring timely and comprehensive feedback. I led the creation and execution of various formation and training seminars within the organization, enhancing member skills and knowledge. I managed special projects under the Internals Office, including the Sets System and other member engagement initiatives, driving participation and community building. Finally, I  assisted in handling human resource-related efforts, contributing to the effective management of member relations and welfare')
     st.caption('Skills: Training and Development, Team Management')
with st.expander('🧑‍🤝‍🧑 **Ateneo Mathematics Society** - Member Relations Department Head (June 2023 - June 2024)', expanded=expand):
     st.write('As a member relations department head, I oversee and lead the Member Relations Department, ensuring effective communication and collaboration between the organization and its members. I also selected and currently manage a team of heads to smoothly operate the department.')
     st.caption('Skills: Project Management, Team Management')
with st.expander('🌹 **Ateneo Blue Rose** - Deputy for External Relations (April 2024 - May 2024)', expanded=expand):
     st.write('Blue Rose is the annual culminating event of graduating Seniors & Super Seniors of the Loyola Schools. As a deputy for external relations, I lead a team that handles partnership proposals for food and beverage vendors.')
     st.caption('Skills: Project Management, Communication')
with st.expander('📃 **Ateneo Mathematics Society** - Leadership Training Seminar Logistics-Platforms Committee (February 2024 - Present)', expanded=expand):
     st.write('As a logistics-platforms committee member, I am in charge of handling the onsite logistics of the event, which includes but not limited to contingencies and mobility plans.')
     st.caption('Skills: Project Management')
with st.expander('💻 **Philippines Junior Data Science Challenge** - Finalist (Top 10 out of 160 teams) (August 2023 - November 2023)', expanded=expand):
     st.write('Our team secured 10th place out of 160 teams nationwide, showcasing top-tier analytical skills and problem-solving abilities in a highly competitive environment. We applied advanced machine learning techniques to analyze and interpret data for Core Mass clients of the Bank of the Philippine Islands (BPI), resulting in the identification of actionable business insights.')
     st.caption('Skills: Data Analysis, Machine Learning (Clustering), Time Series Analysis and Forecasting, Hypothesis Testing')
#with st.expander('🗺️ **ASEAN Data Science Explorers** - XX (April 2024 - June 2024)', expanded=expand):
     #st.write('Our team secured...')
     #st.caption('Skills: Data Analysis, Data Visualization (SAP Analytics Cloud), Software Deployment (SAP Build Apps)')
     #st.page_link("", label = "Read our data storyboard here!, icon = '🗃️")
#with st.expander('💡 **ImaGnation: GCash Innovation Challenge** - Participants (April 2024)', expanded=expand):
     #st.write('Our team secured...')
     #st.caption('Skills: Concept Ideation, Problem-Solving')
     #st.page_link("", label = "Read our pitch, G for Gigi, here!, icon = '🗃️")

st.title('🛠️ Skills & Tools')
st.write("""Peek at the skills and tools I've been refining!""")
expand=False
with st.expander('👩‍💻 **Programming Languages**', expanded=expand):
     st.write(' Python, SQL, R, HTML, CSS')
with st.expander('📊 **Data Science, Big Data & Machine Learning**', expanded=expand):
     st.write('MongoDB, DynamoDB, Python (e.g. scikit-learn, NLTK, PyTorch, Numpy, Pandas, Matplotlib, Seaborn), Data Science Pipeline (cleaning, wrangling, visualization, modeling, interpretation), Web Scraping (Selenium, BeautifulSoup)')
with st.expander('🎲 **Statistics**', expanded=expand):
     st.write('Statistical Analysis (Hypothesis Testing), Multiple Linear Regression, ANOVA, Time Series and Forecasting, Probability Theory')

def my_widget(key):
    return st.button(key)