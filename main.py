import logging

from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import router as llm_router

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(llm_router, prefix="", tags=["LLM"])
