import random
#these are my chatbot greetings
name = input(" Hello! What's your name? ")
print(f" Nice to meet you, {name}! I'm your AI chatbot.")

#these is the chat history list
chat_history = []
#these are the fun replies
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

    #  These are the chat history of the user
    chat_history.append((name, user_input))

    #AND HERE THE CHAT BOT  Chooses random response
    bot_reply = random.choice(replies)
    print("AI:", bot_reply)
