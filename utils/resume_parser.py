import spacy
import re

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

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
