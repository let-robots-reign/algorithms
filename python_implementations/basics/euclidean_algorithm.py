def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def recursive_gcd(a, b):
    if b == 0:
        return a
    return recursive_gcd(b, a % b)
