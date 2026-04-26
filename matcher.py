import json

def compute_match_score(candidate, jd):
    score = 0

    # -------- Skills (45 points) --------
    required_skills = jd.get("required_skills", [])
    candidate_skills = candidate.get("skills", [])

    if required_skills:
        matched = len(set(required_skills).intersection(set(candidate_skills)))
        skill_score = (matched / len(required_skills)) * 45
    else:
        skill_score = 0

    # -------- Experience (20 points) --------
    jd_exp = jd.get("min_experience", 0)
    cand_exp = candidate.get("experience_years", 0)

    if cand_exp >= jd_exp:
        exp_score = 20
    else:
        exp_score = (cand_exp / jd_exp) * 20 if jd_exp > 0 else 0

    # -------- Location / Work Mode (15 points) --------
    jd_location = jd.get("location", "").lower()
    cand_location = candidate.get("location", "").lower()

    if jd_location in cand_location or "remote" in jd_location:
        loc_score = 15
    else:
        loc_score = 5

    # -------- Domain (10 points) --------
    jd_domain = jd.get("domain", "").lower()
    cand_domains = [d.lower() for d in candidate.get("domain_experience", [])]

    if jd_domain and any(jd_domain in d for d in cand_domains):
        domain_score = 10
    else:
        domain_score = 5

    # -------- Role Match (10 points) --------
    jd_role = jd.get("job_title", "").lower()
    cand_role = candidate.get("current_role", "").lower()

    if jd_role in cand_role:
        role_score = 10
    else:
        role_score = 5

    score = skill_score + exp_score + loc_score + domain_score + role_score

    return round(score, 2)

def rank_candidates(candidates, jd):
    results = []
  
    for c in candidates:
        score = compute_match_score(c, jd)
        c_copy = c.copy()
        c_copy["match_score"] = score

        c_copy["explanation"] = generate_explanation(c, jd)

        results.append(c_copy)

    results.sort(key=lambda x: x["match_score"], reverse=True)
    return results


def generate_explanation(candidate, jd):
    required_skills = jd.get("required_skills", [])
    candidate_skills = candidate.get("skills", [])

    matched = list(set(required_skills).intersection(set(candidate_skills)))
    missing = list(set(required_skills) - set(candidate_skills))

    explanation = f"Matched skills: {matched}. "

    if missing:
        explanation += f"Missing skills: {missing}."

    return explanation