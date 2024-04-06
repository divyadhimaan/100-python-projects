import smtplib

my_email = "divya.test.3424@gmail.com"
my_password = "Test@123"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls() #makes connection secure
connection.login(my_email, my_password)
connection.sendmail(from_addr=my_email, to_addr="divya_test_3424@yahoo.com", message="Hello")
connection.close()
