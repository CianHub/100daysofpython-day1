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

print(christmas)
