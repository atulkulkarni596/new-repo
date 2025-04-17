def chatbot():
    print("Hi! I'm a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: That's interesting. Tell me more!")

chatbot()

