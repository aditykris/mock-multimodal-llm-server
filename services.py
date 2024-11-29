import uuid,time

from fastapi import Request
from fastapi.responses import StreamingResponse

from utils import generate_stream_response
from models import Usage

def chat_completion_service(request : Request):
    '''Function to return mock responses'''
    request_id = f"chatcmpl-{uuid.uuid4().hex[:6]}"

    # Handle streaming response
    if request.stream:
        return StreamingResponse(
            generate_stream_response(request_id),
            media_type="text/event-stream"
        )

    # Check if this is an image analysis request
    is_image_request = False
    if request.messages and isinstance(request.messages[-1].content, list):
        for content in request.messages[-1].content:
            if content.type == "image_url":
                is_image_request = True
                break

    # Check if its an image request
    response_content = (
        "This image shows a wooden boardwalk extending through a lush green marshland."
        if is_image_request
        else "Hello there, how may I assist you today?"
    )

    response = {
        "id": request_id,
        "object": "chat.completion",
        "created": int(time.time()),
        "model": request.model,
        "system_fingerprint": "fp_44709d6fcb",
        "choices": [{
            "index": 0,
            "message": {
                "role": "assistant",
                "content": response_content
            },
            "finish_reason": "stop"
        }],
        "usage": Usage()
    }

    return response
