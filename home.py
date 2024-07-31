import streamlit as st

st.set_page_config(page_title="Sportans || Revolutionizing Sports Coaching", layout="wide")
st.sidebar.write("Created with ❤️ by Team Sportans")

# --- Page Setup ---

home_page = st.Page(
    page="./Pages/Home_Page.py",
    title="🏠 Welcome to Sportans",
    default=True
)

about_page = st.Page(
    page="./Pages/2_About_US.py",
    title="👥 About Us - Our Story"
)

register_page = st.Page(
    page="./Pages/3_Register.py",
    title="📝 Register & Get Started"
)

chatbot_page = st.Page(
    page="./Pages/4_ChatBot.py",
    title="🤖 Chat with CoachBot"
)

events_page = st.Page(
    page="./Pages/5_Manage_Events.py",
    title="📅 Manage Your Events"
)

diet_page = st.Page(
    page="./Pages/6_Diet_Recommendations.py",
    title="🥗 Personalized Diet Plans"
)

actions_page = st.Page(
    page="./Pages/8_User_Actions.py",
    title="🔄 Track Your Actions"
)

statistics_page = st.Page(
    page="./Pages/9_Player_Statistics.py",
    title="📊 Player Statistics"
)

user_guide_page = st.Page(
    page="./Pages/10_User Guide.py",
    title="📚 User Guide"
)

fitness_tracking_page = st.Page(
    page="./Pages/11_Fitness_Tracking.py",
    title="🏃 Fitness Tracking & Analysis"
)

# --- Navigation ---

pg = st.navigation({
    "Home" : [home_page],
    "Login/Register" : [register_page],
    "Features":[events_page,diet_page],
    "Login Required Features" : [chatbot_page,actions_page,statistics_page],
    "Info": [user_guide_page,about_page] 
    })

pg.run()
