# write code below!
import streamlit as st

st.title("What do you want to build today?")
if st.button('Left Foot Goal'):
  st.video("./media/LeftFootGoal.mp4")
if st.button('Epic Slide Tackle'):
  st.video("./media/EpicSlideTackle.mp4")
if st.button('Epic Goal'):
  st.video("./media/EpicGoal.mp4")

