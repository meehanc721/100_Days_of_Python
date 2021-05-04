from twilio.rest import Client

TWILIO_SID = "AC0cfc4da53b41e7a8564ac48010b7ef67"
TWILIO_AUTH_TOKEN = "64dc82096cc216ace3a543a61d75bdff"
TWILIO_VIRTUAL_NUMBER = "+16193822382"
TWILIO_VERIFIED_NUMBER = "+17029349088"


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)













    # def text_notification(self):
    #
    #     tw_account_sid = "AC0cfc4da53b41e7a8564ac48010b7ef67"
    #     tw_auth_token = "64dc82096cc216ace3a543a61d75bdff"
    #
    #     client = Client(tw_account_sid, tw_auth_token)
    #     message = client.messages \
    #         .create(
    #         body=formatted_articles_list[i],
    #         from_='+116193822382',
    #         to='+17029349088'
    #     )
    #     print(message.status)