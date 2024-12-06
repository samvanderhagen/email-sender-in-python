from email.message import EmailMessage
from passwordgoogle import password
import ssl
import smtplib

email_sender = "samuelbezerra411@gmail.com"
email_password = password

email_receiver = "samvanderhagen@gmail.com"

subject = "Default Email"
body = """
That's an email I will send to test my python skills!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

