# careclock
A twitter bot which gently reminds you to check in on others.

Code is in careclock.py, requirements are in requirements.txt, messages are in morning.txt, evening.txt, and daytime.txt respectively. Uses Twython to tweet.

You can set it up to run from a cron with something like this:

```
* * * * * cd /home/objectfox/careclock && source /home/objectfox/careclock/env/bin/activate && source /home/objectfox/careclock/creds.sh && python /home/objectfox/careclock/generate.py > /home/objectfox/careclock/cron.log
```
