import streamlit as st
from st_pages import add_page_title, get_nav_from_toml, hide_pages

st.set_page_config(
    page_title="Data Science Projects",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

hide_pages(["Banking Dynamics", "Mental Health Discourse Classifier"])

def my_widget(key):
    return st.button(key)

st.title("📊 Data Science Projects")
st.write("Delve into the projects I poured my heart into!")
st.write("My projects have two classifications: :violet[projects] and :blue[mini-projects].")

expand=False

#tab1, tab2, tab3 = st.tabs(["Projects", "Competitions", "Mini-Projects"])
tab1, tab2 = st.tabs(["Projects", "Mini-Projects"])

with tab1:
   st.header("💻 Projects")
   st.write("Projects are executed demonstrations of advanced data extraction and analysis techniques and visualization methodologies, designed to uncover intricate patterns and communicate complex insights.")
   st.subheader("🏘️ Airbnb Market Analysis")
   container = st.container(border=True)
   container.image("images/Airbnb Market Analysis.png")
   container.write("Our project analyzed the Airbnb data from Big Bear and Joshua Tree, California, aiming to optimize Airbnb hosts' occupancy rates and forecast future revenue and occupancy. We examined key market trends and listing characteristics and we identified factors influencing rental prices through regression models (Support Vector Machines, Random Forests, XGBoost). Using time series forecasting (Facebook Prophet, ARMA, ARIMA, SARIMA), we predicted revenue and occupancy rates. This analysis equips Airbnb hosts with data-driven insights to enhance listing performance and capitalize on market opportunities.")
   container.page_link("https://drive.google.com/file/d/1tGVg8B8PyKTgAXisYzJP8KnNZYds1zAD/view?usp=sharing", label = "Read more about the project here!", icon ="🗃️")
   #container.caption("Tools: ")
   #st.subheader("🪹 Nestbox")
   #container = st.container(border=True)
   #container.caption("Project Overview")
   #container.write("This project...")
   #container.caption("Tools: Streamlit")
   st.subheader("🧘 Mental Health Patterns in Pandemic Discourse Classifier")
   container = st.container(border=True)
   container.image("images/MindInsight Classifier.jpg")
   container.write("We developed Convolutional Neural Network (CNN) and Long Short-Term Momory (LSTM) models trained on a varied dataset of Reddit posts discussing mental health during the pandemic. The project aimed to classify posts into categories like anxiety, schizophrenia, and more, shedding light on the complexities of identifying overlapping symptoms and understanding the language used by those experiencing these conditions.")
   container.page_link("pages/MH_DisClass.py", label = "Read more about the project here!", icon ="🗃️")
   st.subheader("🏦 Banking Dynamics with Customer Segmentation and Time Series Analysis")
   container = st.container(border=True)
   container.image("images/title slide.png")
   container.write("Presented in Philippine Junior Data Science Challenge 2023. We conducted a data science project for a bank, emphasizing customer segmentation and time series forecasting to improve business decisions and customer satisfaction. Our work included data cleaning, exploratory analysis, and optimizing segmentation with five clustering algorithms. We also conducted hypothesis testing using the Kruskal-Wallis test and employed Prophet for time series forecasting.")
   container.page_link("pages/Banking_Dynamics.py", label = "Read more about the project here!", icon ="🗃️")
   st.subheader("💉Spatial Mapping and Modeling of Reported Dengue Incidences in Luzon")
   container = st.container(border=True)
   container.image("images/Spatial Mapping and Modelling.png")
   container.write("Presented in the 3rd DLSU Student High School Research Congress, this project focused on analyzing the spatial distribution of dengue incidences across Luzon provinces in 2018. It aimed to identify factors influencing dengue cases, map the incidence rates, and examine clustering of cases. The research used statistical methods including Poisson and Negative Binomial regression, along with Multiple Linear Regression Models. Results highlighted rainfall and poverty incidence as significant factors affecting dengue rates. Provinces like Nueva Ecija and Tarlac exhibited high dengue counts and incidence, indicating clustering.")
   container.page_link("https://animorepository.dlsu.edu.ph/cgi/viewcontent.cgi?article=1621&context=conf_shsrescon", label = "Read more about the project here!", icon ="🗃️")
   st.subheader("📅 Economic Calendar Web Scraper")
   container = st.container(border=True)
   #container.image("images/title slide.png")
   container.write("This project utilized Selenium and BeautifulSoup to scrape economic calendar data from multiple websites and collected and organized event data by country, impact level, and asset type.")
   container.caption("*Please note that due to internship constraints, I'm unable to provide further details about this project.*")
   #st.subheader("📝 Ateneo AISIS Enlistment Dashboard")
   #container = st.container(border=True)
   #container.image("images/title slide.png")
   #container.write("The project involved analyzing the enlistment process of Ateneo de Manila University to identify data metrics at each stage. From this analysis, a dimensional data schema was devised, detailing the necessary information for each step. Mock data was then generated and populated into fact and dimension tables to simulate the enrollment process. Subsequently, a dashboard using streamlit and plotly was created utilizing the mock data. OLAP operations were applied to extract further insights from the data, exploring trends and patterns within the enrollment process.")
   #container.caption("*Coming soon!*")

#with tab2:
    #st.header("⚙️ Competitions")
    #st.write("Competitions are projects submitted...")
    

with tab2:
   st.header("📈 Mini-Projects")
   st.write("Mini-projects, on the other hand, are brief exercises in data analysis and visualization. They're used to test new libraries and experiment with different types of visualizations. All my mini-projects are centralized in one repository called Datasette.")
   st.page_link("https://github.com/yumoldianne/datasette", label = "Check out Datasette here!", icon = "📼")
   st.subheader("🚗 Time Series Analysis of Motor Vehicle Collisions in the United States")
   container = st.container(border=True)
   container.caption("Project Overview")
   container.write("This project addressed the significant challenge of motor vehicle crashes in the United States. We aimed to improve resource allocation and proactive interventions by estimating anticipated accidents. Exploratory analysis revealed autocorrelation and non-stationarity, leading to data transformation and the use of various time series models. The ARMA(4, 2) model emerged as the most suitable, effectively capturing systematic trends and abrupt disturbances. The model's performance during the COVID-19 pandemic, reflecting changes in traffic patterns, highlights its ability to adapt to evolving conditions and underscores the need for continuous model refinement to ensure road safety.")
   container.page_link("https://drive.google.com/file/d/1FGcGVnIIdfKhLPK7r2ZvxlIhlde5zwn4/view?usp=sharing", label = "Read more about the project here!", icon ="🗃️")
   st.subheader("🍃 Air Quality Analysis in Pre- and Post-Pandemic Philippines")
   container = st.container(border=True)
   container.write("Employing various data science techniques such as spatial analysis and time series analysis, this project will attempt to uncover insights into air quality trends and changes.")
   container.caption("*Coming soon!*")
   st.subheader("🪙 E-Commerce Sales Forecast")
   container = st.container(border=True)
   container.image("images/E-Commerce Sales Forecast.png")
   container.write("This project utilized exploratory data analysis techniques to identify patterns, trends, and insights within the e-commerce dataset and applied time series forecasting techniques using Prophet to predict sales for the upcoming year. K-Means clustering algorithm was applied to categorize customers into distinct segments based on their purchasing behavior.")
   #container.caption("Tools: Pandas, Seaborn, Matplotlib, Plotly Express, scikit-learn, Prophet")
   st.subheader("🎓 Analysis of Graduate Admissions Machine Learning Models")
   container = st.container(border=True)
   container.image("images/CSCI 111 Project Slides.png")
   container.write("Utilizing K-Nearest Neighbors, Decision Trees, and Random Forest algorithms for classification and regression tasks, this project aims to provide insights into the importance of various admission parameters such as GRE scores, TOEFL scores, University Rating, and others.")
   #container.caption("Tools: scikit-learn, Pandas, Seaborn, Matplotlib")
   st.subheader("🎶 Song Database using DynamoDB")
   container = st.container(border=True)
   container.image("images/Group 6_Database Presentation.png")
   container.write("We developed a DynamoDB-based song database for an online streaming service, enabling efficient querying with over 5000 stream entries, artist, album, and song information. This project utilized various access patterns, including base tables, LSIs, and GSIs, to cater to users, artists, developers, and the music industry.")
   #container.caption("Tools: DynamoDB")
   st.subheader("🗨️ Rumor Propagation Model using Agent-Based Modelling")
   container = st.container(border=True)
   container.image("images/CSCI 115-O Final Presentation.png")
   container.write("We conducted an agent-based modeling project to simulate and analyze the propagation of rumors in various scenarios, considering factors such as acceptance rates, introduction times, and starting locations. The results highlight the significant impact of these factors on the spread of rumor and truth, providing insights for effective intervention strategies.")
   #container.caption("Tools: agentpy")


with st.sidebar:
    st.subheader("Currently, I'm...")
    st.write("Working on a forecasting project 📈")
    st.write("Playing Hades ⚔️")

    st.subheader("""Let's connect!""")
    st.page_link("https://www.linkedin.com/in/yumoldianne/", label="LinkedIn", icon="🤝")
    st.page_link("https://github.com/yumoldianne", label="GitHub", icon="🤖")