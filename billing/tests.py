from django.test import TestCase

import datetime
import calendar


date = datetime.date.today()
due_date = date.replace(
  month = date.month + 1,
  day = date.day
)


left = due_date - date
days = str(left).split(",")[0]


       # month range
mon = date.month
print(date)

year = date.year 
print(year)
x = calendar.monthrange(year, mon)
print(x)

todaymin = datetime.datetime.combine(datetime.date.today(),datetime.time.min)
month  = date.replace(
  month = date.month,
  day = 1 )
print(month) 
date = datetime.date.today() 
def last_day_of_month(date):
    # this will never fail
    # get close to the end of the month for any day, and add 4 days 'over'
    next_month = date.replace(day=28) + datetime.timedelta(days=4)
    # subtract the number of remaining 'overage' days to get last day of current month, or said programattically said, the previous day of the first of next month
    return next_month - datetime.timedelta(days=next_month.day)
    



print(datetime.timedelta(days=4))

next_month = date.replace(day=28) + datetime.timedelta(days=4)
x = next_month - datetime.timedelta(days=next_month.day)

print(x)


x ='sarvan'
y ='c.m'
z = x+" "+y
print(z)