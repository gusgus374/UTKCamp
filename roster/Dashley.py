# write code below!
import streamlit as st

st.title("What do you want to build today?")

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

with st.expander("Show Dashley's code"):
    st.code(
        body='''
import streamlit as st

st.title("What do you want to build today?")

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
        ''',
        language="python",
        line_numbers=True
    )