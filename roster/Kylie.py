# write code below!
import streamlit as st

st.title("hello")

if st.button("snow"):
    st.snow()
    
if st.button('kylies "goal"'):
    st.video("./media/kyliesgoal.mp4")

with st.expander("Show Kylie's code"):
    st.code(
        body='''
import streamlit as st

st.title("hello")

if st.button("snow"):
    st.snow()
    
if st.button('kylies "goal"'):
    st.video("./media/kyliesgoal.mp4")
        ''',
        language="python",
        line_numbers=True
    )