# write code below!
import streamlit as st

st.title("Hi im Taylor")


st.image("./media/taylor-howard.jpeg",width=500)
st.write("hi im taylor and in camp this week i liked learning how to code and just practice soccer.Another part that i liked of camp is hanging out with my friends and coach Gustavo Alvarez-Suchini and haaland.")
st.write('The only thing that i didnt like as much was that some days we didnt have a proper feild some days but every day was still super fun.')
vid = st.file_uploader("upload pls")

if st.button("Taylor is better"):
      #st.video(vid)
      st.video("./media/taylorgoal.mp4")
vid = st.file_uploader("so good")
if st.button("Than everyone, just kiddin"):
    #st.video(vid)
    st.video("./media/005313-highlight.mp4")

with st.expander("Show Taylor's code"):
    st.code(
        body='''
# write code below!
import streamlit as st

st.title("Hi im Taylor")


st.image("./media/taylor-howard.jpeg",width=500)
st.write("hi im taylor and in camp this week i liked learning how to code and just practice soccer.Another part that i liked of camp is hanging out with my friends and coach Gustavo Alvarez-Suchini and haaland.")
st.write('The only thing that i didnt like as much was that some days we didnt have a proper feild some days but every day was still super fun.')
vid = st.file_uploader("upload pls")

if st.button("Taylor is better"):
      #st.video(vid)
      st.video("./media/taylorgoal.mp4")
vid = st.file_uploader("so good")
if st.button("Than everyone, just kiddin"):
    #st.video(vid)
    st.video("./media/005313-highlight.mp4")
        ''',
        language="python",
        line_numbers=True
    )