import random

# Greeting
name = input(" Hello! What's your name? ")
print(f" Nice to meet you, {name}! I'm your AI chatbot.")

# Chat history list
chat_history = []

# Predefined fun replies
replies = [
    " Interesting! Tell me more.",
    " I see, I see...",
    " That’s a smart thought!",
    " Haha, you're funny!",
    " Hmmm... let me think about that.",
    " I'm just a basic bot, but that sounds deep."
]

while True:
    user_input = input(f"{name}: ")
    if user_input.lower() == 'exit':
        print(" Chat ended. Goodbye!")
        break

    # Save to chat history
    chat_history.append((name, user_input))

    # Choose random response
    bot_reply = random.choice(replies)
    print("AI:", bot_reply)
