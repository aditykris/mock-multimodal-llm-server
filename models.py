'''Models used in responses'''

from typing import List,Optional,Union

from pydantic import BaseModel

from constants import MESSAGE

class TextContent(BaseModel):
    type: str
    text: str

class ImageUrl(BaseModel):
    url: str

class ImageUrlContent(BaseModel):
    type: str
    image_url: ImageUrl

class Message(BaseModel):
    role: str
    content: Union[str, List[Union[TextContent, ImageUrlContent]]]

class ChatRequest(BaseModel):
    model: str
    messages: List[Message]
    stream: Optional[bool] = False
    max_tokens: Optional[int] = None

class Choice(BaseModel):
    index: int
    message: Optional[str] = None
    delta: str = "DELTA"
    logprobs: Optional[None] = None
    finish_reason: Optional[str] = None

class CompletionTokensDetails(BaseModel):
    reasoning_tokens: int = 0
    accepted_prediction_tokens: int = 0
    rejected_prediction_tokens: int = 0

class Usage(BaseModel):
    prompt_tokens: int = 9
    completion_tokens: int = 12
    total_tokens: int = 21
    completion_tokens_details: CompletionTokensDetails = CompletionTokensDetails()

class ChatResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    system_fingerprint: str
    choices: List[Choice]
    usage: Usage

class ImageGenerationRequest(BaseModel):
    model: str
    prompt: str
    n: Optional[int] = 1
    size: Optional[str]

class ImageGenerationResponse(BaseModel):
    created: int
    data: List[ImageUrl]