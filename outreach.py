from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_outreach(candidate, jd):
    prompt = f"""
    You are a recruiter reaching out to a candidate.

    Candidate:
    Name: {candidate['name']}
    Role: {candidate['current_role']}
    Skills: {candidate['skills']}
    Experience: {candidate['experience_years']} years

    Job:
    Role: {jd.get('job_title')}
    Skills: {jd.get('required_skills')}
    Experience: {jd.get('min_experience')}+

    Write a short personalized message (3-4 lines max):
    - Mention 2 relevant skills from candidate
    - Mention the job role
    - Keep it friendly
    - End with a question about interest
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content