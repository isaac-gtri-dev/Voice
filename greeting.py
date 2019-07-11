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

def speakthistext(txt):   
	# write out to wav file 
	b = 'espeak -w temp.wav "%s" 2>>/dev/null' % txt  

	# speak aloud
	c = 'espeak -ven+m1 -k1 -s150 --punct="<characters>" "%s" 2>>/dev/null' % txt #speak aloud

	execute_unix(b) 
	execute_unix(c) 


print("Listening for name")
result = str(my_listener.wait_for_message_on('awesomeChannel').message)

names = ["connor-o'hara", "timothy hurley", "brian oten", "robbie ratcliff"]

for i in names:
    if i in result:
        speakthistext("Hello, " + result + " how are you doing?")
#   elif result == "Motion Detected":


