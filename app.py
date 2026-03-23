from flask import Flask, request, jsonify, render_template
from model import get_response
from utils import filter_input, empathy_layer, log_chat

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    filtered = filter_input(user_input)
    if filtered:
        return jsonify({"response": filtered})

    response = get_response(user_input)
    response = empathy_layer(user_input, response)

    log_chat(user_input, response)

    return jsonify({"response": response})

import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "App is running"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
    