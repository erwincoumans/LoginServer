from flask import render_template
from flask_mail import Message
from auth import app

import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_account_created_email(user):
    if app.debug:
        print("debug, no email!")
        return
    message = Message('Craft E-mail Verification', [user.email])
    message.body = render_template('account_created_email.txt', user=user)
    print("message=", message)
    msg = MIMEMultipart()

    msg['From'] = 'root@localhost'
    msg['To'] = user.email
    msg['Subject'] = "Confirm Craft registration!"

    msg.attach(MIMEText(message.body, 'plain'))
    server = smtplib.SMTP('localhost')
    server.starttls()
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()    
