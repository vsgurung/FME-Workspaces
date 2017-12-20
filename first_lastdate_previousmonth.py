from datetime import date, datetime
from dateutil.relativedelta import relativedelta

today = date.today()

def get_first_date(in_month=1):
    """
    Takes month as parameter
    returns first date of the in_month months.
    """

    from_date = (today-relativedelta(months=in_month)).replace(day=1)
    
    return from_date

print(get_first_date(1))


def get_last_date(in_months=0,in_days=1):

    to_date = date(today.year, today.month, 1) - relativedelta(months=in_months,days=in_days)

    return to_date


print(get_last_date().strftime('%d/%m/%Y')) # get date in UK date format
