# write code below!
import streamlit as st

st.title("Jameson's App")

vid = st.file_uploader("upload pls")
vid2 = st.file_uploader("Yup")
vid3 = st.file_uploader("Teehee")

if st.button("My Favorite Goal"):
    #st.video(vid)
    st.video("./media/I'mBetterThanTaylor.mp4")
    
if st.button("Kellan Flying"):
    st.video(vid2)
    
if st.button("Evan Falls Like A Toddler"):
    st.video(vid3)

with st.expander("Show Jameson's code"):
    st.code(
        body='''
import streamlit as st

st.title("Jameson's App")

vid = st.file_uploader("upload pls")
vid2 = st.file_uploader("Yup")
vid3 = st.file_uploader("Teehee")

if st.button("My Favorite Goal"):
    #st.video(vid)
    st.video("./media/I'mBetterThanTaylor.mp4")
    
if st.button("Kellan Flying"):
    st.video(vid2)
    
if st.button("Evan Falls Like A Toddler"):
    st.video(vid3)
        ''',
        language="python",
        line_numbers=True
    )