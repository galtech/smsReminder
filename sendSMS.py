import os
from twilio.rest import Client

accountSID = os.environ["TWILIO_ACCOUNT_SID"]
authToken = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(accountSID, authToken)

phoneNumbers = {"Peter1":"123",
                "Peter2":"123"}

for name,number in phoneNumbers.items():
    client.messages.create(
        to=number,
        from_="+16508305452",
        body=name+" this is test message, sincerely - Peter"        
    )
    


#body="Hi, this is a test reminder: You registered for CoderDojo Kells Autumn season Oct5-Nov23. Looking forward to seeing you there. If you can no longer make it please let us know by emailing info@coderdojokells.com"
