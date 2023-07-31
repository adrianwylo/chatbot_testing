import random

class SimpleChatbot:
    def __init__(self):
        self.greetings = ['hello', 'hi', 'hey', 'hola', 'howdy']
        self.goodbyes = ['bye', 'goodbye', 'see you', 'cya']
        self.responses = {
            'what is your name?': 'I am a simple chatbot.',
            'how are you?': 'I am doing well, thank you!',
            'default': "I'm sorry, I don't understand.",
        }

    def generate_response(self, user_input):
        if user_input.lower() in self.greetings:
            return random.choice(self.greetings).capitalize()
        elif user_input.lower() in self.goodbyes:
            return random.choice(self.goodbyes).capitalize()
        else:
            return self.responses.get(user_input.lower(), self.responses['default'])

def main():
    chatbot = SimpleChatbot()
    print("Chatbot: Hello! I'm a simple chatbot. How can I assist you?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day.")
            break

        response = chatbot.generate_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
