#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime
# Change to your own account information
to = 'erouse@northwestern.edu'
gmail_user = 'biomechdevices@gmail.com'
gmail_password = 'ilikelegs'
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()
# Very Linux Specific
arg='ip route list'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
ipaddr = split_data[split_data.index('src')+1]
my_ip = 'IP Address for Raspberry Pi is %s' % ipaddr + '\nTime and Date: '+today.strftime('%I %M %p %d %b %Y')
msg = MIMEText(my_ip)
msg['Subject'] = 'IP For RPi on %s' % today.strftime('%b %d %Y')
msg['From'] = gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
