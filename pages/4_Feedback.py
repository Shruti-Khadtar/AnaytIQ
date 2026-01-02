import streamlit as st

st.title("📊 Interview Feedback")

st.subheader("Your Answer")
st.info(st.session_state.answer)

result = st.session_state.score

st.subheader("Score")
st.progress(result["score"])
st.write(f"**Final Score:** {result['score']}%")

st.subheader("✅ Covered Points")
for p in result["matched"]:
    st.success(p)

st.subheader("❌ Missed Points")
for p in result["missed"]:
    st.warning(p)

if st.session_state.followup:
    st.divider()
    st.subheader("🔍 Follow-up Question")
    st.warning(st.session_state.followup)

if st.button("Practice Again"):
    st.switch_page("pages/2_Practice.py")
