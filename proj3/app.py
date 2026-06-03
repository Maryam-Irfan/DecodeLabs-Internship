import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==================================================
# STEP 1 : INGESTION
# ==================================================

print("\n========== CAREER RECOMMENDER ==========\n")

user_skills = input(
    "Enter your skills (comma separated): "
)

career_goal = input(
    "Enter your career goal: "
)

user_profile = (
    user_skills.replace(",", " ")
    + " "
    + career_goal
)

print("\nProcessing...\n")


# ==================================================
# LOAD DATASET
# ==================================================

df = pd.read_csv("raw_skills.csv")


# ==================================================
# FEATURE ENGINEERING
# ==================================================

df["combined_features"] = (
    df["skills"].fillna("")
    + " "
    + df["tools"].fillna("")
    + " "
    + df["platforms"].fillna("")
    + " "
    + df["career_path"].fillna("")
)

documents = list(df["combined_features"])

documents.append(user_profile)


# ==================================================
# STEP 2 : SCORING
# TF-IDF VECTORIZATION
# ==================================================

vectorizer = TfidfVectorizer(
    stop_words="english"
)

tfidf_matrix = vectorizer.fit_transform(
    documents
)

job_vectors = tfidf_matrix[:-1]

user_vector = tfidf_matrix[-1]


# ==================================================
# COSINE SIMILARITY
# ==================================================

similarity_scores = cosine_similarity(
    user_vector,
    job_vectors
).flatten()


# ==================================================
# STEP 3 : SORTING
# ==================================================

df["similarity_score"] = similarity_scores

df = df.sort_values(
    by="similarity_score",
    ascending=False
)


# ==================================================
# STEP 4 : FILTERING
# ==================================================

THRESHOLD = 0.10

recommendations = df[
    df["similarity_score"] >= THRESHOLD
]


# ==================================================
# RESULTS
# ==================================================

print("\n=========== TOP RECOMMENDATIONS ===========\n")

if recommendations.empty:
    print(
        "No strong matches found.\n"
        "Try entering more skills."
    )

else:

    for rank, (_, row) in enumerate(
        recommendations.iterrows(),
        start=1
    ):

        print(f"Rank #{rank}")

        print(
            f"Role: {row['job_role']}"
        )

        print(
            f"Career Path: {row['career_path']}"
        )

        print(
            f"Similarity Score: "
            f"{row['similarity_score']:.2f}"
        )

        print(
            f"Recommended Tools: "
            f"{row['tools']}"
        )

        print(
            f"Recommended Platforms: "
            f"{row['platforms']}"
        )

        print("-" * 50)
