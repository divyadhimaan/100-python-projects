import datetime as dt
import pandas as pd
from dotenv import load_dotenv
import os
import random
import smtplib

PATH_TO_DATA_FILE="100-python-projects/Day-32/automateBirthdayEmails/birthdays.csv"
PATH_TO_TEMPLATE_FOLDER="100-python-projects/Day-32/automateBirthdayEmails/letter_templates"
birthdays_dict = {}

# Load environment variables
load_dotenv()
my_email = os.getenv('MY_GOOGLE_EMAIL')
my_password = os.getenv('MY_GOOGLE_APP_PASSWORD')
smtp_port=587
smtp_server="smtp.gmail.com"

# 1. Update the birthdays.csv
# def update_birthday_file():
    # try:
    #     file_content = pd.read_csv(PATH_TO_DATA_FILE)
    #     print("Add the details: ")
    #     name = input("Name of the person: ")
    #     email = input("Email of the person: ")
    #     dob = input("DOB of the person, (DD-MM-YYYY) format: ")
    #     dob_split = dob.split("-")
        
    #     new_entry = {
    #         "name": name,
    #         "email": email,
    #         "year": dob_split[2],
    #         "month":dob_split[1],
    #         "day":dob_split[0]
    #     }
        
    #     new_data = pd.DataFrame([new_entry])
    #     updated_data = file_content._append(new_data, ignore_index=True)
    #     updated_data.to_csv(PATH_TO_DATA_FILE,index=False)
    #     print(f"New Entry added to Data File: name: {name}, email:{email}, DOB:{dob_split[0]}-{dob_split[1]}-{dob_split[2]}")
            
    # except FileNotFoundError:
    #     print("File not found: %s" % PATH_TO_DATA_FILE)




# 2. Check if today matches a birthday in the birthdays.csv
def read_birthday_file():
    global birthdays_dict
    try:
        file_content = pd.read_csv(PATH_TO_DATA_FILE)
        birthdays_dict = {(data_row.month, data_row.day): data_row for index, data_row in file_content.iterrows()}
    except FileNotFoundError:
        print("File not found: %s" % PATH_TO_DATA_FILE)

def check_today():
    today_now = dt.datetime.now()
    today = (today_now.month, today_now.day)
    if today in birthdays_dict:
        birthday_person = birthdays_dict[today]
        letter_template_path = f"{PATH_TO_TEMPLATE_FOLDER}/letter_{random.randint(1,3)}.txt"
        with open(letter_template_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday_person["name"])
        
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as connection:
                connection.starttls()  # Encrypts the email
                connection.login(user=my_email, password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=birthday_person["email"],
                    msg=f"Subject:Happy Birthday!\n\n{contents}"
                )
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email. Error: {e}")


# command = input("Type update to update someone's birthday in your data otherwise 'c' for continue: ")
# if command == "update":
#     update_birthday_file()
# else:
read_birthday_file()
check_today()
