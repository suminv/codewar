def weather_info(temperature):
    c = convert_to_celsius(temperature)
    if c < 0:
        return f'{c} is freezing temperature'
    else:
        return f'{c} is above freezing temperature'
