import streamlit as st

st.set_page_config(
    page_title="AnaytIQ | Data Analyst Interview Practice",
    page_icon="📊",
    layout="wide"
)

# Initialize session state
for key in ["topic", "level", "current_question", "answer", "score", "followup"]:
    if key not in st.session_state:
        st.session_state[key] = None

with st.sidebar:
    st.markdown("## 📊 AnaytIQ")
    st.caption("Live Data Analyst Interview Practice")
    st.divider()
    st.page_link("pages/1_Home.py", label="🏠 Home")
    st.page_link("pages/2_Practice.py", label="🎯 Practice")
    st.page_link("pages/3_Interview.py", label="🎥 Interview")
    st.page_link("pages/4_Feedback.py", label="📊 Feedback")
    st.page_link("pages/5_Question_bank.py", label="📚 Question Bank")


st.title("Welcome to 📊 AnaytIQ")
st.markdown("""
Practice **real Data Analyst interviews** with:
- SQL
- Python
- Power BI

Random questions, auto-scoring & follow-ups — just like a real interview.
""")

if st.button("🚀 Start Practice"):
    st.switch_page("pages/2_Practice.py")
import streamlit as st

st.set_page_config(
    page_title="AnaytIQ | Data Analyst Interview Practice",
    page_icon="📊",
    layout="wide"
)

# Initialize session state
for key in ["topic", "level", "current_question", "answer", "score", "followup"]:
    if key not in st.session_state:
        st.session_state[key] = None

with st.sidebar:
    st.markdown("## 📊 AnaytIQ")
    st.caption("Live Data Analyst Interview Practice")
    st.divider()
    st.page_link("pages/1_Home.py", label="🏠 Home")
    st.page_link("pages/2_Practice.py", label="🎯 Practice")
    st.page_link("pages/3_Interview.py", label="🎥 Interview")
    st.page_link("pages/4_Feedback.py", label="📊 Feedback")
    st.page_link("pages/5_Question_bank.py", label="📚 Question Bank")

st.title("Welcome to 📊 AnaytIQ")
st.markdown("""
Practice **real Data Analyst interviews** with:
- SQL
- Python
- Power BI

Random questions, auto-scoring & follow-ups — just like a real interview.
""")

if st.button("🚀 Start Practice"):
    st.switch_page("pages/2_Practice.py")
