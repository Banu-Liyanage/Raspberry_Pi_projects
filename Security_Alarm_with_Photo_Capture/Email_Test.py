import smtplib
from email.message import EmailMessage
import time

from_email = "peteparker31800@gmail.com"
from_password = "iknb eigg yyri kina"
to_email = "wishwadehi190@gmail.com"

msg = EmailMessage()
msg.set_content("Test Email")
msg["From"] = from_email
msg["To"] = to_email
msg["Subject"] = "Test"

print("Connecting to SMTP...")
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(from_email, from_password)
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print("Error:", e)
