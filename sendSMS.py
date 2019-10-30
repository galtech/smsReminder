import os
import sys
from twilio.rest import Client
import csv

accountSID = os.environ["TWILIO_ACCOUNT_SID"]
authToken = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(accountSID, authToken)

# read in phone number list
with open(sys.argv[1], mode='r') as infile:
    reader = csv.reader(infile)
    phoneNumbers = {rows[0]:rows[1] for rows in reader}


# read in custom SMS message
with open(sys.argv[2], mode='r') as infiletwo:
    externalMsg = infiletwo.read()

# read in a short From: name
fromName = sys.argv[3]

# send text to each number 
for name,number in phoneNumbers.items():
    client.messages.create(
        to='+'+number,
        from_=fromName, #"CoderDojo" "+16508305452",
        body=name+', '+externalMsg 
    )
    


