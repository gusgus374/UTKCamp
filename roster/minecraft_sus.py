import streamlit as st
st.title("minecraft")
if st.button('minecraft'):
    st.snow()
if st.button('sus'):
    st.balloons()

with st.expander("Show Gregory's code"):
    st.code(
        body='''
import streamlit as st
st.title("minecraft")
if st.button('minecraft'):
    st.snow()
if st.button('sus'):
    st.balloons()
        ''',
        language="python",
        line_numbers=True
    )