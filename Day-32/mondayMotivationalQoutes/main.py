import datetime as dt
from dotenv import load_dotenv
import os
import smtplib
import random

# Load environment variables
load_dotenv()
my_email = os.getenv('MY_GOOGLE_EMAIL')
my_password = os.getenv('MY_GOOGLE_APP_PASSWORD')
receiver_email = os.getenv('RECEIVER_EMAIL')
smtp_port=587
smtp_server="smtp.gmail.com"

PATH_TO_DATA_FILE="100-python-projects/Day-32/mondayMotivationalQoutes/qoutes.txt"
qoutes_list=[]


# checks if monday
def check_day():
    now = dt.datetime.now()
    day = now.day

    if day == 1:
        return True
    return False

#  Reads data file, it has 102 qoutes
def get_data():
    global qoutes_list
    with open(PATH_TO_DATA_FILE) as data_file:
        qoutes = data_file.read()
        qoutes_list = qoutes.split("\n")
        
def random_qoute():
    return random.choice(qoutes_list)
        
def send_mail():
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as connection:
            connection.starttls()  # Encrypts the email
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=receiver_email,
                msg=f"Subject:Monday Motivation\n\n{random_qoute()}"
            )
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
        
get_data()
# if check_hour():
send_mail()
