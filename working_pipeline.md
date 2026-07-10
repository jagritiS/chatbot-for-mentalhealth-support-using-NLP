python3 -m venv .venv 
. .venv/bin/activate
 pip install flask
 pip freeze > requirements.txt 
 brew tap mongodb/brew
brew install mongodb-community
 brew trust mongodb/brew
 brew install mongodb-community
  mongosh --> for mongo shell


test> show dbs

test> use mental_health_chatbot
mental_health_chatbot> db.conversations.find()
[
  {
    _id: ObjectId('6a4e1e30bd668d870c49dae7'),
    user_message: 'i feel very much stressed today',
    bot_response: 'Hello, I am your mental health assistant.',
    timestamp: ISODate('2026-07-08T15:38:52.322Z')
  },
  {
    _id: ObjectId('6a4e1f22e633531336d7f2be'),
    user_message: 'i am not happy today',
    bot_response: 'Hello, I am your mental health assistant.',
    timestamp: ISODate('2026-07-08T15:42:54.123Z')
  }
]
mental_health_chatbot> 


run train_mental_model to train model from kaggle dataset 
run test_response after reddit_chat.csv