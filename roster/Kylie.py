import streamlit as st

st.title("hello")

if st.button("snow"):
    st.snow()

if st.button('kylies "goal"'):
    st.video("./media/kyliesgoal.mp4")
    
if st.button("what i've enjoyend at camp this week"):
    st.write("This week at camp i've enjoyed playing soccer and learing some of the coding.")
with st.expander("Show Kylie's code"):
    st.code(
        body='''
import streamlit as st

st.title("hello")

if st.button("snow"):
    st.snow()

if st.button('kylies "goal"'):
    st.video("./media/kyliesgoal.mp4")
    
if st.button("what i've enjoyend at camp this week"):
    st.write("This week at camp i've enjoyed playing soccer and learing some of the coding.")
        ''',
        language="python",
        line_numbers=True
    )