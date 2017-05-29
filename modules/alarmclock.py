import re
from time import gmtime, strftime

WORDS = "alarmclock"

def isValid(text):
	return bool(re.search(WORDS, text, re.IGNORECASE))

def handle(text, transcript):
	return strftime("Es ist %H Uhr %M", localtime())

