

from fastapi import APIRouter, Header

from models import ChatRequest,ImageGenerationRequest
from services import chat_completion_service,image_generation_service

# APIRouter.
router = APIRouter()

@router.post("/v1/chat/completions")
async def chat_completion(
    request: ChatRequest,
    authorization: str = Header(None)
):
    return chat_completion_service(request)

@router.post("/v1/images/generations")
async def image_generations(
    request: ImageGenerationRequest,
    authorization: str = Header(None)
):
    return image_generation_service(request)
