def sieve(n):
    is_prime = [True] * (n + 1)
    primes = []
    for d in range(2, n + 1):
        if is_prime[d]:
            primes.append(d)
            for i in range(d * d, n + 1, d):
                is_prime[i] = False
    return is_prime[n]


n = int(input())
print(sieve(n))
