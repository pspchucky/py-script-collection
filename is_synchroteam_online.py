import urllib
import urllib.request
from html.parser import HTMLParser
from time import sleep
from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

#TEST Keys
#account_sid = "" # Your Account SID from www.twilio.com/console
#auth_token  = ""  # Your Auth Token from www.twilio.com/console

#LIVE Keys
account_sid = "" # Your Account SID from www.twilio.com/console
auth_token  = ""  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)
class TitleParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.match = False
        self.title = ''

    def handle_starttag(self, tag, attributes):
        self.match = True if tag == 'title' else False

    def handle_data(self, data):
        if self.match:
            self.title = data
            self.match = False

def checkWebsite():
    synchro = urllib.request.urlopen("https://test.synchroteam.com/app/")
    html_string = str(synchro.read())
    parser = TitleParser()
    parser.feed(html_string)
    if (parser.title == "Synchroteam - Planned Maintenance"): #subject to change | 9/4/2016
        print("Fucking maintenance, checking again in 5 seconds...")
    else:
        message = client.messages.create(body="Synchroteam is back online",
        to="", #your number
        from_="") #Test Key
        print("Oh shit its done!")
        exit()
    sleep(5)
    checkWebsite()

checkWebsite()
