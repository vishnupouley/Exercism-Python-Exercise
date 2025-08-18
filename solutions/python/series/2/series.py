# Solution after optimising the code from Deepseek AI
def slices(series, length):
    if not series:
        raise ValueError("series cannot be empty")
    if length <= 0:
        raise ValueError("slice length cannot be zero" if length == 0 else "slice length cannot be negative")
    series_len = len(series)
    if length > series_len:
        raise ValueError("slice length cannot be greater than series length")
    return [series[i:i+length] for i in range(series_len - length + 1)]