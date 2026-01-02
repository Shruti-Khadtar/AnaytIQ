import streamlit as st
import json

st.title("📚 Question Bank")
st.caption("Search and review all Data Analyst interview questions")

# -----------------------------
# Filters
# -----------------------------
topic = st.selectbox("Select Topic", ["SQL", "Python", "Power BI"])

levels = st.multiselect(
    "Select Difficulty",
    ["Beginner", "Intermediate", "Advanced"],
    default=["Beginner", "Intermediate", "Advanced"]
)

search_query = st.text_input(
    "🔍 Search question, concept, or keyword",
    placeholder="e.g. JOIN, window function, pandas, DAX"
)

file_map = {
    "SQL": "data/sql_questions.json",
    "Python": "data/python_questions.json",
    "Power BI": "data/powerbi_questions.json"
}

# -----------------------------
# Load Data
# -----------------------------
with open(file_map[topic]) as f:
    questions = json.load(f)

# -----------------------------
# Filter Logic
# -----------------------------
filtered = []

for q in questions:
    if q["level"] not in levels:
        continue

    searchable_text = (
        q["question"] + " " +
        " ".join(q["expected_points"]) + " " +
        q["model_answer"]
    ).lower()

    if search_query.lower() in searchable_text:
        filtered.append(q)

# -----------------------------
# Results
# -----------------------------
st.write(f"### Showing {len(filtered)} result(s)")

if not filtered:
    st.warning("No questions found. Try a different keyword.")

for q in filtered:
    with st.expander(f"❓ {q['question']} ({q['level']})"):
        st.markdown("**✅ Model Answer**")
        st.success(q["model_answer"])

        st.markdown("**🎯 Key Interview Points**")
        for p in q["expected_points"]:
            st.markdown(f"- {p}")
