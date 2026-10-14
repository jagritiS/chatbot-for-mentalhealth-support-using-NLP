import os
import sys

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)


from models.emotion_model import detect_emotion

from models.chatbot_pipeline import chatbot_response

from models.train_mental_model import prediction


from flask import Flask, request, jsonify
from flask_cors import CORS
from models.mental_health_model import predict_condition
from database.mongodb import save_chat, get_history
from database.mongodb import (
    save_chat,
    get_history
)



app = Flask(__name__)

CORS(app)



@app.route(
    "/chat",
    methods=["POST"]
)

def chat():
    data=request.json
    user_message=data["message"]
    prediction = predict_condition(
        user_message
    )
    emotion = detect_emotion(
        user_message
    )
    result = chatbot_response(
        user_message
    )
    bot_response = (
            "Thank you for sharing. "
            "I detected signs related to "
            +
            prediction["condition"],
    )


    # Save conversation

    save_chat(
        user_message,
        bot_response,
        prediction["condition"],
        prediction["confidence"],
        emotion
    )

    return jsonify({

        "user_message":
            user_message,

        "emotion":
            result["emotion"],

        "condition":
            result["condition"],

        "response":
            result["response"]

    })



@app.route(
    "/history",
    methods=["GET"]
)

def history():


    chats=get_history()


    return jsonify(chats)




@app.route("/health")
def health():

    return jsonify({

        "status":
        "Backend running"

    })



if __name__=="__main__":

    app.run(
        port=5000,
        debug=True
    )