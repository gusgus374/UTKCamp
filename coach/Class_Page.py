import streamlit as st
import pandas as pd
import numpy as np
import datetime
import altair as alt
import time 
import os
import pathlib
import streamlit.components.v1 as components


st.title("CLASS PAGE - example")
st.code('''
st.title("CLASS PAGE - example")
        ''')

st.header("Python Libraries used:")
st.code('''
import streamlit as st
import pandas as pd
import os
import pathlib
import altair as alt
import streamlit.components.v1 as components
        ''')

#uploaded_file = st.file_uploader("Choose a data file")
#if uploaded_file is not None:
        # use the Pandas read_csv method to read the gps_data and turn into a dataframe
#        all_data = pd.read_csv(uploaded_file)
        # keep only the rows were the column 'Split Name' has a value equal to 'all'
 #       game_data = all_data.loc[all_data['Split Name'] == "game"]
        #game_data = game_data.loc[game_data['Tags'] == 'game']
  #      game_data = game_data.set_index('Player Name', drop=False)
        #game_data["day"] = game_data["Date"] - 45150
        #game_data = game_data.loc[game_data["day"] > 0]
   #     with st.expander(label="View Your Data",expanded=False):
                #display the uploaded data
    #            st.write(game_data)
     #   variable_x = st.selectbox("Pick Your X Variable!",game_data.columns.to_list(),1)
      #  variable_y = st.selectbox("Pick Your Y Variable!",game_data.columns.to_list(),8)
       # variable_size = st.selectbox("Pick Your Size Variable!",game_data.columns.to_list(),9)
#if uploaded_file is not None:
 #   chart = alt.Chart(game_data).mark_circle().encode(
  #      x=variable_x,
   #     y=variable_y,
    #    size=alt.Size(variable_size,legend=None),
     #   color=alt.Color('Player Name',legend=None),
      #  tooltip=["Player Name","Session Title",]).properties(height=500).interactive()
    #st.altair_chart(chart, theme="streamlit", use_container_width=True)
with st.echo("below"):
    st.header("Graph example")

    file_location = os.path.join(str(pathlib.Path().resolve()), './data/last30days_GPS.csv')

    with open(file_location) as file:
            data = pd.read_csv(file)

    ETFS_data = pd.DataFrame(data)

    SLIdata = ETFS_data.loc[(ETFS_data["Player Name"] == "Mr. Josh - ETFS") | (ETFS_data["Player Name"] == "Ms. Mona - ETFS") | (ETFS_data["Player Name"] == "Mr. Jaylen - ETFS")]
    with st.expander("See the dataframe as a table"):
        st.dataframe(SLIdata)

    lines = alt.Chart(SLIdata, title="My interactive chart").mark_line().encode(
            x="Session Title:T",#the little ":T" after "Session Title" tells altair that this data is a time or date value
            y="Top Speed (m/s)",
            color="Player Name"
    )

    circles = alt.Chart(SLIdata).mark_circle().encode(
            x="Session Title:T",
            y="Top Speed (m/s)",
            color="Player Name",
            size=alt.Size("Distance (km)",legend=None),
            tooltip=["Player Name","Session Title","Top Speed (m/s)", "Split Name", "Distance (km)"]
    )

    combined_chart = (lines + circles).interactive()
    st.altair_chart(combined_chart, use_container_width=True)

st.header("_Something Unique_")
with st.echo("below"):
    st.header("Soccer... and Data... *and* Science?")
    st.write("Hi I'm Coach Gus and I love soccer and physics. I enjoy teaching others about my passions and believe learning math and science does not have to be boring!")
    st.write("My favorite club team in England is :red[Liverpool FC] and I admire how their data science team combined physics knowledge with soccer knowledge to help the coaching staff better analyze the game.")
    st.subheader("One of the biggest soccer clubs in the world, Liverpool FC, hired particle physicists to help improve their soccer team")

    col1, col2 = st.columns(2)
    col1.write("They used their knowledge of charged particles and electric fields:")
    col2.write("And combined it with soccer data to create this (known as the Pitch Control model):")
    with col2:
            iframe_src2 = "https://www.youtube.com/embed/Nc3uFWnPlsQ?si=pUx4ouf0EhWYMrVE"
            components.iframe(iframe_src2,600,500)

    with col1:
            iframe_src = "https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_en.html"
            components.iframe(iframe_src,height=500)
            st.caption("Hint: make sure to click the 'Voltage' checkbox then drag and drop the red and blue particels around")
    st.subheader("The invention of the Pitch Control model helps coaches answer questions like:")
    st.write(':orange["when is the right moment in the game to press and try to win the ball back?"]')
    st.subheader("or")
    st.write(':orange["in what areas of the field do our oppenents have a weakness we should attack?"]')
