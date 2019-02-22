from flask import Flask, redirect, url_for, request,jsonify
from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
#from rasa_slack_connector import SlackInput
nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)
app = Flask(__name__)
@app.route('/message',methods = ['POST'])
def Message():
    raw_json = request.get_json(force=True)
    message = raw_json['message']
    reply = agent.handle_message(str(message))
    return jsonify({'result':'Success!','reply':str(reply[0])})
if __name__ == '__main__':
	app.run(debug = True)