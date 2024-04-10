import smtplib
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve email and password from environment variables
my_email = os.getenv('MY_GOOGLE_EMAIL')
my_password = os.getenv('MY_GOOGLE_APP_PASSWORD')
receiver_email = os.getenv('RECEIVER_EMAIL')

# Email message with headers
email_message = """From: {}
To: {}
Subject: Test Email

Hello, this is a test email.""".format(my_email, my_email)

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Encrypts the email
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver_email,
            msg=email_message
        )
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email. Error: {e}")
