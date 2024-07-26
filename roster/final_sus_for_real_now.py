import streamlit as st
import streamlit.components.v1 as components
st.title("minecraft")

st.header("hi I'm Gregory")

st.image("media/gregory-lloyd.jpeg", width=200)

st.write("I love the work that these youtubers make. tks to the youtubers that made those videos possible")

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
if st.button('diamonds!'):
    components.iframe(src="https://www.youtube.com/embed/IBGKLDUe2rk?si=9jQyPwBq51R0j4iB", width = 300)
if st.button('dragons!'):
    components.iframe(src="https://www.youtube.com/embed/5kwsoQcgYNE?si=5GNyz_WdwogCvV2C", width = 300)
