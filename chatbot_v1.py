# AI chatbot - RULE BASED (IF-ELSE CONDITIONS)

print("===== AI CHATBOT =====")
print("Type 'bye','exit' or 'quit' to exit.\n")


while True:
    # get and print the raw input
    raw_input = input("You: ")

    # clean the input
    clean_input = raw_input.lower().strip()

    #check if user want to exit 
    if clean_input in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    # check the input and respond
    elif clean_input == "hello":
        print("Chatbot: Hello!")
    elif clean_input == "how are you":
        print("Chatbot: I'm fine, thank you!")
    else:
        print("Chatbot: I don't understand")

    







