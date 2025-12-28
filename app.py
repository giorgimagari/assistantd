import streamlit as st

st.set_page_config(page_title="Study Assistant", layout="centered")
st.title("📚 Study Assistant")
st.write("⏳ Models will load only when you click a button, so the page opens instantly.")

from agent import run_agent, summarize, translate, study_plan, calculate

st.markdown("""
- Summarize text  
- Translate text  
- Create study plans  
- Solve math expressions  
- Generate general text  
""")

user_input = st.text_area("Enter your text here:", height=200)

col1, col2, col3, col4, col5 = st.columns(5)

if col1.button("Summarize"):
    if user_input.strip():
        with st.spinner("Summarizing..."):
            st.write(summarize(user_input))

if col2.button("Translate"):
    if user_input.strip():
        with st.spinner("Translating..."):
            st.write(translate(user_input))

if col3.button("Study Plan"):
    if user_input.strip():
        with st.spinner("Creating study plan..."):
            st.write(study_plan(user_input))

if col4.button("Calculate"):
    if user_input.strip():
        with st.spinner("Calculating..."):
            st.write(calculate(user_input))

if col5.button("Generate Text"):
    if user_input.strip():
        with st.spinner("Generating text..."):
            st.write(run_agent(user_input))

