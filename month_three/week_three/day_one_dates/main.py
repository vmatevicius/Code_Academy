import datetime
import calendar
import pickle

# Write a function that calculates difference in days between two datetimes.

# time_one = datetime.datetime.today()
# time_two = datetime.datetime(1999, 1, 5, 12, 30, 58)

# difference = (time_one - time_two).days
# print(f"days - {difference}")
# print(f"years - {round(difference / 365)}")

# Write a function that takes a datetime object, which will represent employees starting work day.
# and will return amount of total holidays gained during the work until today. 1 Month = 1.6 day off


# def calculate_holidays(starting_date: datetime.date) -> float:
#     today = datetime.date.today()
#     return round(
#         (today.year - starting_date.year) * 12
#         + (today.month - starting_date.month) * 1.6,
#         1,
#     )


# date = datetime.date(2023, 1, 1)
# print(calculate_holidays(date))

# find next 3 Fridays that happend to be Friday the 13th
# date = datetime.date.today()
# fridays = []
# while True:
#     if date.weekday() == 4 and date.day == 13:
#         fridays.append(date)
#         date = date + datetime.timedelta(days=1)
#     date = date + datetime.timedelta(days=1)
#     if len(fridays) == 3:
#         break
# print(fridays)

# Write a python function that takes nothing but returns the datetime object of last Friday


# def get_last_friday() -> datetime.date:
#     friday = datetime.date.today()
#     while True:
#         if friday.weekday() == 4:
#             return friday
#         else:
#             friday = friday - datetime.timedelta(days=1)
#             continue


# print(get_last_friday())

# Write a Python program to get the last day of a specified year and month, Example: Monday, Tuesday etc.


# def get_last_day(year: int, month: int) -> str:
#     max_days = calendar.monthrange(year, month)[1]
#     day = datetime.date(year, month, max_days).strftime("%A")
#     return day


# print(get_last_day(2023, 4))


# Write a terminal program that required user to login.
# If user does not have an account he should register.
# credentials are username and password.
# Store the information in the file txt or pickle.
# Validate user credentials from the file.
# Once user has logged in: print text: "Hello, <username>".


while True:
    first_user_answer = input("Do you have an account?(Yes/No): ").strip().lower()
    if first_user_answer != "yes" and first_user_answer != "no":
        print("You must type yes or no")
        continue
    else:
        break
if first_user_answer == "yes":
    print("Stop lying this is a new app, no one has made any accounts :)")
    while True:
        second_user_answer = (
            input("Do you want to register an account?(Yes/No): ").strip().lower()
        )
        if second_user_answer != "yes" and second_user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            break
    if second_user_answer == "yes":
        pass
    if second_user_answer == "no":
        print("Why are you even here then?")
if first_user_answer == "no":
    while True:
        second_user_answer = (
            input("Do you want to register an account?(Yes/No): ").strip().lower()
        )
        if second_user_answer != "yes" and second_user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            break
    if second_user_answer == "yes":
        username = input("Enter the username you want to use: ").strip()
        password = input("And your password: ")
        print("not implemented yet")
    if second_user_answer == "no":
        print("Why are you even here then?")
