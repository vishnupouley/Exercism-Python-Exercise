def square(number: int) -> int:
    if 1 <= number <= 64: return 2**(number - 1)
    raise ValueError("square must be between 1 and 64") 


def total() -> int:
    return (1 << 64) - 1
