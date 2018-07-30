from euclidean_algorithm import gcd

a, b = map(int, input().split())
c, d = map(int, input().split())
gcd = gcd(b * d, a * d + b * c)
print(a * d + b * c // gcd, b * d // gcd)
