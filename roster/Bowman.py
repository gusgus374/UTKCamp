import streamlit as st
my_vidNO = st.file_uploader("upload a video")
if st.button("turn-up-volume"):
    st.video(my_vidNO)
    import streamlit as st
my_vidNO = st.file_uploader("upload a audio")
if st.button("turn-up-volum"):
    st.audio(my_vidNO)

with st.expander("Show Bowman's code"):
    st.code(
        body='''
import streamlit as st
my_vidNO = st.file_uploader("upload a video")
if st.button("turn-up-volume"):
    st.video(my_vidNO)
    import streamlit as st
my_vidNO = st.file_uploader("upload a audio")
if st.button("turn-up-volum"):
    st.audio(my_vidNO)
        ''',
        language="python",
        line_numbers=True
    )