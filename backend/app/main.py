from fastapi import FastAPI

app = FastAPI(
    title="AI Support Ticket Analyzer",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "AI Support Ticket Analyzer"
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    }