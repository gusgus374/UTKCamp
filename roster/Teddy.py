# write code below!
import streamlit as st

st.title("What do you want build today")

my_vid = st.file_uploader("whatever")

if st.button("show my video"):
    st.video(my_vid)
    
if st.button("teddygoal"):
    st.video("./media/teddygoal.mp4")

if st.button("teddycooks"):
    st.video("./media/teddycooks.mp4")

with st.expander("Show Teddy's code"):
    st.code(
        body='''
import streamlit as st

st.title("What do you want build today")

my_vid = st.file_uploader("whatever")

if st.button("show my video"):
    st.video(my_vid)
    
if st.button("teddygoal"):
    st.video("./media/teddygoal.mp4")

if st.button("teddycooks"):
    st.video("./media/teddycooks.mp4")
        ''',
        language="python",
        line_numbers=True
    )