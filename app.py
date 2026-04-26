import streamlit as st
import json
import pandas as pd

from jd_parser import parse_jd
from matcher import rank_candidates
from outreach import generate_outreach
from scorer import simulate_reply, compute_interest_score

st.set_page_config(page_title="AI Talent Agent", layout="wide")

st.title("🤖 AI-Powered Talent Scouting & Engagement Agent")

# -------------------------------
# Load Candidates
# -------------------------------
@st.cache_data
def load_candidates():
    with open("candidates.json", "r") as f:
        data = json.load(f)
    return data

candidates = load_candidates()

# -------------------------------
# JD INPUT
# -------------------------------
st.subheader("📝 Enter Job Description")

jd_text = st.text_area("Paste Job Description here", height=200)

if st.button(" Analyze JD"):

    if jd_text.strip() == "":
        st.warning("Please enter a job description")
        st.stop()

    # -------------------------------
    # JD PARSING
    # -------------------------------
    parsed_jd_raw = parse_jd(jd_text)

    try:
        parsed_jd = json.loads(parsed_jd_raw)
    except:
        st.error(" Failed to parse JD properly")
        st.write(parsed_jd_raw)
        st.stop()

    st.subheader(" Parsed Job Description")
    st.json(parsed_jd)

    # -------------------------------
    # MATCHING
    # -------------------------------
    ranked = rank_candidates(candidates, parsed_jd)

    st.subheader(" Top Candidate Matches")

    df_ranked = pd.DataFrame(ranked)
    st.dataframe(df_ranked[["name", "current_role", "match_score", "explanation"]])

    # -------------------------------
    # OUTREACH + REPLIES
    # -------------------------------
    st.subheader(" Outreach & Candidate Responses")

    top_candidates = ranked[:3]
    final_results = []

    for c in top_candidates:

        message = generate_outreach(c, parsed_jd)
        reply, _ = simulate_reply(c)
        interest_score = compute_interest_score(c, parsed_jd)

        final_score = round(0.65 * c["match_score"] + 0.35 * interest_score, 2)

        # -------------------------------
        # RECOMMENDATION LABEL
        # -------------------------------
        if final_score >= 85:
            recommendation = " Strong Shortlist"
        elif final_score >= 70:
            recommendation = " Backup Candidate"
        else:
            recommendation = " Low Priority"

        final_results.append({
            "name": c["name"],
            "match_score": c["match_score"],
            "interest_score": interest_score,
            "final_score": final_score,
            "recommendation": recommendation,
            "explanation": c["explanation"]
        })

        # -------------------------------
        # DISPLAY CHAT
        # -------------------------------
        st.markdown(f"### 👤 {c['name']}")
        st.write("** Message:**")
        st.write(message)

        st.write("** Reply:**")
        st.write(reply)

        st.write(f"** Interest Score:** {interest_score}")
        st.write("---")

    # -------------------------------
    # FINAL RANKING
    # -------------------------------
    st.subheader("🏁 Final Ranked Candidates")

    df_final = pd.DataFrame(final_results)
    df_final = df_final.sort_values(by="final_score", ascending=False)

    # Highlight top candidate
    top_candidate = df_final.iloc[0]
    st.success(f"🏆 Top Candidate: {top_candidate['name']} (Score: {top_candidate['final_score']})")

    # Styled table
    st.dataframe(
        df_final[[
            "name",
            "match_score",
            "interest_score",
            "final_score",
            "recommendation",
            "explanation"
        ]].style.highlight_max(subset=["final_score"], color="lightgreen")
    )

    # -------------------------------
    # CSV EXPORT
    # -------------------------------
    csv = df_final.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Shortlist as CSV",
        data=csv,
        file_name="shortlisted_candidates.csv",
        mime="text/csv"
    )

# -------------------------------
# FULL DATABASE VIEW
# -------------------------------
st.subheader(" Candidate Database")

df = pd.DataFrame(candidates)
st.dataframe(df)