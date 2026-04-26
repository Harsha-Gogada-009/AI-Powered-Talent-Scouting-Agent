def simulate_reply(candidate):
    availability = candidate.get("availability", "").lower()

    if "open" in availability:
        reply = "This sounds interesting, I'd love to learn more about the role."
        base_score = 85

    elif "passive" in availability:
        reply = "I'm not actively looking, but open if the role is a strong fit."
        base_score = 60

    else:
        reply = "Thanks for reaching out, but I'm not exploring opportunities right now."
        base_score = 30

    return reply, base_score


def compute_interest_score(candidate, jd):
    score = 0

    # -------- Availability (40) --------
    availability = candidate.get("availability", "").lower()
    if "open" in availability:
        score += 40
    elif "passive" in availability:
        score += 25
    else:
        score += 10

    # -------- Work Mode Match (15) --------
    jd_mode = jd.get("work_mode", "").lower()
    cand_mode = candidate.get("preferred_work_mode", "").lower()

    if jd_mode and jd_mode in cand_mode:
        score += 15
    else:
        score += 5

    # -------- Notice Period (10) --------
    notice = candidate.get("notice_period_days", 90)
    if notice <= 30:
        score += 10
    elif notice <= 60:
        score += 5
    else:
        score += 2

    # -------- Salary Fit (5) --------
    score += 5  # keep simple for now

    # -------- Reply Sentiment (30) --------
    _, base_score = simulate_reply(candidate)
    score += (base_score / 100) * 30

    return round(score, 2)