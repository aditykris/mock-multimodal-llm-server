import uuid,time

from fastapi import Request,HTTPException
from fastapi.responses import StreamingResponse

from utils import generate_stream_response
from models import Usage,ImageGenerationResponse

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


def image_generation_service(request: Request):
    '''Function to return image urls'''
    n = request.n or 1
    if n < 1 or n > 10:
        raise HTTPException(status_code=400, detail="Number of images must be between 1 and 10")

    # Generate mock image URLs
    image_urls = [
        {"url": f"https://example.com/generated-image-{i+1}.jpg"}
        for i in range(n)
    ]

    response = ImageGenerationResponse(
        created=int(time.time()),
        data=image_urls
    )

    return response
