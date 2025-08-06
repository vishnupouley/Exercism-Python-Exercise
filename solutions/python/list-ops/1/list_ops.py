def append(list1, list2):
    return list1 + list2


def concat(lists):
    return [item for sublist in lists if sublist for item in sublist]


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    return list.index(list[-1]) + 1 if list else 0


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    if len(list):
        initial = function(initial, list.pop(0))
        return foldl(function, list, initial)
    return initial


def foldr(function, list, initial):
    if len(list):
        initial = function(initial, list.pop(-1))
        return foldr(function, list, initial)
    return initial


def reverse(list):
    return list[::-1]
