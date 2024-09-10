import datetime
def get_week_number(year, month, day):
    date = datetime.datetime(year, month, day)
    return date.isocalendar()[1]
year = 2015
month = 6
day = 16
week_number = get_week_number(year, month, day)
print("Week number:", week_number)