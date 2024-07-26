# write code below!
import streamlit as st

import streamlit as st
st.title("Olivia's app")

if st.button("snow"):
    st.snow()
if st. button("balloons"):
     st.balloons()
     
st.image("https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/soccer-ball-close-up-yamada-taro.jpg" , width=200)
     
st.subheader("click here to see me slide")

if st.button("Olivia slid"):
    st.video("./media/olivia_slid.mp4")
    
if st.button("What did I like at camp?"):
    st.write("I loved making new friends then hanging out with them, and playing competetive soccer games. I also liked learning some coding systems and how to read the data from the trackers. Last but not least I really enjoyed making the app with all of the things that we did!")

with st.expander("Show Olivia's code"):
    st.code(
        body='''
import streamlit as st

import streamlit as st
st.title("Olivia's app")

if st.button("snow"):
    st.snow()
if st. button("balloons"):
     st.balloons()
     
st.image("https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/soccer-ball-close-up-yamada-taro.jpg" , width=200)
     
st.subheader("click here to see me slide")

if st.button("Olivia slid"):
    st.video("./media/olivia_slid.mp4")
    
if st.button("What did I like at camp?"):
    st.write("I loved making new friends then hanging out with them, and playing competetive soccer games. I also liked learning some coding systems and how to read the data from the trackers. Last but not least I really enjoyed making the app with all of the things that we did!")
        ''',
        language="python",
        line_numbers=True
    )