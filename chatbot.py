def simple_chatbot():
    print("Chatbot: Hello! I am a simple rule-based chatbot.")
    print("Chatbot: You can ask me about my name, the weather, or just say hi.")
    print("Chatbot: Type 'bye' or 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! How can I help you today?")
        
        elif "who are you" in user_input or "name" in user_input:
            print("Chatbot: I am a Python Chatbot created for Task 8.")

        elif "weather" in user_input:
            print("Chatbot: I can't look outside, but it's always sunny in the digital world!")
        
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day.")
            break
            
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you rephrase?")

if __name__ == "__main__":
    simple_chatbot()