def steps(number: int) -> int:
    if number < 1: raise ValueError("Only positive integers are allowed")
    if number < 3: return 0 if number == 1 else 1
    i = 0
    while number > 1:
        number = number / 2 if not number % 2 else (number * 3) + 1
        i += 1
    return i
