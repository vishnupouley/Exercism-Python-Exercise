def convert(number: int) -> str:
    return ''.join(sound for divisor, sound in {3: 'Pling', 5: 'Plang', 7: 'Plong'}.items() if number % divisor == 0) or str(number)