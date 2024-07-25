# write code below!
import streamlit as st

st.title("Manchesters Blue")

my_vid = st.file_uploader("sigma")

st.video(my_vid)

if st.button("lucas goal"):
    st.video("./media/lucasgoal.mp4")
    
if st.button("lucas banger"):
    st.video("./media/lucasbanger.mp4")
if st.button("lucas clip"):
    st.video("./media/lucasclip.mp4")

with st.expander("Show Lucas's code"):
    st.code(
        body='''
import streamlit as st

st.title("Manchesters Blue")

my_vid = st.file_uploader("sigma")

st.video(my_vid)

if st.button("lucas goal"):
    st.video("./media/lucasgoal.mp4")
    
if st.button("lucas banger"):
    st.video("./media/lucasbanger.mp4")
if st.button("lucas clip"):
    st.video("./media/lucasclip.mp4")
        ''',
        language="python",
        line_numbers=True
    )