import streamlit as st

st.title("West Ham")

vid = st.file_uploader("upload pls")

if st.button("Arsenal"):
    #st.video(vid)
    st.video("./media/kadesgoal.mp4")

with st.expander("Show Kade's code"):
    st.code(
        body='''
import streamlit as st

st.title("West Ham")

vid = st.file_uploader("upload pls")

if st.button("Arsenal"):
    #st.video(vid)
    st.video("./media/kadesgoal.mp4")
        ''',
        language="python",
        line_numbers=True
    )