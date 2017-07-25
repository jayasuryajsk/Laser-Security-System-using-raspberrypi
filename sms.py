from twilio.rest import TwilioRestClient

client = TwilioRestClient("ACaf5326775ed7f280cb76882b3202c431", "2a2c55dfc508eaac902d45e4bbe89f68")



def send_sms():
    client.messages.create(from_="+13363106998",to="+919944820260",body="Intruder Alert,Please check your mail and click this link for live stream" 'https://www.ivideon.com/my/cameras/devices')
    print("SMS Sent to Registered Mobile")
