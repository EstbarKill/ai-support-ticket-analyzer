from fastapi import FastAPI

from app.database.init_db import init_db

from app.api.ticket_routes import router as ticket_router
from app.api.dashboard_routes import router as dashboard_router
from app.api.ask_routes import router as ask_routes

app = FastAPI(
    title="AI Support Ticket Analyzer",
    version="1.0.0"
)

@app.on_event("startup")
def startup():
    init_db()


app.include_router(
    ticket_router
)

app.include_router(
    dashboard_router
)
app.include_router(
    ask_routes
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