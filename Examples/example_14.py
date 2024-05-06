from openai import OpenAI
import json

# Initialize the OpenAI client
client = OpenAI()

# Call the moderation API
response = client.moderations.create(input="I love kittens.")
output = response.results[0]

# Extract relevant data from the output object
categories_data = {
    "harassment": output.categories.harassment,
    "harassment_threatening": output.categories.harassment_threatening,
    "hate": output.categories.hate,
    "hate_threatening": output.categories.hate_threatening,
    "self_harm": output.categories.self_harm,
    "self_harm_instructions": output.categories.self_harm_instructions,
    "self_harm_intent": output.categories.self_harm_intent,
    "sexual": output.categories.sexual,
    "sexual_minors": output.categories.sexual_minors,
    "violence": output.categories.violence,
    "violence_graphic": output.categories.violence_graphic,
    "self_harm_intent": output.categories.self_harm_intent,
    "self_harm_instructions": output.categories.self_harm_instructions,
    "harassment_threatening": output.categories.harassment_threatening
}

category_scores_data = {
    "harassment": output.category_scores.harassment,
    "harassment_threatening": output.category_scores.harassment_threatening,
    "hate": output.category_scores.hate,
    "hate_threatening": output.category_scores.hate_threatening,
    "self_harm": output.category_scores.self_harm,
    "self_harm_instructions": output.category_scores.self_harm_instructions,
    "self_harm_intent": output.category_scores.self_harm_intent,
    "sexual": output.category_scores.sexual,
    "sexual_minors": output.category_scores.sexual_minors,
    "violence": output.category_scores.violence,
    "violence_graphic": output.category_scores.violence_graphic,
    "self_harm_intent": output.category_scores.self_harm_intent,
    "self_harm_instructions": output.category_scores.self_harm_instructions,
    "harassment_threatening": output.category_scores.harassment_threatening
}

# Create a serializable dictionary from extracted data
json_data = {
    "categories": categories_data,
    "category_scores": category_scores_data,
    "flagged": output.flagged
}

# Convert the dictionary to JSON format
json_output = json.dumps(json_data, indent=4)

# Specify the file path to save the JSON output
file_path = "moderation_output.json"

# Save the JSON output to a file
with open(file_path, "w") as json_file:
    json_file.write(json_output)

print(f"JSON output saved to {file_path}")
