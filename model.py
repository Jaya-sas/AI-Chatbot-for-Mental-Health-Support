from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from transformers import AutoTokenizer, AutoModel

import os
token = os.getenv("HF_TOKEN")
# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

# Store chat history
chat_history_ids = None

def get_response(user_input):
    global chat_history_ids

    # Encode user input
    new_input_ids = tokenizer.encode(
        user_input + tokenizer.eos_token,
        return_tensors='pt'
    )

    # Append to chat history
    if chat_history_ids is None:
        bot_input_ids = new_input_ids
    else:
        bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1)

    # Generate response
    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=200,                     # shorter & faster
        temperature=0.7,                   # better quality
        top_k=50,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id
    )

    # Decode response
    response = tokenizer.decode(
        chat_history_ids[:, bot_input_ids.shape[-1]:][0],
        skip_special_tokens=True
    )

    # Handle empty or weak responses
    if response.strip() == "":
        return "I'm here for you 💛 Tell me more."

    return response