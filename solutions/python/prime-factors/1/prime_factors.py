sieve = bytearray(b"\xFF") * ((447457 + 7) // 8)
for i in range(447457):
    if not (sieve[i // 8] & (1 << i % 8)): continue
    p = 2 * i + 3
    if p * p > 894916: break
    for k in range((p * p - 3) // 2, 447457, p): sieve[k // 8] &= ~(1 << k % 8)
PRIME_LIST = [2] + [2 * i + 3 for i in range(447457) if sieve[i // 8] & (1 << i % 8)]


def factors(value):
    FACTOR = []
    while value % 2 == 0:
        FACTOR.append(2)
        value //= 2
        if value == 1: return FACTOR
    NEEDED_PRIME_LIST = PRIME_LIST[:value//2]
    for prime in NEEDED_PRIME_LIST:
        if prime > int(value**0.5) + 1: break
        if prime > value: break
        while value % prime == 0:
            FACTOR.append(prime)
            value //= prime
            if value == 1: return FACTOR
    if value > 1: FACTOR.append(value)
    return FACTOR
