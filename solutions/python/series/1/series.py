def slices(series, length):
    if length > 0 and series:
        if length > len(series):
            raise ValueError("slice length cannot be greater than series length")
        i, slice_list = 0, []
        try:
            while series[length - 1]:
                word = ""
                for k in range(i, length, 1):
                    word += series[k]
                slice_list.append(word)
                length += 1
                i += 1                
        except IndexError:
            return slice_list
    else:
        raise ValueError("slice length cannot be zero") if not length else ValueError("slice length cannot be negative") if length < 0 else ValueError("series cannot be empty")
