ROMAN = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40 : 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D' ,900: 'CM', 1000: 'M'}

def roman(number):
    roman = ""
    for place in [1000, 100, 10, 1]:
        div = number // place
        roman += ROMAN[div * place] if ROMAN.get(div * place, False) else ROMAN[place] * div if div < 5 else ROMAN[place * 5] + ROMAN[place] * (div - 5)
        number %= place
    return roman
