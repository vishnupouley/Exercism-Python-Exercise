def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    aliquot_sum = 0
    if number <= 0: raise ValueError("Classification is only possible for positive integers.")
    for i in range(1, number//2 + 1):
        if not number % i:
            aliquot_sum += i
            if aliquot_sum > number: return 'abundant'
        else:
            i += i
    return 'perfect' if aliquot_sum == number else 'deficient'
