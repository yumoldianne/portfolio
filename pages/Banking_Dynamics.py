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
        #Page("pages/Other_Projects.py", "Other Projects", "📦"),
        Page("pages/Banking_Dynamics.py", "Banking Dynamics", "🏦"),
        Page("pages/MH_DisClass.py", "Mental Health Discourse Classifier", "🧠")
    ]
)

hide_pages(["Banking Dynamics", "Mental Health Discourse Classifier"])
st.image("images/title slide.png")

st.header("🏦 Banking Dynamics with Customer Segmentation and Time Series Analysis")
col1, col2, col3= st.columns([0.2, 0.2, 0.6], gap = "small")
with col1:
    st.page_link("https://github.com/yumoldianne/banking-dynamics", label="View in Github", icon="🤖")
with col2:
    st.page_link("https://drive.google.com/file/d/1DbrreSkAiNZj1Yw5AdlDtj-eLnHdg3c2/view?usp=sharing", label ="Read the report", icon="📄")

st.write("In the rapidly evolving landscape of banking and finance, the abundance of transactional data poses a significant challenge. Financial institutions accumulate massive volumes of transactional data daily. With so much transaction data, :violet[how can banks harness data to derive actionable insights for business decision-making and initiatives?] ")

st.subheader("Exploratory Data Analysis")
st.image("images/banking/title slide.png")
st.image("images/banking/title slide (1).png")
st.image("images/banking/title slide (2).png")

st.subheader("Data Processing Steps")
st.write("""
**Data Cleaning:** Data cleaning involved removing inconsistencies, duplicates, and missing values in the dataset. This step was necessary to ensure the accuracy and reliability of subsequent analyses. Clean data is fundamental for obtaining meaningful insights and making informed decisions.
""")

st.write("""
**Data Aggregation:** Aggregating the data involved combining multiple datasets or rows into summarized information. This was essential to condense the data and extract meaningful patterns or trends. Aggregation simplifies the analysis process, making it more manageable and efficient.
""")

st.write("""
**One-Hot Encoding:** Employed to convert categorical data into a numerical format, representing them as binary vectors. This step was necessary as machine learning models typically operate on numerical data. It ensures compatibility and allows models to interpret categorical information during analysis.
""")

st.write("""
**Standard Scaling:** Involved transforming numerical features to a standard scale (mean of 0 and standard deviation of 1). This step was necessary to prevent features with larger scales from dominating the analysis. Standardized features ensure that each feature contributes equally to the machine learning model, enhancing its performance and accuracy.
""")

st.image("images/banking/title slide (3).png")
st.image("images/banking/title slide (4).png")

st.write("""
The analysis culminated in precise categorization of the client base, discovering five discrete segments, each distinguished by unique behavioral traits. Despite the fact that for some variables, few clusters did not exhibit significant differences, they can still be characterized through other relevant variables.
""")

st.subheader("Customer Segmentation")
st.write("""
From there, we identified generalizations for each of the cluster: """)
expand=False
with st.expander('**Cluster 0: Usual Customers**', expanded=expand):
    st.write("These are customers with minimal transaction activity, primarily using banking services for storing money without engaging in specific transaction types regularly. They are not easily categorized into specific segments.")
with st.expander('**Cluster 1: Young Transaction Magnet**', expanded=expand):
    st.write("This cluster consists of the youngest customers with relatively low tenure. They exhibit high levels of debit transactions and digital activities such as web and e-wallet payments but lack credit and outgoing transactions. Encouraging them to explore credit options could be beneficial given their digital inclinations.")
with st.expander('**Cluster 2: Mobile-Oriented Shoppers**', expanded=expand):
    st.write("Customers in this cluster have the highest tenure, mostly mid-aged, and are significantly engaged in credit card and digital transactions. They prefer mobile channels, paying bills, and conducting numerous debit transactions. Notably, outgoing transactions are absent among this group.")
with st.expander('**Cluster 3: Tech-driven Entrepreneurs**', expanded=expand):
    st.write("This cluster includes customers engaging in various transaction types except for credit transactions. They have a relatively short tenure similar to Cluster 1, exhibiting high debit transaction activity, especially in terms of count. These customers are characterized by their tech-savvy behavior and lead in outgoing transactions despite limited digital transaction activity.")
with st.expander('**Cluster 4: Traditional Debit Users**', expanded=expand):
    st.write("These customers have moderate tenure with limited exposure to credit transactions. They rely primarily on traditional transaction methods, showing a relatively high level of debit activity.")

st.subheader("Time-Series Forecasting")

st.write("""
To predict transaction trends per cluster and understand patterns that can aid in planning and strategizing for the future, we utilized Prophet, an open-source forecasting model developed by Meta. By leveraging the transaction data from each identified cluster, we employed Prophet to forecast transaction trends over time. This approach enabled us to anticipate how each customer segment might evolve in their transaction behaviors, providing valuable insights for tailored marketing initiatives and product development strategies. 
""")

st.image("images/banking/title slide (5).png")

container = st.container(border=True)
container.write("✅ **Conclusion**")
container.write("From this project, I learned how to implement a comprehensive data science project. This was also my first forray into machine learning and time series forecasting.")

with st.sidebar:
    st.subheader("Currently, I'm...")
    st.write("Working on a forecasting project 📈")
    st.write("Playing Hades ⚔️")

    st.subheader("""Let's connect!""")
    st.page_link("https://www.linkedin.com/in/yumoldianne/", label="LinkedIn", icon="🤝")
    st.page_link("https://github.com/yumoldianne", label="GitHub", icon="🤖")