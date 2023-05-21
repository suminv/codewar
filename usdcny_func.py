def usdcny(usd):
    """Create a function that converts US dollars (USD) to Chinese Yuan (CNY) . The input is the amount of USD as an
    integer, and the output should be a string that states the amount of Yuan followed by 'Chinese Yuan'

    """
    return f"{(usd * 6.75):.2f} Chinese Yuan"


assert usdcny(465) == "3138.75 Chinese Yuan"
