from models.emotion_model import detect_emotion

from models.mental_health_model import predict_condition

from models.response_generator import generate_response



def chatbot_response(message):


    # 1. Detect emotion

    emotion = detect_emotion(
        message
    )



    # 2. Detect mental condition

    condition = predict_condition(
        message
    )



    # 3. Generate reply

    response = generate_response(
        message
    )



    return {


        "emotion":
        emotion,


        "condition":
        condition,


        "response":
        response

    }