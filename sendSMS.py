import os
from twilio.rest import Client
import csv

accountSID = os.environ["TWILIO_ACCOUNT_SID"]
authToken = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(accountSID, authToken)

# read in phone number list
with open('data.csv', mode='r') as infile:
    reader = csv.reader(infile)
    phoneNumbers = {rows[0]:rows[1] for rows in reader}

# send text to each number 
for name,number in phoneNumbers.items():
    client.messages.create(
        to='+'+number,
        from_="+16508305452",
        body=name+" this is test message, sincerely - Peter"        
    )
    


#body="Hi, You registered for CoderDojo Kells Autumn season Oct5-Nov23. Looking forward to seeing you there. If you can no longer make it please let us know by emailing info@coderdojokells.com"
