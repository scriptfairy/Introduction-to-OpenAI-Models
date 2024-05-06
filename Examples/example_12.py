import requests

from openai import OpenAI

client = OpenAI()
response = client.images.edit(
    model="dall-e-2",
    image=open("Son_of_Man_detail_resized.png", "rb"),
    prompt="complete the face of the man in the painting.",
    size="1024x1024",
    n=1,
)

# Extract the image URL from the API response
image_url = response.data[0].url
print("Image URL:", image_url)

# Send a GET request to download the image data
image_data_response = requests.get(image_url)

# Check if the request was successful (status code 200)
if image_data_response.status_code == 200:
    # Specify the local file path where you want to save the image
    # Change the file name and extension as needed
    local_file_path = "son_of_man_processed_v1.png"

    # Write the image data to a local file
    with open(local_file_path, "wb") as file:
        file.write(image_data_response.content)

    print(f"Image saved successfully as '{local_file_path}'")
else:
    print("Failed to download the image. Status code:",
          image_data_response.status_code)
