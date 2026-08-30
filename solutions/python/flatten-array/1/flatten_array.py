def flatten(iterable):
    iterable = ''.join(str(iterable).split()).replace(']', '').replace('[', '')
    return [int(item) for item in iterable.split(',') if item != 'None'] if iterable else []
