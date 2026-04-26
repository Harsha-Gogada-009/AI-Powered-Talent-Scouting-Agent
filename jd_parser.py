import os
from openai import OpenAI
from dotenv import load_dotenv
import os
from openai import OpenAI
import json
import re

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def parse_jd(jd_text):
    prompt = f"""
    Extract structured information from the following job description.

    Return ONLY valid JSON. No explanation, no extra text.

    Format:
    {{
      "job_title": "",
      "required_skills": [],
      "min_experience": 0,
      "location": "",
      "work_mode": ""
    }}

    Job Description:
    {jd_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    content = response.choices[0].message.content

    # 🔥 Extract JSON using regex
    match = re.search(r"\{.*\}", content, re.DOTALL)
    if match:
        json_str = match.group(0)
        return json_str
    else:
        return content  # fallback