from fastapi import FastAPI
from backend.email_reader import get_emails
from backend.intent_engine_lb import detect_intent
from backend.decision_engine import decide_action

app=FastAPI()

@app.get("/")

def Home():
    return {"Message" : "AutoHeal-RPA Backend Running 🚀"}

# Health check route (For debugging process)
@app.get("/health")
def health():
    return {"status": "OK"}

# Fetch emails from Gmail
@app.get("/emails")

def read_emails():
    try:
        emails=get_emails()
        return{
            "status": "Success",
            "count": len(emails),
            "data": emails
        }
    except Exception as e:
        return{
            "status": "error",
            "message":str(e)
        }

# Process Emails (AI Intent Engine)
@app.get("/process-emails")
def process_emails():
    try:
        emails=get_emails()
        results=[]

        for email in emails:
            subject=email.get("subject", "")

            # AI Intent Detection
            intent_data=detect_intent(subject)
            action = decide_action(intent_data)

            results.append({
                "subject": subject,
                "intent": intent_data.get("intent"),
                "confidence": intent_data.get("confidence"),
                "action": action
            })

        return{
            "status": "processed",
            "count": len(results),
            "data": results
        }
    
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
    
# Future Ready Endpoint (UiPath Trigger Placeholder)

@app.post("/trigger-bot")
def trigger_bot(intent: str):
    """
    This will trigger UiPath bots based on detected intent.
    """

    mapping = {
        "report_bot": "ReportBot.xaml",
        "data_entry_bot": "DataEntryBot.xaml",
        "alert": "AlertHandler.xaml"
    }

    bot = mapping.get(intent, "UnknownBot")

    return {
        "status": "triggered",
        "intent": intent,
        "bot": bot,
        "message": f"{bot} will be triggered (UiPath integration pending)"
    }

