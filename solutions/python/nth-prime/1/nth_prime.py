def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
    prime, i = [2], 3
    while len(prime) != number:
        if not any(i % p == 0 for p in prime):
            prime.append(i)
        i += 2
    return prime[number - 1]
