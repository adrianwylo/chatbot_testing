import os
import openai

openai.api_type = "azure"
openai.api_base = "https://test-ai-insurance.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = os.getenv("8a55f4d848e841cba22354e78789ada4")

class SimpleChatbot:
    def __init__(self):
        self.messages = [
            {"role": "system", "content": "You are an AI assistant that helps people find information."}
        ]

    def generate_response(self, user_input):
        self.messages.append({"role": "user", "content": user_input.lower()})
        response = openai.ChatCompletion.create(
            engine="text-davinci-002",  # Use an appropriate engine here.
            messages=self.messages,
            temperature=0.7,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
        self.messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
        return response["choices"][0]["message"]["content"]

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
