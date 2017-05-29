import re
import json, urllib2
import pyowm
from datetime import datetime

WORDS = "weather"

owm = pyowm.OWM('c863a42da17862a24bc8cb26877e897e')

def isValid(text):
	return bool(re.search(WORDS, text, re.IGNORECASE))

def handle(text, transcript):

	transcript_json = json.loads(transcript)	
	location = transcript_json["entities"]["location"][0]["value"]
	time = transcript_json["entities"]["datetime"][0]["values"][0]["value"]
	
	print("City: " + location)	
	
	fc = owm.three_hours_forecast(location)
	f = fc.get_forecast()
	st = f.get_weathers()

	if (time[11:13]=="00"):
		weather = fc.get_weather_at(datetime(int(time[0:4]), int(time[5:7]), int(time[8:10]), 12, int(time[14:16]), int(time[17:19])))
		print "Time: " + str(datetime(int(time[0:4]), int(time[5:7]), int(time[8:10]), 12, int(time[14:16]), int(time[17:19])))
	else:
		weather = fc.get_weather_at(datetime(int(time[0:4]), int(time[5:7]), int(time[8:10]), int(time[11:13]), int(time[14:16]), int(time[17:19])))
		print "Time: " + str(datetime(int(time[0:4]), int(time[5:7]), int(time[8:10]), int(time[11:13]), int(time[14:16]), int(time[17:19])))
	
	ans1 = weather.get_status()
	ans2 = weather.get_temperature('celsius')['temp']
	answer = "Es wird " + ans1 + " mit " + str(int(ans2)) + " Grad in " + location
	answer = answer.replace("Clear", "klar")
	answer = answer.replace("Clouds", "wolkig")
	answer = answer.replace("Rain", "regnerisch")
	answer = answer.replace("Snow", "schneien")
	return answer

