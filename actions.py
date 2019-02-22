from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from datetime import datetime

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ActionWeather(Action):
	def name(self):
		return 'action_weather'
		
	def run(self, dispatcher, tracker, domain):
		from apixu.client import ApixuClient
		# api_key = '...' #your apixu key
		# client = ApixuClient(api_key)
		
		# loc = tracker.get_slot('location')
		# current = client.getCurrentWeather(q=loc)
		
		# country = current['location']['country']
		# city = current['location']['name']
		# condition = current['current']['condition']['text']
		# temperature_c = current['current']['temp_c']
		# humidity = current['current']['humidity']
		# wind_mph = current['current']['wind_mph']

		response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format("0","1","2","3","4")
						
		dispatcher.utter_message(response)
		return [SlotSet('location',"India")]
class Age(Action):
	def name(self):
		return 'action_calculate_age'
		
	def run(self,dispatcher,tracker,domain):
		current_date = datetime.now()
		creation_date="2019-02-10"
		creation_date = datetime.strptime(creation_date, "%Y-%m-%d")
		days = abs(current_date - creation_date).days
		response = """I am {} days old.""".format(days)
		dispatcher.utter_message(response)
		return [SlotSet("age","age")]