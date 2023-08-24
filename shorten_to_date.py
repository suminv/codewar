def shorten_to_date(long_date):
    return long_date.split(",")[0]


assert shorten_to_date("Monday February 2, 8pm") == "Monday February 2"
