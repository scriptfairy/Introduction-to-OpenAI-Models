import json
from openai import OpenAI

client = OpenAI()

# Function to load reviews from a JSON file


def load_reviews(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Function to save embeddings to a JSON file


def save_embeddings(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Function to get embeddings for all reviews in a batch


def get_embeddings(reviews):
    # Prepare a list of texts for embedding
    texts = [review['review'] for review in reviews]
    # Send a single API request for all texts
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts,
        dimensions=10
    )
    print(response)
    print("\n\n")
    # Combine the original reviews with their embeddings
    embeddings = []
    for i, review in enumerate(reviews):
        embedding_vector = response.data[i].embedding
        embeddings.append({
            "score": review['score'],
            "review": review['review'],
            # Assume embeddings are returned in order
            "embedding": embedding_vector
        })
    return embeddings

# Main execution function


def main():
    reviews = load_reviews('review.json')
    embeddings = get_embeddings(reviews)
    save_embeddings(embeddings, 'embeddings.json')
    print("---------- DONE ------------")


if __name__ == '__main__':
    main()
