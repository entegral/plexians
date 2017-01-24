# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries

from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC4ef5b1267687ff3f1984829aa9e13f8b"
auth_token = "afbcc30cede0b005efa5b9c20e365749"
client = TwilioRestClient(account_sid, auth_token)


def send_sms(phone, note):
    message = client.messages.create(to=phone, from_="+15415000742",
                                     body=note)

phone = "+15416018751"
note = "test biiiitch!"
send_sms(phone, note)

def send_all(people, note):
    note = input("What would you like to sms?")
    for individual in people:
        send_sms(individual.phone, note)
