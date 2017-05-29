import snowboydecoder
import sys
import signal
import convert
import vlc

from brain import Brain
modules = Brain.get_modules()

import record

interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

model = sys.argv[1]

signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Listening...')

while True:
    detector.start(detected_callback=snowboydecoder.play_audio_file,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

    transcript = record.stt()
    try:
    	intent = convert.intent(transcript)
	print intent	
    except:
	result = "Dieser Befehl ist nicht bekannt"

    try:
	result = Brain.query(modules, intent, transcript)
    except:
	result = "Bitte spezifizieren"  

    print result

    if (result==None):
    	p = vlc.MediaPlayer("https://api.voicerss.org/?key=19eeef30be214ff296079bc724ebd9c9&hl=de-de&src=Dieser Befehl ist nicht bekannt!")
	print "Dieser Befehl ist nicht bekannt!"
    else:
    	p = vlc.MediaPlayer("https://api.voicerss.org/?key=19eeef30be214ff296079bc724ebd9c9&hl=de-de&src=" + result)
    p.play()
