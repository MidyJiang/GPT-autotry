import csv,time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

path=os.path.abspath("")
print(9,path)
for a,b,c in os.walk(path):
  print(a,b,c)
