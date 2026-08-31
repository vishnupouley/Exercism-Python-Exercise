import re
def is_valid(isbn):
    if len(isbn.replace("-", "")) == 10:
        if not (isbn.replace("-", "")[:9].isnumeric() or isbn.replace("-", "").isnumeric()): return False
        if len(re.sub(r'[^0-9X]', '', isbn)) == 10: return sum((index + 1) * num for index, num in enumerate([int(i) if i.isnumeric() else 10 for i in re.sub(r'[^0-9X]', '', isbn)][::-1])) % 11 == 0
    return False