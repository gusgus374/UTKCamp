import streamlit as st

st.title("West Ham")

vid = st.file_uploader("upload pls")

if st.button("Arsenal"):
    #st.video(vid)
    st.video("./media/kadesgoal.mp4")

st.write("I LOVED THIS CAMP BECAUSE I GOT TO PLAY SOCCER WITH GREAT PLAYERS AND LEARN NEW THINGS LIKE CODING.")
st.write("learning about my own stats and getting to compare them, to other peoples stats is really cool.") 
st.image("./media/kade_profile.png",width=300)
with st.expander("Show Kade's code"):
    st.code(
        body='''
import streamlit as st

st.title("West Ham")

vid = st.file_uploader("upload pls")

if st.button("Arsenal"):
    #st.video(vid)
    st.video("./media/kadesgoal.mp4")

st.write("I LOVED THIS CAMP BECAUSE I GOT TO PLAY SOCCER WITH GREAT PLAYERS AND LEARN NEW THINGS LIKE CODING.")
st.write("learning about my own stats and getting to compare them, to other peoples stats is really cool.") 
st.image("./media/kade_profile.png",width=300)
        ''',
        language="python",
        line_numbers=True
    )