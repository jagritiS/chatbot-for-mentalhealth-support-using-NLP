import joblib


MODEL_PATH = (
"../trained_models/"
"mental_health_classifier.pkl"
)



model = joblib.load(
    MODEL_PATH
)



def predict_condition(text):


    prediction = model.predict(
        [text]
    )


    probability = (
        model.predict_proba(
            [text]
        )
    )


    confidence = max(
        probability[0]
    )


    return {

        "condition":
        prediction[0],


        "confidence":
        round(
            float(confidence),
            2
        )

    }
