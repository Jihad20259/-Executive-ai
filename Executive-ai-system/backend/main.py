from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Executive AI System is running"}
