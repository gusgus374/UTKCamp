# write code below!
import streamlit as st

st.title("What do you want build today")

my_vid = st.file_uploader("whatever")

st.video(my_vid)