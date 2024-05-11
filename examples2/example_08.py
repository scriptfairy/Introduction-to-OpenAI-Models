from openai import OpenAI
client = OpenAI()
response = client.embeddings.create(
    input="Will have to discard as the package had a hole in it.",
    model="text-embedding-3-small",
    dimensions=10
)
print(response.data[0].embedding)
