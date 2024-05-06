from openai import OpenAI
client = OpenAI()

file_name = "speech.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Oh, the curious feline, mysterious and sly, Leaping and bounding, oh so spry"
)
response.stream_to_file(file_name)
