##################### Normal Starting Project ######################
from datetime import datetime
import pandas as pd
import random
import smtplib

today = datetime.now()
today_tuple = (today.month, today.day)

df = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    letter_number = random.randint(1, 3)
    file_path = f"./letter_templates/letter_{letter_number}.txt"
    with open(file_path) as letter_file:
        letter_contents = letter_file.read()
        letter_contents = letter_contents.replace("[NAME]", birthday_person["name"])

    my_email = "codechad721@gmail.com"
    password = "suckalemon"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject: "
                f"Happy Birthday\n\n{letter_contents}"
               # f"Today is {birthday_person['name']}\'s birthday!\n\n" ---use this line instead to remind you to wish a HB
        )




