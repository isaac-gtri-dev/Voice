import subprocess
import time
from pubnub.callbacks import SubscribeCallback 
from pubnub.enums import PNStatusCategory  
from pubnub.pnconfiguration import PNConfiguration  
from pubnub.pubnub import PubNub  
import threading 
import time  
from time import sleep 
from pubnub.pubnub import PubNub, SubscribeListener  

from gtts import gTTS 
import os 

pnconfig = PNConfiguration() 
pnconfig.subscribe_key = "sub-c-bab9dc6c-912f-11e9-9769-e24cdeae5ee1" 
pnconfig.publish_key = "pub-c-14a2c33b-ff74-4bb7-8139-ff46eed621cc" 

 
pubnub = PubNub(pnconfig)
print("setting up listener")
my_listener = SubscribeListener()

print("adding listener")
pubnub.add_listener(my_listener)
print("subscribing to channel")
pubnub.subscribe().channels('awesomeChannel').execute()


def execute_unix(inputcommand):
   p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()
   return output

def tts(mytext):
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("welcome.mp3") 
        os.system("mpg321 welcome.mp3") 

tts("Hello, my name is iris.")

print("Listening for name")
#result = str(my_listener.wait_for_message_on('awesomeChannel').message)

lastmsg = "" #result

while True:
        result = str(my_listener.wait_for_message_on('awesomeChannel').message)
	print("*******result = " + result)
        if result != lastmsg:
                names = ["connor-o'hara", "timothy hurley", "brian oten", "robbie ratcliff"]

                #for i in names:
		if result in names:
			tts("Hello, " + result + " how are you doing?")
		elif result == ("Motion Detected"):
			tts("I am detecting motion.")

                lastmsg = result

                print(result)

#        if result =
#   elif result == "Motion Detected":

