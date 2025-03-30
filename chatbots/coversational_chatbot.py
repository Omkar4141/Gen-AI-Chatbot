# Import necessary classes from LangChain and Hugging Face
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# Import load_dotenv to load environment variables from a .env file
from dotenv import load_dotenv

# Load environment variables from the .env file
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

# Start an infinite loop to take user input and generate responses
while True:
    # Prompt the user for input
    user = input("User: ")
    
    # Check if the user wants to exit by pressing 'q' or 'Q'
    if user.lower() == 'q':
        print("Exiting... Goodbye!")  # Display an exit message
        break  # Exit the loop
    
    # Combine conversation history with the new user input
    context = "\n".join(conversation_history + [f"User: {user}"])
    
    # Invoke the model to generate a response based on the user's input and history
    response = model.invoke(context)
    
    # Get the model's response content
    ai_response = response.content
    
    # Add the user input and AI response to the conversation history
    conversation_history.append(f"User: {user}")
    conversation_history.append(f"AI: {ai_response}")
    
    # Print the AI's response to the user
    print("AI:", ai_response)
