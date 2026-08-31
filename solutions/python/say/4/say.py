ref = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

def say(num):
    if not 0 <= num < 1e12: raise ValueError("input out of range")
    return ref[num] if num < 20 else\
           (f"{ref[num // 10 * 10]}-{ref[num % 10]}" if num % 10 else ref[num]) if num < 100 else \
           f"{say(num // 100)} hundred{' '  + say(num % 100) if num % 100 else ''}" if num < 1e3 else \
           f"{say(num // 1e3)} thousand{' ' + say(num % 1e3) if num % 1e3 else ''}" if num < 1e6 else \
           f"{say(num // 1e6)} million{' '  + say(num % 1e6) if num % 1e6 else ''}" if num < 1e9 else \
           f"{say(num // 1e9)} billion{' '  + say(num % 1e9) if num % 1e9 else ''}"
           
# Kudoos to this solution from aevinquorath