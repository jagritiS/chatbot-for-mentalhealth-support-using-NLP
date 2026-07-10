import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression

from sklearn.pipeline import Pipeline

from sklearn.metrics import accuracy_score

import joblib



# Load dataset

data = pd.read_csv(
    "../dataset/kaggle/mental_health_combined_test.csv"
)

data = data.dropna(subset=["text", "label"])

print(data.head())



X = data["text"]

y = data["label"]



# Split data

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,
    test_size=0.2,
    random_state=42

)



# TF-IDF + Classifier

model = Pipeline([

    (
    "tfidf",
    TfidfVectorizer(
        stop_words="english"
    )
    ),


    (
    "classifier",
    LogisticRegression(
        max_iter=1000
    )
    )

])



# Train

model.fit(
    X_train,
    y_train
)



# Test

prediction = model.predict(
    X_test
)



accuracy = accuracy_score(
    y_test,
    prediction
)


print(
    "Accuracy:",
    accuracy
)



# Save model

joblib.dump(

    model,

    "../trained_models/mental_health_classifier.pkl"

)


print(
"****************** Model saved : /trained_models/mental_health_classifier.pkl ****************"
)