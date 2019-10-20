import os
from twilio.rest import Client
import csv

accountSID = os.environ["TWILIO_ACCOUNT_SID"]
authToken = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(accountSID, authToken)

grpMsg = """
Reminder: You registered for CoderDojo Kells Autumn
Season starting this Sat. 3:30-5pm for 8 weeks. See you then.
Qus: info@coderdojokells.com
"""

singleMsg = """
You expressed an interest in our Autumn season. 
We now have a space. If you are still interested can 
you please confirm by emailing info@coderdojokells.com 
"""

# read in phone number list
with open('extradata.csv', mode='r') as infile:
    reader = csv.reader(infile)
    phoneNumbers = {rows[0]:rows[1] for rows in reader}

# send text to each number 
for name,number in phoneNumbers.items():
    client.messages.create(
        to='+'+number,
        from_="CoderDojo", #"+16508305452",
        body=name+', '+singleMsg 
    )
    


