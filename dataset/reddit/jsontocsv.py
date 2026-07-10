import json
import pandas as pd


# Load JSON file
with open("intents 2.json", "r", encoding="utf-8") as file:
    data = json.load(file)


rows = []

# Loop through intents
for intent in data["intents"]:

    patterns = intent["patterns"]
    responses = intent["responses"]

    # Combine every pattern with every response
    for pattern in patterns:
        for response in responses:
            rows.append({
                "question": pattern,
                "response": response
            })


# Create dataframe
df = pd.DataFrame(rows)


# Save CSV
df.to_csv(
    "reddit_chat.csv",
    index=False,
    encoding="utf-8"
)


print("CSV created successfully!")
print(df.head())