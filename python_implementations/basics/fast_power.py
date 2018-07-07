def fast_power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return fast_power(a, n // 2) ** 2
    else:
        return fast_power(a, n - 1) * a
