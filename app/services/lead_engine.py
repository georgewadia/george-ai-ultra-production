def calculate_lead_score(message: str):

    score = 0

    text = message.lower()

    hot_keywords = [
        "معاينة",
        "رقمي",
        "اتصل",
        "عايز اعمل",
        "ابدأ",
        "ابدء",
        "عايز تصميم",
        "عايز تشطيب"
    ]

    for keyword in hot_keywords:
        if keyword in text:
            score += 25

    if "سعر" in text:
        score += 10

    if "صور" in text:
        score += 15

    return score


def detect_lead_status(score: int):

    if score >= 70:
        return "HOT"

    if score >= 40:
        return "WARM"

    return "COLD"