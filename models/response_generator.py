import os
import pandas as pd

from sentence_transformers import SentenceTransformer

from sklearn.metrics.pairwise import cosine_similarity

import numpy as np

# Get current file directory

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


# Dataset path

CSV_PATH = os.path.join(
    BASE_DIR,
    "..",
    "dataset",
    "reddit",
    "reddit_chat.csv"
)



# Load dataset

data = pd.read_csv(
    CSV_PATH
)



print("Dataset loaded")
print(data.head())
print("Columns:", data.columns)
print("Rows before cleaning:", len(data))



# Remove empty values

data = data.dropna(
    subset=[
        "question",
        "response"
    ]
)



print("Rows after cleaning:", len(data))



# Check dataset

if len(data) == 0:
    raise ValueError(
        "Dataset is empty after cleaning. Check reddit_chat.csv"
    )



questions = data["question"].astype(str).tolist()

responses = data["response"].astype(str).tolist()



print("Questions loaded:", len(questions))
print("Responses loaded:", len(responses))



# Load embedding model

encoder = SentenceTransformer(
    "all-MiniLM-L6-v2"
)



# Create question embeddings

question_embeddings = encoder.encode(
    questions
)



print(
    "Embeddings created:",
    question_embeddings.shape
)


def generate_response(user_text):
    print("Generating response...", user_text)

    # 1. Ensure the text isn't empty or just spaces
    if not user_text or str(user_text).strip() == "":
        return "I'm here to listen. Can you tell me more about how you feel?"

    # 2. Generate the user embedding
    user_embedding = encoder.encode([user_text])

    # 3. Convert to safe float32 arrays to prevent Python 3.13 macOS matmul warnings
    A = np.asarray(user_embedding, dtype=np.float32)
    B = np.asarray(question_embeddings, dtype=np.float32)

    # 4. Calculate cosine similarity safely using numpy
    # This avoids the buggy sklearn matmul path on macOS
    dot_product = np.dot(A, B.T)[0]
    norm_A = np.linalg.norm(A)
    norm_B = np.linalg.norm(B, axis=1)

    # Prevent divide by zero if a norm happens to be 0
    if norm_A == 0 or np.any(norm_B == 0):
        return "I'm here to listen. Can you tell me more about how you feel?"

    similarity = dot_product / (norm_A * norm_B)

    # 5. Find the best match
    best_match = similarity.argmax()
    score = similarity[best_match]

    print("Similarity score:", score)

    # If the match is poor, use the fallback response
    if score < 0.40:
        return "I'm here to listen. Can you tell me more about how you feel?"

    return responses[best_match]
'''
def generate_response(user_text):


    print(
        "Generating response...",
        user_text
    )


    user_embedding = encoder.encode(
        [user_text]
    )


    similarity = cosine_similarity(

        user_embedding,

        question_embeddings

    )[0]


    best_match = similarity.argmax()


    score = similarity[best_match]



    print(
        "Similarity score:",
        score
    )



    if score < 0.40:

        return (
            "I'm here to listen. "
            "Can you tell me more about how you feel?"
        )


    return responses[best_match]
    
    '''