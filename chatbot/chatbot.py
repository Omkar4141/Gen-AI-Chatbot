# chatbot.py

# Import necessary classes from LangChain and Hugging Face
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# Import load_dotenv to load environment variables from a ..env file
from dotenv import load_dotenv
import os

# Load environment variables from the ..env file
load_dotenv()

# Create an instance of HuggingFaceEndpoint to interact with the Hugging Face model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",  # Specify the model repository ID
    task="text-generation"           # Define the task as text generation
)

# Create a ChatHuggingFace instance using the Hugging Face endpoint
model = ChatHuggingFace(llm=llm)

# Initialize an empty list to store conversation history
conversation_history = []

def get_ai_response(user_input):
    """
    Generates a response from the AI model based on user input and conversation history.

    Args:
    - user_input (str): The user's message.

    Returns:
    - str: The AI's response.
    """
    global conversation_history

    # Combine conversation history with the new user input
    context = "\n".join(conversation_history + [f"User: {user_input}"])

    # Invoke the model to generate a response based on the context
    response = model.invoke(context)

    # Get the model's response content
    ai_response = response.content

    # Add user input and AI response to the conversation history
    conversation_history.append(f"User: {user_input}")
    conversation_history.append(f"AI: {ai_response}")

    return ai_response

