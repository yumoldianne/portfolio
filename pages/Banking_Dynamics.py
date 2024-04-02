import streamlit as st
from st_pages import Page, add_page_title, show_pages, hide_pages

st.set_page_config(
    page_title="Banking Dynamics",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

show_pages(
    [
        Page("Home.py", "Home", "🏠"),
        Page("pages/Data_Science_Projects.py", "Data Science Projects", "📊"),
        Page("pages/Work_Experience.py", "Work Experience", "💼"),
        Page("pages/Other_Projects.py", "Other Projects", "📦"),
        Page("pages/Banking_Dynamics.py", "Banking Dynamics", "🏦")
    ]
)

hide_pages(["Banking Dynamics"])

st.title("Banking Dynamics with Customer Segmentation and Time Series Analysis")
st.page_link("https://drive.google.com/file/d/1mzKGFkiQDqgd0JY-7a6e7dQv8PhMZlW5/view?usp=sharing", label="View in Github", icon="🤖")
st.subheader("Introduction")
st.caption("In the rapidly evolving landscape of banking and finance, there is an abundance of transactional data and a gap for data innovation.")
st.write("""
We initiated Project DECIPHER to derive actionable insights in the banking and finance sector, bridging the gap in data innovation. The project employed five key methodologies: Data Cleaning, Exploratory Data Analysis, Customer Segmentation Optimization, Intelligent Application, and Analysis. Notably, Customer Segmentation Optimization involved comparing five clustering algorithms, while the Intelligent Application phase featured Hypothesis Testing via Kruskal-Wallis test, AI-driven Advertising Insights (ARIA), and Time Series Forecasting via Prophet.
""")

st.subheader("Methods")
st.write("""
Project DECIPHER followed five main procedures: Data Cleaning, Exploratory Data Analysis, Customer Segmentation Optimization, Intelligent Application, and Analysis. The data underwent rigorous cleaning and preprocessing before being analyzed using various clustering techniques. K-Means emerged as the optimal model for customer segmentation, backed by robust performance metrics and clear visualizations. Hypothesis testing validated the clustering results, while AI-driven Advertising Insights and Time Series Forecasting offered promising avenues for personalized marketing strategies.
""")

st.subheader("Results")
st.write("""
Project DECIPHER's analysis culminated in the identification of five distinct customer segments, each characterized by unique behavioral patterns and transactional tendencies.
""")

container = st.container(border=True)
container.write("✅ **Conclusion**")
container.write("From this project, I learned...")

with st.sidebar:
    st.subheader("Currently, I'm...")
    st.write("Working on a forecasting project 📈")
    st.write("Playing Hades ⚔️")

    st.subheader("""Let's connect!""")
    st.write("📧 Email")
    st.page_link("https://www.linkedin.com/in/yumoldianne/", label="LinkedIn", icon="🤝")
    st.page_link("https://github.com/yumoldianne", label="GitHub", icon="🤖")