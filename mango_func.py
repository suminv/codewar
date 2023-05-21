def mango(quantity, price):
    """ 8kyu Price of Mangoes"""
    return (quantity - quantity // 3) * price


assert (mango(3, 3)) == 6
assert (mango(9, 5)) == 30
