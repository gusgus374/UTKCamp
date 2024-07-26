# write code below!
import streamlit as st

import streamlit as st

st.title("Manchesters Blue")

if st.button("lucas goal"):
    st.video("./media/lucasgoal.mp4")

if st.button("lucas banger"):
    st.video("./media/lucasbanger.mp4")
if st.button("lucas clip"):
    st.video("./media/lucasclip.mp4")
st.image("./media/lucas-downey.jpeg",width=200)
st.write("I really enjoyed using the new technology and playing soccer with new people")

with st.expander("Show Lucas's code"):
    st.code(
        body='''
import streamlit as st

st.title("Manchesters Blue")

if st.button("lucas goal"):
    st.video("./media/lucasgoal.mp4")

if st.button("lucas banger"):
    st.video("./media/lucasbanger.mp4")
if st.button("lucas clip"):
    st.video("./media/lucasclip.mp4")
st.image("./media/lucas-downey.jpeg",width=200)
st.write("I really enjoyed using the new technology and playing soccer with new people")
        ''',
        language="python",
        line_numbers=True
    )