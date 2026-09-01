def find(search_list, value):
    length = len(search_list)
    if length == 1 or (length and search_list[0] == value): return 0
    n = length // 2
    for _ in range(length):
        if search_list[n] == value: return n
        n = n - n // 2 if search_list[:n][-1] > value else n + (n // 2)
        if n == 0 or n > length: break
    raise ValueError("value not in array")