import streamlit as st
import pandas as pd
from utils.text_extraction import extract_text_from_image
from utils.text_anonymization import anonymize_text
from utils.resume_parser import extract_candidate_name, parse_resume
from utils.similarity_calculator import compute_similarity
from utils.interview_questions import generate_interview_questions
import pdfplumber

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
