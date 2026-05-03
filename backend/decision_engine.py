def decide_action(intent_data):
    """
    Decide what action to take based on intent + confidence
    """

    intent = intent_data.get("intent")
    confidence = intent_data.get("confidence", 0)

    # 🟢 High confidence → trigger automation
    if intent != "unknown" and confidence > 0.7:
        return "trigger_bot"

    # 🟡 Medium confidence → human review
    elif confidence > 0.5:
        return "needs_review"

    # 🔴 Low confidence → ignore
    else:
        return "ignore"