# write code below!
import streamlit as st

st.title("What do you want to build today?")

if st.button('Alex "Nutmeg"'):
    st.video("./media/AlexNutmeg.mp4")
    
if st.button('Alex "skill"'):
    st.video("./media/alexskill.mp4")
    
if st.button('Alex "goalaso"'):
    st.video('./media/Alexgoalaso.mp4')
    
st.divider()
st.header("Division caculator")
co11, co12 = st.columns(2)


with st.expander("Show Alex's code"):
    st.code(
        body='''
import streamlit as st

st.title("What do you want to build today?")

if st.button('Alex "Nutmeg"'):
    st.video("./media/AlexNutmeg.mp4")
    
if st.button('Alex "skill"'):
    st.video("./media/alexskill.mp4")
    
if st.button('Alex "goalaso"'):
    st.video('./media/Alexgoalaso.mp4')
    
st.divider()
st.header("Division caculator")
co11, co12 = st.columns(2)
        ''',
        language="python",
        line_numbers=True
    )