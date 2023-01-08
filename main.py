#####################################
#
# Aurthor: Matthew. Klatt
#
# Version: v1.0.0
#
# Project name: AERL Clocking in/out system.
#
# Project description:
#  This was written to mess with Nat.
#  I'm not sorry, I told you I'd do it.
#
#####################################






import sys
import time
import ntplib
import random
import requests
import pyautogui as pag
import pyperclip as clipboard
from datetime import datetime, timezone

s_combinedMessage = "xxx"
s_savedHour = "999"
s_message = """
Hey Nat,
This is an automated message I created to remind you to pick me up tomorrow morning for work, this message will be sent once every hour until I turn it off.
I told you I'd do it lmao

Now, enjoy a randomly generated 'fun-fact':
"""
a_facts = [
	"A dentist invented the electric chair. (I don't think he had many repeat patients.)",
	"The dot over the letter i is called a tittle.",
	"In ancient Egypt, priests plucked EVERY hair from their bodies, including their eyebrows and eyelashes.\n(Any modern woman that has attempted to pluck a man's eyebrows only to hear him scream like a toddler finds this fact unbelievable.)",
	"A crocodile cannot stick its tongue out. (This is only a problem for pre-teen crocs when their parents ask them to do chores.)",
	"The common house fly hums in the middle octave key of F.",
	"Only one person in two billion will live to be 116 or older.",
	"Women blink nearly twice as much as men. (Research has shown that dumbfounded wives blink at five times their husbands' rate after he has done something idiotic.)"
]
	
i_betweenClicks = 1.00




while(len(a_facts) > 0):
	# shake to keep awake
	#"""
	pag.moveTo(100, 200)
	pag.moveTo(200, 100)
	pag.moveTo(100, 200)
	pag.moveTo(200, 100)
	#"""
	
	
	try:
		requests.get("https://www.google.com.au/", timeout = 2)
		client = ntplib.NTPClient()
		response = client.request("1.au.pool.ntp.org", version = 3)
		response.offset
	except:
		print("- Connection dropped . . .")
	
	
	
	if(s_savedHour != datetime.fromtimestamp(response.tx_time).strftime("%H")):
		rand = random.randrange(len(a_facts))
		s_choice = a_facts[rand]
		s_combinedMessage = f"{s_message} \n{s_choice}"
		a_facts.pop(rand)
		clipboard.copy(s_combinedMessage)
		
		
		# navigate os
		#"""
		pag.click(x=210, y=19)   # Maximize Chrome
		time.sleep(i_betweenClicks)
		pag.click(x=885, y=738)  # Click on message box
		time.sleep(i_betweenClicks)
		clipboard.paste()
		time.sleep(i_betweenClicks)
		#pag.press('enter')       # send message
		time.sleep(i_betweenClicks)
		pag.click(x=210, y=19)   # Minimize Chrome
		#"""

		# Debug: Print what was sent out.
		print(f"{s_combinedMessage} \n ---------------------- \n\n")
		s_savedHour = datetime.fromtimestamp(response.tx_time).strftime("%H")
		
	time.sleep(5.00)
	
	# wait 1 hour, and loop again
	#time.sleep(3600.00)
	