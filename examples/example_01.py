
# Example 1: Simple chat completion request

# uses the Chat Completion API of OpenAI, engaging the gpt-3.5-turbo-0125
# model to translate an English sentence into Arabic, with a response limited to 60 tokens

# Requirements:
# - An OpenAI API key stored as environment variable
# - Python installed on your computer
# - Installation of requests library

import os
import requests

YOUR_API_KEY = os.getenv("OPENAI_API_KEY")

# Define the API endpoint URL for chat completions
chat_engine_url = "https://api.openai.com/v1/chat/completions"

# Set request headers (include your API key for authentication)
headers = {
    "Authorization": f"Bearer {YOUR_API_KEY}",
    "Content-Type": "application/json"
}

# Define the data payload with the prompt and other parameters
data = {
    "model": "gpt-3.5-turbo-0125",
    "messages": [
        {"role": "user", "content": "Translate the following English text to Arabic: 'Hello, how are you?'"}
    ],
    "max_tokens": 60
}

response = requests.post(chat_engine_url, headers=headers, json=data)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")
