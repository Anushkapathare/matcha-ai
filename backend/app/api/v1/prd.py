from fastapi import APIRouter

router = APIRouter()

@router.post("/prd/generate")
def generate_prd():
    return {
        "project_name": "Matcha AI",
        "problem": "Developers waste time creating planning documents manually.",
        "solution": "AI automatically generates Product Requirement Documents.",
        "status": "Dummy Response"
    }