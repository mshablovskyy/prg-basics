import os
import re

path = os .path.dirname(__file__) + "/"
file = path + "email.txt"

with open(file) as file:
    text = file.read()
    
# sender email address
sender_email = re.findall("<.+>", str(re.findall("From:.*>", text)))[0][1:-1]
print(sender_email)
# recipient email address
recipient_email = re.findall("<.+>", str(re.findall("To:.*>", text)))[0][1:-1]
print(recipient_email)
# email subject
subject = re.findall(":.*", str(re.findall("Subject:.*", text)))[0][2:-2]
print(subject)
# email body
body = re.findall("7bit.*", text, flags=re.DOTALL)[0][6:-2]
print(body)