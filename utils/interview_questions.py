import random

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
