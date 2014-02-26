#!/usr/bin/python
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
#fp = open(textfile, 'rb')
# Create a text/plain message
#msg = MIMEText('Dies ist nur ein Test')
#fp.close()

msg = MIMEText('Dies ist nur ein Test')
msg_from = 'tedaldi@hifo.uzh.ch'
msg_to = ['marco.tedaldi@gmail.com', 'tedaldi@hifo.uzh.ch', 'kasper@hifo.uzh.ch']
me = msg_from
you = msg_to


# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Testmail von Pi'
msg['From'] = msg_from
msg['To'] = ", ".join(msg_to)

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('smtp.uzh.ch')
s.sendmail(me, you, msg.as_string())
s.quit()


