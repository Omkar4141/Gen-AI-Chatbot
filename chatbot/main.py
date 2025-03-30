# main.py
# Import required libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from chatbot import get_ai_response
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Chatbot API",
    description="API to interact with a chatbot using Hugging Face and LangChain",
    version="1.0.0"
)

# Define request body model
class ChatRequest(BaseModel):
    message: str

# Root endpoint to check API status
@app.get("/")
def read_root():
    return {"message": "Welcome to the Chatbot API! Send POST requests to /chat."}

# Endpoint to interact with the chatbot
@app.post("/chat/")
def chat(request: ChatRequest):
    """
    Receives a user message and returns a response from the chatbot.

    Args:
    - request (ChatRequest): A Pydantic model containing the user message.

    Returns:
    - dict: The AI's response.
    """
    try:
        # Get user input from the request
        user_input = request.message

        # Get AI response from the chatbot
        ai_response = get_ai_response(user_input)

        # Return the AI's response
        return {"user": user_input, "ai": ai_response}
    except Exception as e:
        # Handle errors gracefully
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# Run Uvicorn server programmatically
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("API_PORT")), reload=True)

