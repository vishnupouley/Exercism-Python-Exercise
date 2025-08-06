def convert(number: int) -> str:
    rain = ''
    if number % 3 == 0:
        rain += 'Pling'
    if number % 5 == 0:
        rain += 'Plang'
    if number % 7 == 0:
        rain += 'Plong'
    if len(rain) == 0:
        return str(number)
    return rain
