from fastapi import APIRouter

from app.rag.rag_service import (
    RAGService
)

from app.schemas.ask_request import (
    AskRequest
)

from app.schemas.ask_response import (
    AskResponse
)

router = APIRouter(
    prefix="",
    tags=["AI Assistant"]
)


@router.post(
    "/ask",
    response_model=AskResponse
)
def ask_question(
    request: AskRequest
):

    rag_service = RAGService()

    result = rag_service.ask(
        request.question
    )

    return result