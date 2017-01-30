#!/usr/bin/env python
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys


recipients = ['test@test.com'] 
emaillist = [elem.strip().split(',') for elem in recipients]
msg = MIMEMultipart()
msg['Subject'] = 'test'
msg['From'] = 'test@test.com'
#msg['Reply-to'] = 'abcxyz@gmail.com'
 
msg.preamble = 'Multipart massage.\n'
 
part = MIMEText("Hi, please find the attached file")
msg.attach(part)
 
part = MIMEApplication(open(str(sys.argv[1]),"rb").read())
part.add_header('Content-Disposition', 'attachment', filename=str(sys.argv[1]))
msg.attach(part)

debuglevel = True
server = smtplib.SMTP("smtp.mail.yahoo.com:587")
server.set_debuglevel(debuglevel)
server.ehlo()
server.starttls()
server.login("test@test.com", "Password")
 
server.sendmail(msg['From'], emaillist , msg.as_string())
