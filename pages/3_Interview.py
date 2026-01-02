import streamlit as st
import json, random
from utils.scoring import score_answer
from utils.followup import get_followup

st.title("🎥 Interview")

# Load questions
file_map = {
    "SQL": "data/sql_questions.json",
    "Python": "data/python_questions.json",
    "Power BI": "data/powerbi_questions.json"
}

with open(file_map[st.session_state.topic]) as f:
    questions = json.load(f)

filtered = [q for q in questions if q["level"] == st.session_state.level]
question = random.choice(filtered)

st.session_state.current_question = question

st.subheader("Interview Question")
st.write(question["question"])

answer = st.text_area("Your Answer", height=200)

if st.button("Submit Answer"):
    st.session_state.answer = answer
    result = score_answer(answer, question["expected_points"])
    st.session_state.score = result

    if result["score"] < 70:
        st.session_state.followup = get_followup(
            st.session_state.topic,
            result["missed"]
        )
    else:
        st.session_state.followup = None

    st.switch_page("pages/4_Feedback.py")
