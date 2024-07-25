# write code below!
import streamlit as st

tab1, tab2 = st.tabs(["page 1", "page 2"])

with tab1:
    if st.button('minecraft'):
        st.toast("diamond time!", icon='💎')
    st.title ("minecraft" )

with tab2:
    if st.button('oops!'):
        st.video("./media/oops.mp4")
    if st.button('what!'):
        st.video ("./media/005754-highlight.mp4")

with st.expander("Show Carolina's code"):
    st.code(
        body='''
import streamlit as st

tab1, tab2 = st.tabs(["page 1", "page 2"])

with tab1:
    if st.button('minecraft'):
        st.toast("diamond time!", icon='💎')
    st.title ("minecraft" )

with tab2:
    if st.button('oops!'):
        st.video("./media/oops.mp4")
    if st.button('what!'):
        st.video ("./media/005754-highlight.mp4")
        ''',
        language="python",
        line_numbers=True
    )