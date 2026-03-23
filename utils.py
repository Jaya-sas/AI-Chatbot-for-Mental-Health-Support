import datetime

blocked_words = ["hate"]

def filter_input(user_input):
    for word in blocked_words:
        if word in user_input.lower():
            return "Let's keep the conversation safe and supportive."
    return None

def empathy_layer(user_input, bot_response):
    text = user_input.lower()

    if "sad" in text:
        return "I'm really sorry you're feeling this way. " + bot_response

    elif "stress" in text:
        return "That sounds stressful. I'm here for you. " + bot_response

    elif "alone" in text:
        return "You're not alone. I'm here to listen. " + bot_response

    elif "suicide" in text or "kill myself" in text:
        return "I'm really sorry you're feeling this way. You're not alone. Please consider talking to a trusted person or a professional. You matter 💛"

    return bot_response

def log_chat(user_input, bot_response):
    with open("chat_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} | User: {user_input} | Bot: {bot_response}\n")