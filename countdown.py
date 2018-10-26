from time import sleep
#from contextlib import closing
#from urllib.request import urlopen, Request
#from urllib.parse import urlencode

#url = 'https://hooks.slack.com/services/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'
#values = {'text' : 'Hey Jake'}
#data = urlencode(values)
#data = data.encode("ascii")
#req = Request(url=url, data=data)
#req.add_header('Content-type', 'application/json')
#res = urlopen(req).read()



#data = urlencode({"text":"hi jake"}).encode()
#with closing(urlopen(url, data)) as response:
#    print(response.read().decode())

import json
import urllib3
import certifi
from datetime import datetime, timedelta

class Notifier:

    def __init__(self):
        self.http = urllib3.PoolManager(1)
        self.slack_url = ""
        self.goal = datetime(2019, 6, 22)
        print("countdown to goal: " + str(self.goal))
        self.sentTo = [datetime.now().date()]
        self.sentTo.pop()

        print(self.sentTo)

    def run(self):
        if not datetime.now().date() in self.sentTo and datetime.now().hour == 10:
            self.send()
            self.sentTo.append(datetime.now().date())

    def send(self):
        self.post_to_slack(self.getMessage())

    def post_to_slack(self, message):
        encoded_data = json.dumps({'text': message}).encode('utf-8')
        response = self.http.request("POST", self.slack_url, body=encoded_data, headers={'Content-Type': 'application/json'})

    def getMessage(self):
        now = datetime.now()
        delta = (self.goal-now).days
        return "T minus %i days" % delta

if __name__ == '__main__':
    n = Notifier()
    while True:
        n.run()
        sleep(60)
