# write code below!
import streamlit as st
import streamlit.components.v1 as components

st.title("What do you want to build today?")

st.image("./media/dashley_profile.png",width=200)


st.write("What I liked about camp was...the soccer part")
st.write("...and watching how we did in the vidoes of us playing soccer!")

st.header("multiplication calculator")
col1, col2 = st.columns(2)

with col1:
    number1 = st.number_input("Enter the first number")
    st.write(number1)
    number2 = st.number_input("Enter the second number")
    st.write(number2)
with col2:
    st.write(f"{number1} * {number2} is {number1 * number2}")
    st.subheader(f"{number1 * number2}")
    
if st.button('Learn to make a video game with AI'):
    components.iframe(src="https://www.youtube.com/embed/335xJHHS-og?si=IPMUzD_w0BSuvTM3", width = 300)

with st.expander("Show Dashley's code"):
    st.code(
        body='''
# write code below!
import streamlit as st
import streamlit.components.v1 as components

st.title("What do you want to build today?")

st.image("./media/dashley_profile.png",width=200)


st.write("What I liked about camp was...the soccer part")
st.write("...and watching how we did in the vidoes of us playing soccer!")

st.header("multiplication calculator")
col1, col2 = st.columns(2)

with col1:
    number1 = st.number_input("Enter the first number")
    st.write(number1)
    number2 = st.number_input("Enter the second number")
    st.write(number2)
with col2:
    st.write(f"{number1} * {number2} is {number1 * number2}")
    st.subheader(f"{number1 * number2}")
    
if st.button('Learn to make a video game with AI'):
    components.iframe(src="https://www.youtube.com/embed/335xJHHS-og?si=IPMUzD_w0BSuvTM3", width = 300)
        ''',
        language="python",
        line_numbers=True
    )