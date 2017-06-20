import time
import os
import sys
from urllib.request import urlretrieve
import smtplib
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("[*]Taking snap")
urlretrieve("http:/url-of-the-webacm/photoaf.jpg", "photo.jpg")

fromaddr = ""
toaddr = ""

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Intruder Alert..!!"

body = "system has detected an Intruder"
msg.attach(MIMEText(body, 'plain'))

filename = "photo.jpg"
attachment = open("location-of-the-image" , "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
print("[*]starting encryption....")
server.starttls()
print("[*]logging in..")
server.login(fromaddr, "password")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
print("[*]Message has been delivered.")





