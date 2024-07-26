# write code below!
import streamlit as st
import pandas as pd
import altair as alt


st.title("Hi I'm Kellan")
st.write("What I liked about camp this week was how I learned to code and to see my data on the trackers. ")
if st.button('Left Foot Goal'):
  st.video("./media/LeftFootGoal.mp4")
if st.button('Epic Slide Tackle'):
  st.video("./media/EpicSlideTackle.mp4")
if st.button('Epic Goal'):
  st.video("./media/EpicGoal.mp4")
  
st.header("Graph example")

file_location = "./data/last30days_GPS.csv"

data = pd.read_csv(file_location)

group_data = pd.DataFrame(data)

players_data = group_data.loc[(group_data["Player Name"] == "Kellan - SL") | (group_data["Player Name"] == "Gregory - SL") | (group_data["Player Name"] == "Teddy - SL") | (group_data["Player Name"] == "Bowman - SL")]

st.dataframe(players_data)

lines = alt.Chart(players_data, title="My interactive chart").mark_line().encode(
        x="Session Title:T",#the little ":T" after "Session Title" tells altair that this data is a time or date value
        y="Top Speed (m/s)",
        color="Player Name"
)

circles = alt.Chart(players_data).mark_circle().encode(
        x="Session Title:T",
        y="Top Speed (m/s)",
        color="Player Name",
        size=alt.Size("Distance (km)",legend=None),
        tooltip=["Player Name","Session Title","Top Speed (m/s)", "Split Name", "Distance (km)"]
)

combined_chart = (lines + circles).interactive()
st.altair_chart(combined_chart, use_container_width=True)

with st.expander("Show Kellen's code"):
    st.code(
        body='''
import streamlit as st
import pandas as pd
import altair as alt


st.title("Hi I'm Kellan")
st.write("What I liked about camp this week was how I learned to code and to see my data on the trackers. ")
if st.button('Left Foot Goal'):
  st.video("./media/LeftFootGoal.mp4")
if st.button('Epic Slide Tackle'):
  st.video("./media/EpicSlideTackle.mp4")
if st.button('Epic Goal'):
  st.video("./media/EpicGoal.mp4")
  
st.header("Graph example")

file_location = "./data/last30days_GPS.csv"

data = pd.read_csv(file_location)

group_data = pd.DataFrame(data)

players_data = group_data.loc[(group_data["Player Name"] == "Kellan - SL") | (group_data["Player Name"] == "Gregory - SL") | (group_data["Player Name"] == "Teddy - SL") | (group_data["Player Name"] == "Bowman - SL")]

st.dataframe(players_data)

lines = alt.Chart(players_data, title="My interactive chart").mark_line().encode(
        x="Session Title:T",#the little ":T" after "Session Title" tells altair that this data is a time or date value
        y="Top Speed (m/s)",
        color="Player Name"
)

circles = alt.Chart(players_data).mark_circle().encode(
        x="Session Title:T",
        y="Top Speed (m/s)",
        color="Player Name",
        size=alt.Size("Distance (km)",legend=None),
        tooltip=["Player Name","Session Title","Top Speed (m/s)", "Split Name", "Distance (km)"]
)

combined_chart = (lines + circles).interactive()
st.altair_chart(combined_chart, use_container_width=True)
        ''',
        language="python",
        line_numbers=True
    )