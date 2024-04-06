import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

my_email = os.getenv('MY_GOOGLE_EMAIL')
my_password = os.getenv('MY_GOOGLE_PASSWORD')

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() #makes connection secure
    connection.login(my_email, my_password)
    connection.sendmail(from_addr=my_email, to_addr="divya_test_3424@yahoo.com", message="Hello")
