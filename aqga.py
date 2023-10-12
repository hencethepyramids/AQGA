import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample questions and explanations
questions = [
    "What is a variable in programming?",
    "How do you define a function in Python?",
    "Explain the concept of a for loop.",
]
explanations = [
    "A variable is a container for storing data in a program.",
    "In Python, you can define a function using the 'def' keyword.",
    "A for loop is used to iterate over a sequence of items."
]

# Initialize spaCy
nlp = spacy.load("en_core_web_sm")

# Vectorize the explanations
tfidf_vectorizer = TfidfVectorizer()
explanation_vectors = tfidf_vectorizer.fit_transform(explanations)

# Process the user's input
user_input = "What is a variable in coding?"
user_input = nlp(user_input)

# Vectorize the user's input
user_input_vector = tfidf_vectorizer.transform([user_input.text])

# Calculate cosine similarity
similarities = cosine_similarity(user_input_vector, explanation_vectors)

# Find the most similar explanation
most_similar_idx = similarities.argmax()

# Display the explanation
print("User's Question:", user_input.text)
print("Explanation:", explanations[most_similar_idx])
