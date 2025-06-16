Here’s a clean and professional **`README.md`** for your Streamlit-based **ResumeRadar** ATS analyzer project:

---

```markdown
# 📄 ResumeRadar – Intelligent ATS Resume Analyzer

**ResumeRadar** is an AI-powered web application that evaluates resumes against job descriptions using **Google Gemini LLMs**. It provides quick resume scans, tailored ATS optimization suggestions, and lets users ask custom questions about their resume.

---

## 🚀 Features

- ✨ **Quick Scan**: Get a compatibility score, resume insights, and profile match.
- 🛠️ **ATS Optimization**: Identify missing keywords, improvements, and personalized suggestions.
- 🤖 **Ask Anything**: Ask custom questions about your resume.

---


## 🛠️ Installation

1. **Clone the Repository**

```bash
git clone https://github.com/akshatt123/Resume-ATS.git
cd resumeradar
```

2. **Create a Virtual Environment**

```bash
conda create -n resumeradar python=3.10
conda activate resumeradar
```

3. **Install Requirements**

```bash
pip install -r requirements.txt
```

4. **Setup Environment Variables**

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_generativeai_key
```

> Get your [Google Generative AI key here](https://makersuite.google.com/app/apikey).

---

## ▶️ How to Use

```bash
streamlit run app.py
```

1. Paste the **Job Description**
2. Upload your **Resume (PDF)**
3. Click:
   - `✨ Quick Scan` → Get resume match score
   - `🛠️ ATS Optimization` → Get suggestions
   - `🔍 Ask` → Ask custom resume-related questions

---



