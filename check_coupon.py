from datetime import datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    date1 = datetime.strptime(current_date, '%B %d, %Y')
    date2 = datetime.strptime(expiration_date, '%B %d, %Y')

    if entered_code is correct_code and date1 <= date2:
        return True

    return False


assert check_coupon('123', '123', 'September 5, 2014', 'October 1, 2014') == True
assert check_coupon('123a', '123', 'September 5, 2014', 'October 1, 2014') == False
