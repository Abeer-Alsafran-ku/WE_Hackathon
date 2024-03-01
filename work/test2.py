from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_cosine_similarity(string, string_list):
    # Combine the input string and the list of strings
    all_strings = [string] + string_list

    # Create TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_strings)

    # Compute cosine similarity between the input string and the list of strings
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    return cosine_similarities

# Example
input_string = "apple banana"
string_list = ["banana orange", "apple mango", "grape pineapple"]

similarities = compute_cosine_similarity(input_string, string_list)

# Print similarity scores
for i, sim in enumerate(similarities):
    print(f"Similarity between '{input_string}' and '{string_list[i]}': {sim}")

