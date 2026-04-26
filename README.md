# 🤖 AI-Powered Talent Scouting & Engagement Agent

## 🚀 Live Demo

🔗 [Deployed Link(click)](https://ai-powered-talent-scouting-agent-mzitqqcnxyvgsm2ztk4smp.streamlit.app/)

---


## 🎥 Demo

Link:


---

## 📌 Overview

Recruiters spend significant time manually reviewing resumes, filtering candidates, and reaching out with uncertain response rates.

This project presents an **AI-powered recruitment agent** that automates the entire pipeline:

* 📄 Job Description Understanding
* 🔍 Candidate Matching
* 📨 Personalized Outreach
* 💬 Simulated Candidate Responses
* 📊 Interest & Fit Scoring
* 🏆 Final Ranked Shortlist

The system helps recruiters move from **raw job descriptions to actionable candidate shortlists** in seconds.

---

## 🎯 Problem Statement

Traditional recruitment workflows are:

* Time-consuming
* Manual and repetitive
* Inefficient in gauging candidate interest
* Lacking explainability in selection

👉 Recruiters need both:

* **Skill fit (Match Score)**
* **Candidate willingness (Interest Score)**

---

## 💡 Solution

This system introduces an **AI-driven agent** that:

1. Parses job descriptions using LLMs
2. Matches candidates using multi-factor scoring
3. Generates personalized recruiter messages
4. Simulates candidate responses
5. Estimates interest level
6. Produces a ranked shortlist with explanations

---

## 🧠 System Architecture

```
Job Description
        ↓
LLM-based JD Parser
        ↓
Candidate Matching Engine
        ↓
Top Candidates
        ↓
Outreach Generator (LLM)
        ↓
Simulated Candidate Replies
        ↓
Interest Scoring
        ↓
Final Ranking System
```

---

## ⚙️ Features

### 🔹 1. Job Description Parsing (LLM)

* Extracts:

  * Role
  * Required skills
  * Experience
  * Location
  * Work mode

---

### 🔹 2. Candidate Matching Engine

Multi-factor scoring based on:

| Factor               | Weight |
| -------------------- | ------ |
| Skills Match         | 45%    |
| Experience           | 20%    |
| Location / Work Mode | 15%    |
| Domain Match         | 10%    |
| Role Alignment       | 10%    |

---

### 🔹 3. Explainable AI Matching

Each candidate includes:

* ✔ Matched skills
* ❌ Missing skills

---

### 🔹 4. Personalized Outreach (LLM)

Generates recruiter messages based on:

* Candidate skills
* Experience
* Job requirements

---

### 🔹 5. Simulated Candidate Responses

* Rule-based behavior simulation
* Based on:

  * Availability
  * Preferences

---

### 🔹 6. Interest Scoring

| Factor             | Weight |
| ------------------ | ------ |
| Availability       | 40%    |
| Response sentiment | 30%    |
| Work mode match    | 15%    |
| Notice period      | 10%    |
| Salary fit         | 5%     |

---

### 🔹 7. Final Ranking System

```
Final Score = 0.65 × Match Score + 0.35 × Interest Score
```

---

### 🔹 8. Recruiter-Friendly Output

* 🏆 Top candidate highlight
* 📊 Ranked shortlist
* 📥 CSV export

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python
* **LLM Integration**: OpenAI API
* **Data Handling**: Pandas
* **Storage**: JSON (candidate database)

---

## 📁 Project Structure

```
AI-Powered-Talent-Scouting-Agent/
│
├── app.py                # Main Streamlit app
├── candidates.json      # Candidate dataset
├── jd_parser.py         # JD parsing using LLM
├── matcher.py           # Candidate matching logic
├── outreach.py          # Message generation
├── scorer.py            # Interest + final scoring
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run Locally

### 1. Clone the repository

```
git clone https://github.com/Harsha-Gogada-009/AI-Powered-Talent-Scouting-Agent.git
cd AI-Powered-Talent-Scouting-Agent
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Set API Key

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

OR set environment variable:

```
export OPENAI_API_KEY=your_api_key
```

---

### 4. Run the app

```
streamlit run app.py
```

---

## 📊 Example Workflow

### Input:

```
We are hiring a Machine Learning Engineer with 2-4 years experience.
Skills: Python, NLP, PyTorch.
Location: Remote India.
```

---

### Output:

* Parsed JD
* Ranked candidates
* Personalized messages
* Simulated replies
* Final shortlist

---

## 🔐 Security & Ethics

* ❌ No sensitive attributes used (gender, race, religion, etc.)
* ✅ Focus only on job-relevant features
* 🔐 API keys handled securely via environment variables

---

## 🚀 Future Improvements

* Resume upload (PDF parsing)
* Vector search (FAISS embeddings)
* Real-time email integration
* Multi-agent orchestration
* Interview question generation
* Recruiter feedback loop

---

## 🏁 Conclusion

This project demonstrates how AI can:

* Reduce recruiter workload
* Improve candidate targeting
* Combine fit + interest for better hiring decisions

---

## 👤 Author

Harsha Vardhan
🔗 https://github.com/Harsha-Gogada-009


