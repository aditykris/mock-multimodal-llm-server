import time,json,asyncio

async def generate_stream_response(request_id: str):
    '''Simulate streaming response chunks'''
    chunks = [
        {"role": "assistant", "content": ""},
        {"content": "Hello"},
        {"content": " there"},
        {"content": ", how"},
        {"content": " can"},
        {"content": " I"},
        {"content": " help"},
        {"content": " you"},
        {"content": " today"},
        {"content": "?"},
    ]

    # First chunk with role
    response = {
        "id": request_id,
        "object": "chat.completion.chunk",
        "created": int(time.time()),
        "model": "gpt-4o-mini",
        "system_fingerprint": "fp_44709d6fcb",
        "choices": [{
            "index": 0,
            "delta": chunks[0],
            "logprobs": None,
            "finish_reason": None
        }]
    }
    yield f"data: {json.dumps(response)}\n\n"
    await asyncio.sleep(0.1)

    # Content chunks
    for chunk in chunks[1:-1]:
        response["choices"][0]["delta"] = chunk
        yield f"data: {json.dumps(response)}\n\n"
        await asyncio.sleep(0.1)

    # Final chunk
    response["choices"][0]["delta"] = {}
    response["choices"][0]["finish_reason"] = "stop"
    yield f"data: {json.dumps(response)}\n\n"
    yield "data: [DONE]\n\n"
