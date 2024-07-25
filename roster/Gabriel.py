# write code below!
import streamlit as st

st.title("What do you want to build today?")

st.header("addition calculator")
co11,co12 = st.columns(2)

with co11:
    number1 = st.number_input("Enter the first number")  
    st.write(number1)
    number2 =st.number_input("Enter thes second number")
    st. write(number2)
with co12:
    st.write(f"{number1} + {number2} is {number1 + number2}")
    st.subheader(f"{number1 + number2}")




