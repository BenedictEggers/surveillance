# Author: Ben Eggers

# This file will email me at <ben.eggers36@gmail.com> to tell
# me that the file has been run. Used in conjunction with
# motion as part of an ad-hoc security system.

import smtplib
from time import strftime
from time import localtime

from email.MIMEMultipart import MIMEMultipart


FROM_ADDR = "your email here"
TO_ADDR = "who to warn here"
SUBJECT = "Event triggered %s" % strftime("%a, %d %b %Y %H:%M:%S", localtime())


def main():

	# Log in
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(FROM_ADDR, 'your pass here')

	# Set up our message
	msg = MIMEMultipart()
	msg['From'] = FROM_ADDR
	msg['To'] = TO_ADDR
	msg['Subject'] = SUBJECT

	# And send it
	text = msg.as_string()
	server.sendmail(FROM_ADDR, TO_ADDR, text)

	server.quit()


if __name__ == "__main__":
	main()
