# 289
# import smtplib
#
# my_email = 'jl29071009jl@gmail.com'
# password = 'kszqbxpgxzcbgdqk'
#
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs='jl29071009jl@yahoo.com',
#                         msg='Subject:hello\n\nThis is the body of my email.'
#     )


# 290
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# day_of_birth = dt.datetime(year=1996, month=10, day=9, hour=7)
# print(day_of_birth)


# 291
import smtplib
import datetime as dt
import random

MY_EMAIL = 'jl29071009jl@gmail.com'
MY_PASSWORD = 'asd123456'

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readline()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_PASSWORD,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )