from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta


def dates():
    today=date.today()
    delta1=timedelta(days=1)
    delta30=timedelta(days=30)
    yesterday=today-delta1
    month_ago=today-relativedelta(months = 1)
    print(today)
    print(yesterday)
    print(month_ago)


def string_to_date():
    str1="01/01/17 12:10:03.234567"
    dt=datetime.strptime(str1, '%d/%m/%y %H:%M:%S.%f')
    print(dt)


dates()
string_to_date()