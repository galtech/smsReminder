# smsReminder
### A simple SMS appointment or event reminder

This is a simple script to send appointment or event reminders using the Twilio API. 
Your accountID and token can be added to your environment variables and referenced in the 
code as I have done. 

Names and phone numbers can be stored in a CSV. You may use the sample file I have included as a guide.  

### How to run 

When running from command line, follow script name with three arguments in the following order:

1. contact list in CSV format (see sample file)
2. text file with desired SMS message (see sample file)
3. A name that appears in the From location on the message the person receives

example: python sendSMS.py data.csv msg.txt smsBot 
