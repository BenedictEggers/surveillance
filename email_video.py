# Author: Ben Eggers

# This script accepts a filename as a parameter. It grabs the
# video located at that filename, and emails it to me. Used
# in conjunction with email_notify_event.py to create an
# ad hoc security system.


import sys
import smtplib
import email

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from time import localtime
from time import strftime


FROM_ADDR = 'your email@gmail.com'
TO_ADDR = 'warned persons email@gmail.com'
SUBJECT = 'Video %s' % strftime("%a, %d %b %Y %H:%M:%S", localtime())


def main():
	# Make sure we got a file
	fo = open(sys.argv[1], 'r')
	
	# Connect and log in
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(FROM_ADDR, 'password for your email')

	# Set up our message
	msg = MIMEMultipart()
	msg['From'] = FROM_ADDR
	msg['To'] = TO_ADDR
	msg['Subject'] = SUBJECT

	part = MIMEApplication(fo.read())
	part.add_header('Content-Disposition', 'attachment', filename=sys.argv[1])
	msg.attach(part)	

	# And send it
	server.sendmail(FROM_ADDR, TO_ADDR, msg.as_string())


if __name__ == "__main__":
	main()
