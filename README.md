# Mock Multimodal LLM Server

A mock server designed to serve OpenAI Large Language Model (LLM) APIs, supporting diverse multimodal requests.

## Overview

This server currently supports three types of requests:
1. **Regular Chat Completion**: Handles standard conversational interactions.
2. **Image Analysis Requests**: Processes image-related queries and provides responses based on analysis.
3. **Streaming Responses**: Streams responses that OpenAI streaming responses.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aditykris/mock-multimodal-llm-server.git
   cd mock-multimodal-llm-server
   ```
2. Set up a virtual environment and install dependencies
    ```
    python -m venv venv
    source venv/bin/activate    # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```
3.  Run the server 
    ``` fastapi dev main.py ```
