from fastapi import FastAPI

app=FastAPI()

@app.get("/")

def Home():
    return {"Message" : "AutoHeal-RPA Backend Running 🚀"}
