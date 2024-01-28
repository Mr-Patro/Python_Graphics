from twilio.rest import client
Account_sid="my_twilio_Account_id"
auth_token="provided by the account again"
client=client(Account_sid,auth_token)
client.message.create(from ="6371480921",body="hai re mg",to="subodha")
