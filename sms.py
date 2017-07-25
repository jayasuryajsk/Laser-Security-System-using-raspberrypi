from twilio.rest import TwilioRestClient

client = TwilioRestClient(", "")



def send_sms():
    client.messages.create(from_="from_number",to="to number",body="Intruder Alert,Please check your mail and click this link for live stream" 'https://www.ivideon.com/my/cameras/devices')
    print("SMS Sent to Registered Mobile")
