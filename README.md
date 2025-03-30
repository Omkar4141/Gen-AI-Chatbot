
# Chatbot API with FastAPI and Hugging Face

This is a simple chatbot API built using **FastAPI** and **Hugging Face** models, leveraging **LangChain** to generate responses.

## 🚀 Features
- Chat endpoint to interact with the AI.
- Uvicorn server runs automatically when `main.py` is executed.
- Conversation history is maintained during the session.

## 📚 Requirements
- Python 3.8+
- API key from Hugging Face (set in `.env` file).

## 🔧 Setup
1. **Clone the Repository:**
```bash
git clone <repository-url>
cd <project-directory>
```

2. **Set Environment Variables:**
- Create a `.env` file with the following content:
```
HF_TOKEN=your_huggingface_api_key
API_PORT=<mention_port_for_api>
```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

## ▶️ Running the Application
Run the application using:
```bash
python main.py
```

## 🌐 API Endpoints
- **GET /** – Check API status.
- **POST /chat/** – Send a message to the chatbot.

## 🧪 Testing
You can test the API using:
- **cURL**
- **Postman**

## 🎯 Future Improvements
- Add authentication.
- Implement session-based conversation history.
- Save conversation data to a database.

---

Let me know if you need further modifications! 😊🚀
