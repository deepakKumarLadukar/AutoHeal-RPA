def detect_intent(text: str):
    """
    Detect intent from email subject/text.
    Returns intent + confidence score.
    """

    if not text:
        return {
            "intent": "unknown",
            "confidence": 0.0
        }

    text = text.lower()

    # 🔹 Keyword groups
    report_keywords = ["report", "summary", "analysis", "dashboard"]
    data_keywords = ["update", "excel", "data", "sheet", "modify"]
    alert_keywords = ["urgent", "asap", "immediately", "important"]

    score = {
        "report_bot": 0,
        "data_entry_bot": 0,
        "alert": 0
    }

    # 🔹 Scoring logic
    for word in report_keywords:
        if word in text:
            score["report_bot"] += 1

    for word in data_keywords:
        if word in text:
            score["data_entry_bot"] += 1

    for word in alert_keywords:
        if word in text:
            score["alert"] += 1

    # 🔹 Determine best intent
    best_intent = max(score, key=score.get)
    best_score = score[best_intent]

    # 🔹 Confidence calculation
    total = sum(score.values())

    if total == 0:
        return {
            "intent": "unknown",
            "confidence": 0.5
        }

    confidence = round(best_score / total, 2)

    return {
        "intent": best_intent,
        "confidence": confidence
    }