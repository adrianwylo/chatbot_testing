import os
import openai

openai.api_base = "https://test-ai-insurance.openai.azure.com/"
openai.api_key = "81b41771820741638eac156eb53bb053"
openai.api_type = "azure"
openai.api_version = "2023-03-15-preview"

deployment_name = 'CustomDataBotTest'  # This will correspond to the custom name you chose for your deployment when you deployed a model.


class SimpleChatbot:
    def __init__(self):
        self.messages = [
            {"role": "system", "content": "You are an AI assistant that helps people find information."}
        ]

    def generate_response(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        print("Next response processing")

        response = openai.ChatCompletion.create(
            engine="CustomDataBotTest",
            messages=self.messages,
            temperature=0.7,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
        self.messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
        print("Response Tokens:", response["choices"][0]["message"]["content"])  # Print the token count of the response
        return response["choices"][0]["message"]["content"]

    def display_messages(self):
        print(self.messages)


def main():
    chatbot = SimpleChatbot()
    print("Chatbot: Hello! I'm a simple chatbot. How can I assist you?")
    
    for _ in range(10):  # Change the maximum number of iterations as needed
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day.")
            break
        response = chatbot.generate_response(user_input)
        print("Chatbot:", response)
        chatbot.display_messages()
    print("Chatbot: Goodbye! Have a great day. bit.")

if __name__ == "__main__":
    main()
