import streamlit as st

st.title("📊 DataMock")
st.subheader("Live Mock Interviews for Data Analysts")

st.markdown("""
**DataMock** helps you prepare for real interviews using:
- Real interview questions
- Randomized difficulty
- Automatic evaluation
- Follow-up probing
""")

if st.button("Start Interview Practice"):
    st.switch_page("pages/2_Practice.py")
