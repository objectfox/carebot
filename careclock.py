#!/usr/bin/env python3

from twython import Twython
from datetime import datetime, timedelta
import random
import pytz
import os

# Check to see if it's time to tweet

if os.path.exists("time_to_tweet.txt"):
	timestamp = open("time_to_tweet.txt").read().strip()
	time_to_tweet = datetime.fromisoformat(timestamp)
	if time_to_tweet >= datetime.now(pytz.timezone("US/Central")):
		exit()
else:
	print("No time_to_tweet file, auto-tweeting.")

# Compose our tweet

now = datetime.now(pytz.timezone("US/Central"))

if now.hour <= 9:
	# Morning message
	message_file = "morning.txt"

elif now.hour <= 18:
	# Daytime message
	message_file = "daytime.txt"

else:
	# Evening message
	message_file = "evening.txt"

message = random.choice(open(message_file).readlines()).strip()

print("Tweeting: %s" % message)

# Create our Twitter object

twitter = Twython(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'],
                  os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])

# Post to Twitter

twitter.update_status(status=message)

# Schedule tomorrow's tweet

tomorrow = (datetime.now(pytz.timezone("US/Central"))+timedelta(days=1)).replace(hour=8,minute=0,second=0)
tomorrow = tomorrow + timedelta(minutes=random.randint(0,14*60))
print("Scheduling next tweet for %s" % tomorrow)
timefile = open("time_to_tweet.txt","w")
timefile.write(tomorrow.isoformat()+"\n")