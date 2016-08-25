import json
from twilio.rest import TwilioRestClient

# Get credentials from external file
with open('cred.json') as cred_file:    
    cred = json.load(cred_file)
    
ACCOUNT_SID =  cred['account_sid']
AUTH_TOKEN  =  cred['auth_token']
FAKE_PHONE  =  cred['fake_phone']
MY_PHONE    =  cred['my_phone']

# Set Twilio's rest-client
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
# Set message
client.messages.create(
    to = MY_PHONE,
    from_ = FAKE_PHONE,
    body = 'Hello There',
)

         
