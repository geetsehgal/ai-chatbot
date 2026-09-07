from fastapi import APIRouter

from models.schemas import ChatRequest

from services.gemini_service import (
    generate_response
)

router = APIRouter()

@router.post("/chat")

def chat(
    request: ChatRequest
):

    answer = generate_response(
        request.message
    )

    return {
        "answer": answer
    }
