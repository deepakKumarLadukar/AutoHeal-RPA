from fastapi import FastAPI
from backend.email_reader import get_emails

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