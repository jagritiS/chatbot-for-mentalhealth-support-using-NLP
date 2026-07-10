import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()


client = InferenceClient(
    provider="hf-inference",
    api_key=os.environ["HF_TOKEN"]
)


MODEL_NAME = "SamLowe/roberta-base-go_emotions"



def detect_emotion(text):

    result = client.text_classification(
        text,
        model=MODEL_NAME
    )
    emotions = {}
    for item in result:

        emotions[item.label] = round(
            item.score,
            3
        )
    return emotions