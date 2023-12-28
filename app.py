import streamlit as st

import time as t

st.title("Hello")

st.header("Python Developers")

st.subheader("Search content")

st.info("Get the name")

st.warning("put the id ")

st.error("Wrong password")

st.success("win")

st.markdown("## Aswin")
st.markdown("##### Aswin")
st.markdown(":moon:")

st.write("employee")

st.checkbox("login")

st.button("click")

st.radio("pick the gender",["male","female"])

st.selectbox("pick the course",["java","python"])

with st.spinner("just wait"):
    t.sleep(2)

st.balloons()

st.snow()