# write code below!
import streamlit as st
st.title("Olivia's app")

if st.button("snow"):
    st.snow()
if st. button("balloons"):
     st.balloons()
     
st.subheader("click here to see me slide")

if st.button("Olivia slid"):
    st.video("./media/olivia_slid.mp4")

with st.expander("Show Olivia's code"):
    st.code(
        body='''
import streamlit as st
st.title("Olivia's app")

if st.button("snow"):
    st.snow()
if st. button("balloons"):
     st.balloons()
     
st.subheader("click here to see me slide")

if st.button("Olivia slid"):
    st.video("./media/olivia_slid.mp4")
        ''',
        language="python",
        line_numbers=True
    )