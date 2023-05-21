def is_today(date):
    return date.date() == datetime.today().date()


assert is_today(datetime(2020, 10, 1, 1, 1, 1, 1)) == False
