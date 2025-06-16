import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += str(page.extract_text())
    return text

def get_gemini_response(prompt_template, resume_text, job_description):
    model = genai.GenerativeModel('gemini-1.5-flash')
    filled_prompt = prompt_template.format(resume_text=resume_text, jd=job_description)
    response = model.generate_content(filled_prompt)
    return response.text

def ask_question_about_resume(resume_text, user_question):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"""
    You are an AI assistant skilled in resume analysis. Below is a candidate's resume text. 
    Based on this resume, answer the user's question truthfully and concisely.

    Resume: {resume_text}

    User Question: {user_question}
    """
    response = model.generate_content(prompt)
    return response.text
