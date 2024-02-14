#!/usr/bin/env python3
# Created by Ranger


# This is a Python script that connects to your 

# Usage information
# python gmail.py

# What this script does:
# Modify the send_email function to handle attachments.
# The script requires an active internet connection to send the email.
# The script requires a Gmail address and password to send the email.

# Import required modules
# The os module provides an API for interacting with the operating system, including file operations and environment variables.
# The smtplib module provides an API for sending emails using the Simple Mail Transfer Protocol (SMTP).
# The email.mime.multipart module provides an API for creating MIME objects for sending emails with attachments.
# The email.mime.text module provides an API for creating MIME objects for sending plain text emails.
# The email.mime.base module provides an API for creating MIME objects for sending emails with attachments.
# The email module provides an API for creating and sending emails.

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

os.system('cls' if os.name == 'nt' else 'clear')

# Print welcome banner
print("\nMade By David\nVersion 1.0.0\n")

def send_email(to_email, attachment_path=None):
    # Get the email, password, subject, and message from the user
    from_email = input("Enter your Gmail address: ")
    from_password = input("Enter your Gmail password: ")
    subject = input("Enter your subject: ")
    message_body = input("Enter your message: ")

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach message body directly
    msg.attach(MIMEText(message_body, 'plain'))

    # Attach the file if path is not None
    if attachment_path is not None:
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {os.path.basename(attachment_path)}",
        )
        msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully.")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    to_email = input("Enter the recipient's email address: ")
    send_email(to_email)