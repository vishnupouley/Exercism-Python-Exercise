def primes(limit):
    if limit < 3:
        return [] if limit == 1 else [2]
    loop_range = (limit - 1) // 2
    sieve = bytearray(b"\xFF") * ((loop_range + 7) // 8)
    for i in range(loop_range):
        if not (sieve[i // 8] & (1 << i % 8)): continue
        p = 2 * i + 3
        if p * p > limit: break
        for k in range((p * p - 3) // 2, loop_range, p): 
            sieve[k // 8] &= ~(1 << k % 8)
    return [2] + [2 * i + 3 for i in range(loop_range) if sieve[i // 8] & (1 << i % 8)]
