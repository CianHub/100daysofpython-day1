from datetime import datetime
from datetime import date

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
