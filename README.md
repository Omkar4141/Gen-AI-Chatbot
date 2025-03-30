

## 🚀 Chatbot using Hugging Face and LangChain

This project is a **chatbot** that uses Hugging Face's `gemma-2-2b-it` model for text generation, integrated with LangChain. It maintains a conversation history by storing the user and AI responses in a list, allowing for contextual conversations.

---

## 📚 Features

✅ Use Hugging Face's `gemma-2-2b-it` model for text generation.  
✅ Maintains conversation context across multiple interactions.  
✅ Exit the conversation gracefully by pressing `q` or `Q`.  
✅ Easily extendable for more complex conversation flows.  

---

## 🛠️ Requirements

- Python 3.8+
- Hugging Face API key (stored in `.env` file)
- Required Python libraries:
  ```
  pip install langchain-huggingface python-dotenv
  ```

---

## 📦 Installation

1. **Clone the Repository:**
```bash
git clone https://github.com/your-username/chatbot.git
cd chatbot
```

2. **Set Up a Virtual Environment (Optional but Recommended):**
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Linux/Mac
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

3. **Install Required Packages:**
```bash
pip install langchain-huggingface python-dotenv
```

4. **Set Up Environment Variables:**
- Create a `.env` file in the root directory and add your Hugging Face API key:
```
HF_TOKEN=your_huggingface_api_key
```

---

## 📄 Usage

1. **Run the Script:**
```bash
python chatbot.py
```

2. **Chat with the AI:**
```
User: Hello
AI: Hi! How can I assist you today?

User: Tell me a joke
AI: Why don't scientists trust atoms? Because they make up everything!

User: q
Exiting... Goodbye!
```

3. **Exit the Conversation:**
- Press `q` or `Q` to exit the chat.

---

## 📝 Code Overview

### 1. **Import Required Libraries:**
```python
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
```
- `ChatHuggingFace` and `HuggingFaceEndpoint` allow interaction with Hugging Face models.
- `load_dotenv` loads environment variables from the `.env` file.

### 2. **Load Environment Variables:**
```python
load_dotenv()
```
- Loads the Hugging Face API token.

### 3. **Define the Hugging Face Model Endpoint:**
```python
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
```
- `repo_id` specifies the Hugging Face model.
- `task` defines the task (`text-generation`).

### 4. **Create a Chat Model:**
```python
model = ChatHuggingFace(llm=llm)
```

### 5. **Initialize Conversation History:**
```python
conversation_history = []
```
- Stores the conversation context for multi-turn conversations.

### 6. **Main Loop for User Interaction:**
```python
while True:
    user = input("User: ")
    if user.lower() == 'q':
        print("Exiting... Goodbye!")
        break
```
- Takes user input and exits on `q` or `Q`.

### 7. **Pass Conversation History to Maintain Context:**
```python
context = "\n".join(conversation_history + [f"User: {user}"])
response = model.invoke(context)
```
- Passes conversation history with the user's new query.

### 8. **Update and Display AI Response:**
```python
ai_response = response.content
conversation_history.append(f"User: {user}")
conversation_history.append(f"AI: {ai_response}")
print("AI:", ai_response)
```

---

## 🧠 How It Works

1. The model is initialized using `HuggingFaceEndpoint` with the `gemma-2-2b-it` model.
2. The conversation starts, and the user's input is captured.
3. The AI generates a response, and the conversation is stored to maintain context.
4. The conversation history is passed along with the next question to maintain coherence.
5. Press `q` to exit.

---

## 🎯 Future Improvements

- Add error handling for API failures.
- Implement different models with ease.
- Save and load conversation history from a file.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.  

---

## 📄 License

This project is licensed under the MIT License.

---

💡 **Happy Coding!** 😊

---

Let me know if you'd like to make any modifications! 🎉
