from pymongo import MongoClient
from datetime import datetime


# MongoDB Connection

client = MongoClient(
    "mongodb://localhost:27017/"
)


database = client[
    "mental_health_chatbot"
]


chat_collection = database[
    "conversations"
]


def save_chat(
    user_message,
    bot_response,
    condition,
    confidence,
    emotion
):
    document = {
        "user_message":
        user_message,
        "bot_response":
        bot_response,
        "condition":
        condition,
        "condition_confidence":
        confidence,
        "emotion":
        emotion,
        "timestamp":
        datetime.now()

    }
    chat_collection.insert_one(
        document
    )


def get_history():

    chats = chat_collection.find()


    history=[]


    for chat in chats:

        history.append({

            "user":
            chat["user_message"],


            "bot":
            chat["bot_response"]

        })


    return history