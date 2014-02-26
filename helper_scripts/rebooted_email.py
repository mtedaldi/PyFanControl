#!/usr/bin/python

# Simple script that sends an email with a given text to given addresses
# This script is used to notify users on reboots of the device since this
# could point to problems.
# The script located in the users home directory
# The scribt is started from the users crontab
# This way, there are no root right required in to process

# The crontab entry:
# @reboot sleep 15; ./rebooted_email.py


# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

msg = MIMEText('Pi im Laserschrank neu gestartet')
msg_from = 'tedaldi@hifo.uzh.ch'
msg_to = ['tedaldi@hifo.uzh.ch', 'kasper@hifo.uzh.ch']
me = msg_from
you = msg_to


# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Pi (Laserschrank) rebooted'
msg['From'] = msg_from
msg['To'] = ", ".join(msg_to)

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('smtp.uzh.ch')
s.sendmail(me, you, msg.as_string())
s.quit()


