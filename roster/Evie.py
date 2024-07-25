# write code below!
import streamlit as st

st.title("What do you want to build today?")

#my_video = st.file_uploader("upload something, BRO")

if st.button('Evie Skill'):
    st.video("./media/evieskill.mp4")
    #st.video(my_video)

with st.expander("Show Evie's code"):
    st.code(
        body='''
import streamlit as st

st.title("What do you want to build today?")

#my_video = st.file_uploader("upload something, BRO")

if st.button('Evie Skill'):
    st.video("./media/evieskill.mp4")
    #st.video(my_video)
        ''',
        language="python",
        line_numbers=True
    )