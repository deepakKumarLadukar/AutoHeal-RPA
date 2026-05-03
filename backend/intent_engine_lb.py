import os
from openai import OpenAI
from dotenv import load_dotenv

# Load secret keys from the .env files and store it into client variables 
load_dotenv()
client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def detect_intent(text: str):
    """
    AI-based intent detection using LLM
    """
    if not text:
        return{"intent": "unknown", "confidence": 0.0}
    
    prompt=f"""
    You are an AI assistant for email automation.

    classify the intent of this email into one of the following
    - report_bot
    - data_entry_bot
    - alert
    - unknown

    Also provide a confidence score between o and 1.

    email:
    {text}

    output strictly in JSON:
    {{
    "intent": "...",
    "Confidence": ...
    }}
    """
    try:
        response=client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        result_text=response.choices[0].message.content

        # Convert string → dict safely
        import json
        return json.loads(result_text)
    
    except Exception as e:
        return{
            "intent": "error",
            "confidence": 0.0,
            "message": str(e)
        }
