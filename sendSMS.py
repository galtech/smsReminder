import os
from twilio.rest import Client
import csv

accountSID = os.environ["TWILIO_ACCOUNT_SID"]
authToken = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(accountSID, authToken)

message = """
Reminder: You registered for CoderDojo Kells Autumn
Season starting this Saturday 3:30-5pm for 8 weeks. Qus: info@coderdojokells.com
"""

# read in phone number list
with open('data.csv', mode='r') as infile:
    reader = csv.reader(infile)
    phoneNumbers = {rows[0]:rows[1] for rows in reader}

# send text to each number 
for name,number in phoneNumbers.items():
    client.messages.create(
        to='+'+number,
        from_="CoderDojo", #"+16508305452",
        body=name+', '+message 
    )
    


