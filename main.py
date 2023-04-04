import pandas
import datetime as dt
import smtplib
import os
import random
import numpy

##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
my_email = os.getenv('MY_EMAIL')
password = os.getenv('PASSWORD')
bd_data = pandas.read_csv("birthdays.csv")
new_data = bd_data.to_dict(orient="records")
print(new_data)

now = dt.datetime.now()
today = now.day
print(today)
this_month = now.month
this_day = (this_month, today)
for item in new_data:
    if item["day"] == today and item["month"] == this_month:
        print(item["name"])
        new_name = item["name"]
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
            old_letter = letter.read()
            new_letter = old_letter.replace("[NAME]", new_name)
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(user=my_email, password=password)
            server.sendmail(from_addr=my_email, to_addrs=item["email"],
                            msg=f"Subject:Birthday mail\n\n{new_letter}")




