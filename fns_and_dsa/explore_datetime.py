import datetime
from datetime import timedelta
def display_current_datetime():
    return datetime.datetime.now()
current_date = display_current_datetime()
print (current_date)
formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)
def calculate_future_date():
    number_of_days = int(input("enter a number of days: "))
    return datetime.date.today() + timedelta(days=number_of_days)
future_date = calculate_future_date().strftime("%Y-%m-%d")
print (future_date)
