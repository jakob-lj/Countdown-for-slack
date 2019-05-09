from time import sleep
import json
import urllib3
import certifi
from datetime import datetime, timedelta
import daemon

urllib3.disable_warnings()

class Notifier:
    def __init__(self):
        self.http = urllib3.PoolManager(1)
        self.slack_url = self.getUrl()
        self.goal = datetime(2019, 6, 18)
        #print("countdown to goal: " + str(self.goal))
        #self.sentTo = [datetime.now().date()]
        self.sentTo = []
        #self.send()
        #print(self.sentTo)

    def run(self):
        if not datetime.now().date() in self.sentTo and datetime.now().hour == 11:
            self.send()

    def testRun(self):
        self.sentTo.append(datetime.now().date())
        self.send()

    def send(self):
        self.sentTo.append(datetime.now().date())
        self.post_to_slack(self.getMessage())


    def post_to_slack(self, message):
        encoded_data = json.dumps({'text': message}).encode('utf-8')
        response = self.http.request("POST", self.slack_url, body=encoded_data, headers={'Content-Type': 'application/json'})

    def getMessage(self):
        now = datetime.now()
        delta = (self.goal-now).days + 1
        return "T minus %i days" % delta

    def getUrl(self):
        with open("url.dat") as u:
            return u.readline().strip()

n = Notifier()
n.run()
#while True:
#    n.run()
#    sleep(60)
