import requests
from datetime import datetime
import smtplib 
from dotenv import load_dotenv
import os
import time


load_dotenv()
my_email = os.getenv('MY_GOOGLE_EMAIL')
my_password = os.getenv('MY_GOOGLE_APP_PASSWORD')

MY_LAT = 12.971599
MY_LONG = 77.594566

# Email message with headers
email_message = """From: {}
To: {}
Subject: ISS Spotting

The ISS is above you in the sky""".format(my_email, my_email)

def is_iss_in_range():
    
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])
    iss_position = (latitude, longitude)
    
    if ((MY_LAT - 5) <= latitude <= (MY_LAT + 5)) and ((MY_LONG - 5) <= longitude <= (MY_LONG + 5)):
        return True
    return False


def is_night():


    parameters = {
        "lat": latitude,
        "lng": longitude,
        "formatted": 0
    }

    response = requests.get(url =f"https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data = response.json()


    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)

    time_now = datetime.now()
    now = time_now.hour
    print(now)

    if(now <= sunrise or now >= sunset):
        return True
    return False

while True:
    time.sleep(60)
    if is_iss_in_range() and is_night():
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()  # Encrypts the email
                connection.login(user=my_email, password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=my_email,
                    msg=email_message
                )
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email. Error: {e}")
