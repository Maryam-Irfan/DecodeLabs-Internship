# AI chatbot - DICTIONARY BASED

print("===== AI CHATBOT =====")
print("Type 'bye' to exit.\n")

# Dictionary of responses
responses = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "how are you": "I am functioning properly.",
    "what is your name": "I am a Rule-Based Chatbot.",
    "what can you do": "I can answer predefined questions.",
    "bye": "Goodbye!"
}

while True:

    user_input = input("You: ").lower()

    # Check if input exists in dictionary
    if user_input in responses:

        print("Bot:", responses[user_input])

        # Exit condition
        if user_input == "bye":
            break

    else:
        print("Bot: Sorry, I don't understand.")
