import streamlit as st
import streamlit.components.v1 as components
st.title("minecraft")
if st.button('minecraft'):
    st.snow()
if st.button('sus'):
    st.balloons()
if st.button('minecraft tnt'):
    components.iframe(src="https://www.youtube.com/embed/k2rDbRUDkds?si=IohUs9Z5FTcTyfBA", width = 300)
if st.button('cowboy steve'):
    components.iframe(src="https://www.youtube.com/embed/xH-pigclAfU?si=AxwzCVVrg5t24hYH", width = 300)
if st.button('cake!'):
    components.iframe(src="https://www.youtube.com/embed/NCMJnTBZfeE?si=EofDbXHAOfyqMe2M", width = 300)
if st.button('hacker'):
    components.iframe(src="https://www.youtube.com/embed/fr7V5ewRU5U?si=RkRnwgx8pWHOf_Zq", width = 300)

with st.expander("Show Gregory's code"):
    st.code(
        body='''
import streamlit as st
import streamlit.components.v1 as components
st.title("minecraft")
if st.button('minecraft'):
    st.snow()
if st.button('sus'):
    st.balloons()
if st.button('minecraft tnt'):
    components.iframe(src="https://www.youtube.com/embed/k2rDbRUDkds?si=IohUs9Z5FTcTyfBA", width = 300)
if st.button('cowboy steve'):
    components.iframe(src="https://www.youtube.com/embed/xH-pigclAfU?si=AxwzCVVrg5t24hYH", width = 300)
if st.button('cake!'):
    components.iframe(src="https://www.youtube.com/embed/NCMJnTBZfeE?si=EofDbXHAOfyqMe2M", width = 300)
if st.button('hacker'):
    components.iframe(src="https://www.youtube.com/embed/fr7V5ewRU5U?si=RkRnwgx8pWHOf_Zq", width = 300)
        ''',
        language="python",
        line_numbers=True
    )