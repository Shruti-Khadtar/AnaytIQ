import streamlit as st

st.title("🎯 Interview Setup")

st.session_state.topic = st.selectbox(
    "Select Topic",
    ["SQL", "Python", "Power BI"]
)

st.session_state.level = st.radio(
    "Difficulty Level",
    ["Beginner", "Intermediate", "Advanced"]
)

if st.button("Start Interview"):
    st.switch_page("pages/3_Interview.py")
