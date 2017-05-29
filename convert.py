import record
import json

def intent(transcript):
	try:	
		transcript_json = json.loads(transcript)	
		intent = transcript_json["entities"]["intent"][0]["value"]
		return intent
	except:
		return "none"
