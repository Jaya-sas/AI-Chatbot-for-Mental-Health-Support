AI Chatbot for Mental Health Support

📌 Objective

This project is a simple AI-powered chatbot designed to provide basic emotional support and conversation. It uses natural language processing (NLP) and a conversational model to simulate empathetic responses.

⚠️ Note: This chatbot is not a replacement for professional therapy or medical advice.

🚀 Features
💬 Conversational AI using pretrained transformer models
❤️ Empathetic and supportive responses
🚫 Basic offensive language filtering
🌐 REST API using Flask
🖥️ Simple frontend (HTML/CSS or Streamlit)
📊 Logging of user conversations
☁️ Deployable on Render / Replit
🛠️ Tech Stack
Python
Hugging Face Transformers
Flask (Backend API)
HTML / CSS / Streamlit (Frontend)
Render / Replit (Deployment)
🤖 Model Used

This project uses conversational models such as:

DialoGPT
BlenderBot

These models are fine-tuned for generating human-like dialogue.

📂 Project Structure


ai-mental-health-chatbot/

│
├── app.py                # Flask backend API

├── model/                # Fine-tuned model (optional)

├── templates/            # HTML frontend (if using Flask)

├── static/               # CSS / JS files

├── logs/                 # User chat logs

├── requirements.txt      # Project dependencies

└── README.md             # Project documentation

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/ai-chatbot.git
cd ai-chatbot
2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows
3. Install Dependencies
pip install -r requirements.txt
4. Run the Application
python app.py
🌐 API Endpoints
➤ Chat Endpoint

POST /chat

Request:

{
  "message": "I feel stressed today"
}

Response:

{
  "reply": "I'm here for you. Want to talk about what's making you feel this way?"
}
🧹 NLP Safety Filters
Detects and blocks offensive or harmful inputs
Prevents toxic language generation
Ensures safe and respectful conversations
💡 Example Conversations

User: I feel very sad today
Bot: I'm really sorry you're feeling this way. You're not alone—I'm here for you.

📊 Logging Feature
Stores user messages and bot responses
Helps analyze conversation patterns
Useful for improving model performance
☁️ Deployment

You can deploy this project on:

Render
Replit
Deployment Steps (Render)
Push code to GitHub
Create a new Web Service on Render
Connect your repo

Set:

Start Command: python app.py
📦 Requirements
flask
transformers
torch
📌 Future Improvements
Add voice-based interaction 🎤
Improve emotion detection 😌
Integrate with mental health resources
Add database for persistent chat history
Improve UI/UX design.
