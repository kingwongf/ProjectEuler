import numpy as np

num = 600851475143
a = 2
factor = []
while a > 1 and a <= num:
    while num % a == 0:
        factor.append(a)
        num = num/a
    a = a+1

print(factor)

def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors


pfs = prime_factors(600851475143 )

print(pfs)