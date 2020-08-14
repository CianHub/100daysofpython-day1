from datetime import datetime
from datetime import date
from datetime import timedelta

""" Returns a datetime instance of today"""
today = datetime.today()

""" Returns todays date as a date object yyyy-mm-dd """
todays_date = date.today()

""" Can drill into date object"""
todays_month = todays_date.month
todays_day = todays_date.day
todays_year = todays_date.year

""" Create new instance of date"""
christmas = date(2020, 12, 25)

""" Can get the difference between two dates returned as a timedelta instance"""
diff = christmas - todays_date

""" Can drill into timedelta"""
number_of_days_diff = diff.days

""" use case"""
if christmas is not todays_date:
    print('Christmas is ' + str(number_of_days_diff) + ' days away')

""" Create timedelta"""
custom_timedelta = timedelta(days=4, hours=10)

""" Timedeltas only can do 1 max in seconds so will only show hours e.g. 36000"""
sec = custom_timedelta.seconds

""" Converts seconds to hours"""
print(sec / 60 / 60)

""" Can add now and a timedelta to get the datetime for when that is"""
today = datetime.today()
eta = timedelta(hours=4)
print(today + eta)
