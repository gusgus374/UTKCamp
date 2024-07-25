# write code below!
import streamlit as st


st.title("taylor is better than everyone")

vid = st.file_uploader("upload pls")

if st.button("Taylor is better"):
      #st.video(vid)
      st.video("./media/taylorgoal.mp4")
vid = st.file_uploader("so good")
if st.button("Than everyone"):
    #st.video(vid)
    st.video("./media/005313-highlight.mp4")

with st.expander("Show Taylor's code"):
    st.code(
        body='''
import streamlit as st


st.title("taylor is better than everyone")

vid = st.file_uploader("upload pls")

if st.button("Taylor is better"):
      #st.video(vid)
      st.video("./media/taylorgoal.mp4")
vid = st.file_uploader("so good")
if st.button("Than everyone"):
    #st.video(vid)
    st.video("./media/005313-highlight.mp4")
        ''',
        language="python",
        line_numbers=True
    )