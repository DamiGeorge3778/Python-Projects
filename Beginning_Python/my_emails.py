from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "Dami George"
message['to'] = "akintundegeorge23@gmail.com"
message['subject'] = "This is a test"
message.attach(MIMEText("Body"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("damio3778@gmail.com", "coderz4life")
    smtp.send_message(message)
    print("Sent...")
# WOULD WORK IF THE EMAIL ADDRESS EXISTED 🤷‍♂️
# TO COMPLICATED