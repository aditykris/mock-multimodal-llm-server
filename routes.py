
from typing import Annotated

from fastapi import APIRouter, Request, Header, UploadFile, File

from models import ChatRequest
from services import chat_completion_service
# APIRouter.
router = APIRouter()

@router.post("/v1/chat/completions")
async def chat_completion(
    request: ChatRequest,
    authorization: str = Header(None)
):
    return chat_completion_service(request)
