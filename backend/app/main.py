from fastapi import FastAPI

app = FastAPI(
    title="Matcha AI",
    description="AI-powered Product Engineering Platform",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Matcha AI 🚀"
    }