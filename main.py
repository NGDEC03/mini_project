import streamlit as st
import pandas as pd
import random
import pytesseract
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import pdfplumber
from PIL import Image

import spacy
import subprocess
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)

def anonymize_text(text):
    text = re.sub(r'\b(\w+\.\w+@\w+\.\w+)\b', 'email_removed', text)
    text = re.sub(r'\b\d{10}\b', 'phone_removed', text)
    return text

def extract_candidate_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return "Unknown Candidate"

def parse_resume(text):
    doc = nlp(text)
    skills = []
    experience = []
    education = []

    skill_keywords = ["Python", "JavaScript", "Machine Learning", "React", "Django", "SQL", "C++", "Java"]
    for token in doc:
        if token.text in skill_keywords:
            skills.append(token.text)

    experience_pattern = re.compile(r"\b(\d{4})\s*-\s*(\d{4}|Present)\b")
    for match in experience_pattern.finditer(text):
        experience.append(match.group())

    education_keywords = ["B.Tech", "B.E", "MCA", "MBA"]
    for sent in doc.sents:
        if any(edu in sent.text for edu in education_keywords):
            education.append(sent.text)

    return {
        "skills": list(set(skills)),
        "experience": experience,
        "education": education,
    }

def compute_similarity(resume_text, job_description):
    documents = [resume_text, job_description]
    tfidf_vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

def generate_interview_questions(skills):
    questions = []
    num_questions = 5

    for skill in skills:
        questions.append(f"Can you walk me through a project where you effectively utilized {skill}?")
        questions.append(f"What are some common challenges you’ve faced when working with {skill}, and how did you resolve them?")
        questions.append(f"How would you rate your proficiency in {skill}, and how have you improved it over time?")
        questions.append(f"Can you provide an example of using {skill} to solve a complex problem?")
        questions.append(f"How do you stay up-to-date with the latest trends and updates in {skill}?")

    return random.sample(questions, num_questions)

st.title("AI-Based Resume Screening Tool")

uploaded_files = st.file_uploader("Upload Resumes", accept_multiple_files=True, type=["pdf", "png", "jpg", "jpeg"])
job_description = st.text_area("Paste Job Description Here")

if st.button("Analyze Resumes"):
    if uploaded_files and job_description:
        results = []
        for uploaded_file in uploaded_files:
            file_type = uploaded_file.type
            resume_text = ""
            
            try:
                if "image" in file_type:
                    resume_text = extract_text_from_image(uploaded_file)
                elif "pdf" in file_type:
                    with pdfplumber.open(uploaded_file) as pdf:
                        for page in pdf.pages:
                            resume_text += page.extract_text()
                else:
                    st.error("Invalid file format.")
                    continue
                
                if not resume_text.strip():
                    st.error(f"Could not extract text from {uploaded_file.name}.")
                    continue

                resume_text = anonymize_text(resume_text)
                candidate_name = extract_candidate_name(resume_text)
                extracted_info = parse_resume(resume_text)
                similarity_score = compute_similarity(resume_text, job_description)
                interview_questions = generate_interview_questions(extracted_info["skills"])

                result = {
                    "Candidate Name": candidate_name,
                    "Skills": extracted_info["skills"],
                    "Experience": extracted_info["experience"],
                    "Education": extracted_info["education"],
                    "Similarity Score": round(similarity_score * 100, 2),
                    "Interview Questions": interview_questions
                }
                results.append(result)

            except Exception as e:
                st.error(f"Error processing {uploaded_file.name}: {e}")
                continue

        if results:
            st.success("Analysis Complete!")
            df = pd.DataFrame(results).rename(columns={"Candidate Name": "Name"})
            st.dataframe(df)

            for result in results:
                st.subheader(f"Interview Questions for {result['Candidate Name']}")
                for question in result["Interview Questions"]:
                    st.write("- " + question)

    else:
        st.warning("Please upload resumes and provide a job description.")
