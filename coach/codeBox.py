import streamlit as st

from streamlit_metrics import metric, metric_row
from streamlit_ace import st_ace

import pandas as pd
import numpy as np
import altair as alt
import os
import pathlib


if 'code' not in st.session_state:
     st.session_state['code'] = None
if 'old_code' not in st.session_state:
     st.session_state['old_code'] = None

st.title("footyLab codeBox")
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("**Stuck**? :green[Embrace it], :orange[cuz that's part of it!] You gotta just _**try stuff**_")
    st.write("If you're struggling, try finding examples in other pages. Try making a button.")
    with st.echo():
        if st.button('Taylor "Slipped"'):
            st.video("./media/taylorslipped.mp4")
st.subheader("_Don't forget to save your code!!_")
with st.sidebar:
    file = st.file_uploader("upload python script",type=[".py"])

if st.session_state.old_code is not None:
    if file is not None:
        old_code = file.read()
        decoded_string = old_code.decode("utf-8")
        if st.session_state.old_code != decoded_string:
            st.session_state.old_code = decoded_string
        st.session_state.code = st.session_state.old_code
    else:
        st.session_state.code = st.session_state.old_code

if st.session_state.old_code is None:
    if file is not None:
        old_code = file.read()
        decoded_string = old_code.decode("utf-8")
        st.session_state.old_code = decoded_string
        INITIAL_CODE = st.session_state.old_code
            
    else:
        INITIAL_CODE = """# write code below!
import streamlit as st

st.title("What do you want to build today?")

"""
     


editor = st.container(border=False)
if st.session_state.code is None:
    with editor:
        code = st_ace(
            value=INITIAL_CODE,
            language="python",
            placeholder="st.header('Hello world!')",
            theme="tomorrow_night_eighties",
            show_gutter=True,
            wrap=True,
            show_print_margin=True,
            auto_update=False,
            readonly=False,
            key="ace-editor",
        )
        #st.write("Hit `CTRL+ENTER` to refresh")
if st.session_state.code is not None:
    with editor:
        code = st_ace(
            value=st.session_state.code,
            language="python",
            placeholder="st.header('Hello world!')",
            theme="tomorrow_night_eighties",
            show_gutter=True,
            wrap=True,
            show_print_margin=True,
            auto_update=False,
            readonly=False,
            key="ace-editor",
        )

st.session_state.code = code
st.session_state.old_code = st.session_state.code
        #st.write("*Remember to save your code separately!*")

with st.popover(f"{st.session_state.user}, SAVE YOUR WORK!"):
    file_name = st.text_input("Name your file",f"{st.session_state.user}")
    btn = st.download_button(
                    label="Download Python File",
                    data = code,
                    file_name=f"{file_name}.py"
    )

with st.expander("Expand me to preview your app!",icon=":material/preview:",expanded=True):
    app = st.container(border=False)
    with app:
        exec(st.session_state.code)

