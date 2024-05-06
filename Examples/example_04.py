# Required the Installation of openai library
from openai import OpenAI
client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Substitute with "gpt-4" if using that model
    messages=[
        {"role": "system", "content": "This is the beginning of the chat."},
        {"role": "user", "content": "Hello, how can you assist me today?"},
        {"role": "assistant", "content": "I'm here to help! Please tell me your query."}
    ]
)
print(completion.choices[0].message)
