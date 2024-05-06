import os
import requests

# Your OpenAI API key
YOUR_API_KEY = os.getenv("OPENAI_API_KEY")


# The URL for the OpenAI chat completion API
url = 'https://api.openai.com/v1/chat/completions'

# Headers for the request
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {YOUR_API_KEY}'
}

# Data to be sent in the request
data = {
    "model": "gpt-3.5-turbo-0125",
    "messages": [
        {"role": "user", "content": "Say Hello World"}
    ]
}

# Make the POST request
response = requests.post(url, headers=headers, json=data)

# Check if the request was successful
if response.status_code == 200:
    # Get the completion message from the response
    completion = response.json()['choices'][0]['message']['content']
    print(completion)
else:
    print("Failed to fetch data:", response.status_code, response.text)
