from fastapi import FastAPI
from app.api.router import router

app = FastAPI(
    title="Matcha AI",
    description="AI-powered Product Engineering Platform",
    version="0.1.0"
)

app.include_router(
    router,
    prefix="/api/v1"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to Matcha AI 🚀"
    }