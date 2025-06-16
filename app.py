import streamlit as st
from model_utils import input_pdf_text, get_gemini_response, ask_question_about_resume

# Prompt Templates
input_prompt1 = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst.cyber security engineer
and big data engineer. Your task is to evaluate the resume based on the given job description.
 
1. Assign the percentage Matching based on Job Descriptipon(JD) 
2. Identify the most suitable profession for this resume.
3. Rate the following aspects out of 10: Impact, Brevity, Style, Structure, Skills.
4. Give an overall ATS score out of 100.

resume:{resume_text}
description:{jd}
"""

input_prompt2 = """
You are an expert ResumeChecker, an expert in ATS optimization.
Analyze the following resume and the job description.You must consider the job market is very competitive. You should provide 
best assistance for improving the resumes and provide optimization suggestions:

1. Identify missing keywords with high accuracy from the job description that should be included in the resume.
2. Suggest 3-5 areas for improvement with specific recommendations.
3. Give an overall ATS  compatibility score out of 100 with a breakdown of the scoring and explain how to improve it.
4. Provide 3-5 bullet points on how to tailor this resume for the specific job description.

resume:{resume_text}
description:{jd}
"""

# Streamlit App UI
st.set_page_config(page_title="ATS Resume Expert", layout="wide")

# Custom CSS
st.markdown("""<style>     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(to right, #e0eafc, #cfdef3);
        color: #1d1d1f;
    }

    .stTextInput > div > div > input, 
    .stTextArea > div > textarea, 
    .stFileUploader > div, 
    .stButton > button {
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-size: 1rem;
    }

    .stButton > button {
        background: linear-gradient(to right, #0071e3, #00b4db);
        color: white;
        font-weight: 400;
        border: none;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 4px 15px rgba(0, 113, 227, 0.3);
    }

    .stButton > button:hover {
        background: linear-gradient(to right, #00b4db, #0071e3);
        transform: scale(1.02);
    }

    .block-container {
        padding: 2rem 2rem 2rem 2rem;
    }

    h1, h2, h3 {
        color: #003366;
        font-weight: 400;
    }

    .section {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
    }

    hr {
        border: none;
        height: 2px;
        background-color: #0071e3;
        margin: 2rem 0;
    }        
    </style>
""", unsafe_allow_html=True)


st.title("📄 ResumeRadar")

jd = st.text_area("📌 Paste the Job Description", height=160, placeholder="Enter the job description here...")
uploaded_file = st.file_uploader("📎 Upload Your Resume (PDF only)", type="pdf", help="Upload your resume in PDF format")

col1, col2 = st.columns(2)
with col1:
    submit1 = st.button("✨ Quick Scan")
with col2:
    submit2 = st.button("🛠️ ATS Optimization")

st.subheader("🤖 Ask Anything About the Resume")
user_question = st.text_input("💬 Ask a question", placeholder="e.g., What are the top skills mentioned?")
ask_btn = st.button("🔍 Ask")

if ask_btn:
    if uploaded_file is not None:
        resume_text = input_pdf_text(uploaded_file)[:10000]
        answer = ask_question_about_resume(resume_text, user_question)
        st.markdown("**🧠 Answer:**")
        st.write(answer)
    else:
        st.warning("Please upload a resume.")

if submit1:
    if uploaded_file is not None:
        resume_text = input_pdf_text(uploaded_file)[:10000]
        response = get_gemini_response(input_prompt1, resume_text, jd)       
        st.subheader("📊 Quick Scan Result")
        st.write(response)
    else:
        st.warning("Please upload a resume.")

elif submit2:
    if uploaded_file is not None:
        resume_text = input_pdf_text(uploaded_file)[:10000]
        response = get_gemini_response(input_prompt2, resume_text, jd)
        st.subheader("⚙️ ATS Optimization Result")
        st.write(response)
    else:
        st.warning("Please upload a resume.")
