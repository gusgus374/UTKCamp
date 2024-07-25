import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import pathlib
import streamlit as st
import altair as alt
from streamlit_ace import st_ace
import streamlit.components.v1 as components
#import folium
#from folium.plugins import HeatMap
#import seaborn as sns

st.set_page_config(
    page_title="footyLab • Play to Learn | DataRook, Inc.",
    page_icon="./media/DR_favicon.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

if "user" not in st.session_state:
    st.session_state.user = None
#if "password" not in st.session_state:
#     st.session_state.password = None

ROLES = [None,"Coach Gus", "Alex", "Bowman", "Carolina", "Dashley", "Deklan", "Evie", "Gabriel", "Gregory", "Jameson", "Kade", "Kellan", "Kylie", "Lucas", "Olivia", "Taylor", "Teddy"]
allroles = ["Coach Gus", "Alex", "Bowman", "Carolina", "Dashley", "Deklan", "Evie", "Gabriel", "Gregory", "Jameson", "Kade", "Kellan", "Kylie", "Lucas", "Olivia", "Taylor", "Teddy"]
playersdeployed = ["coach Gus", "Kylie", "Carolina", "Gregory", "Olivia", "Teddy", "Lucas", "Kade", "Kellan", "Gabriel", "Alex", "Bowman", "Dashley", "Evie", "Taylor", "Jameson"]
def login():

    st.header("Log in")
    user = st.selectbox("User", ROLES)
    #password = st.text_input("Password")

    if st.button("Log in"):
        st.session_state.user = user
        #st.session_state.password = password
        st.rerun()


def logout():
    st.session_state.user = None
    #st.session_state.password = None
    st.rerun()


user = st.session_state.user
#password = st.session_state.password

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

settings = st.Page("settings.py", title="Settings", icon=":material/settings:")

BootRoom = st.Page(
    "./coach/1_BootRoom.py",
    title="BootRoom",
    icon=":material/interactive_space:",
)
coachGus = st.Page(
    "./coach/coachGus.py", title="Coach's Examples", icon=":material/sports:",default=(user == "coach Gus")
)
classpage = st.Page(
    "./coach/Class_Page.py",
    title="Class Page",
    icon=":material/school:"
)

codeBox = st.Page(
    "./coach/codeBox.py", title="", icon=":material/person_play:",default=(user not in playersdeployed)
)
prosoccer = st.Page(
    "./coach/2_US_Pro_Soccer.py",
    title="Pro Soccer Data",
    icon=":material/sports_and_outdoors:",
)
#ayden = st.Page("./roster/ayden.py", title="Ayden", icon=":material/security:",default=(user=="Ayden"))

kylie = st.Page(
    "./roster/Kylie.py",
    title="Kylie's App",
    icon=":material/school:",
    default=(user == "Kylie")
)

carolina = st.Page(
    "./roster/Carolina.py",
    title="Carolina's App",
    icon=":material/school:",
    default=(user == "Carolina")
)

gregory = st.Page(
    "./roster/Gregorys_awsome_sus_bruh.py",
    title="Minecraft sus",
    icon=":material/school:",
    default=(user == "Gregory")
)

olivia = st.Page(
    "./roster/Olivia.py",
    title="Olivia's App",
    icon=":material/school:",
    default=(user == "Olivia")
)

teddy = st.Page(
    "./roster/Teddy.py",
    title="Teddy's App",
    icon=":material/school:",
    default=(user == "Teddy")
)

lucas = st.Page(
    "./roster/Lucas.py",
    title="Lucas's App",
    icon=":material/school:",
    default=(user == "Lucas")
)

kade = st.Page(
    "./roster/Kade.py",
    title="Kade's App",
    icon=":material/school:",
    default=(user == "Kade")
)

kellan = st.Page(
    "./roster/Kellan.py",
    title="Kellan's App",
    icon=":material/school:",
    default=(user == "Kellan")
)

gabriel = st.Page(
    "./roster/Gabriel.py",
    title="Gabriel's App",
    icon=":material/school:",
    default=(user == "Gabriel")
)

alex = st.Page(
    "./roster/Alex.py",
    title="Alex's App",
    icon=":material/school:",
    default=(user == "Alex")
)

bowman = st.Page(
    "./roster/Bowman.py",
    title="Bowman's App",
    icon=":material/school:",
    default=(user == "Bowman")
)

dashley = st.Page(
    "./roster/Dashley.py",
    title="Dashley's App",
    icon=":material/school:",
    default=(user == "Dashley")
)

evie = st.Page(
    "./roster/Evie.py",
    title="Evie's App",
    icon=":material/school:",
    default=(user == "Evie")
)

taylor = st.Page(
    "./roster/Taylor.py",
    title="Taylor's App",
    icon=":material/school:",
    default=(user == "Taylor")
)

jameson = st.Page(
    "./roster/Jameson.py",
    title="Jameson's App",
    icon=":material/school:",
    default=(user == "Jameson")
)

account_pages = [logout_page, settings]
explore_pages = [BootRoom, prosoccer]
build_pages = [codeBox, coachGus]
deployed_pages = [classpage, kylie, carolina, gregory, olivia, teddy, lucas, kade, kellan, gabriel, alex, bowman, dashley, evie, taylor, jameson]

page_dict = {}

if (st.session_state.user in allroles):
    page_dict["Build"] = build_pages
if (st.session_state.user in allroles):
    page_dict["Explore"] = explore_pages
if (st.session_state.user in allroles):
    page_dict["Deployed"] = deployed_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()

st.logo("./media/footyLab_v2_96_NB.png",link="https://datarook.com/")

st.divider()
st.header("Links and Resources")
col1, col2 = st.columns(2)
with col1:
      #st.subheader("Streamlit ~~Docs~~ Spellbook")
      st.page_link("https://docs.streamlit.io/develop/api-reference", label="Click me to read about Streamlit ~~methods~~ spells", icon="🪄")
      uploaded_file = os.path.join(str(pathlib.Path().resolve()), './data/last30days_GPS.csv')
      with open(uploaded_file) as f:
            btn = st.download_button(
                  label="Download Last 30 Days GPS Data",
                  data = f,
                  file_name="gps_data.csv",
                  mime="text/csv"
                )
with col2:
      st.page_link("https://www.notion.so/oneknoxcollective/79ae71c252cf40af9c6a303de4fb69a4?v=9d3007011c49427a85ce101431e1b5ce", label="Soccer Scientists", icon="🏡")
      st.page_link("https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/", label="Emoji Codes!", icon="😎")
      st.page_link("https://app.veo.co/clubs/datarook-academy/teams/soccer-lab/#recordings", label="Game Footage", icon="🎥")
      st.page_link("https://forms.gle/7Zn14EdkySSFArir8", label="Day 1 Info Form", icon="📋")
      