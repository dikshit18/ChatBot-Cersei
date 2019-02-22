# Sample CHATBOT Tutorial 
Initially, i wanted to name it WeatherBot in order to just hit weather API(but i didn't actually call any API). But later i extended it to other static general purpose questions. Hence some files have name weather in them.

To create data.json which is my intents classification file, i used "rasa-nlu-trainer" in my cmd after installing Node.js. The RASA framework providies us an easy way to train our data through rasa-nlu-trainer which is a very interactive dashboard.

data  - data.json --> Intene classification file
      - stories.md --> Contains RASA stories for dialogue management using RASA core
mndels - Contains trained model
actions.py --? Contains the code where we perform dynamic operations through Chatbot liking Hitting API, Mathematical Calculations etc.
config_spacy.json --> Contains pipeline and trained models data
nlu_model.py --> File to train our model
requirements.txt --> Contains required dependencies to install Rasa nlu and core, its training
train_init.py --> Used to train out model
train_online.py - Used to train our model online. Here we can correct our model if it is doing some mistake
run_app.py -- > Converts RASA bot into API using FLASK.
weather_domain.yml --> Contains slots,intents,actions,entities,tenplates

After training , a demo conversation with my chatbot: 
