def convert_to_celsius(temperature):
    return (temperature - 32) * (5 / 9)


assert weather_info(50) == '10.0 is above freezing temperature'
assert weather_info(23) == '-5.0 is freezing temperature'
