import numpy as np
import time

start = time.time()
num = 600851475143
a = 2
factor = []
for i in range(100000):
    while a > 1 and a <= num:
        while num % a == 0:
            factor.append(a)
            num = num/a
        a = a+1

print(factor)
print((time.time() - start))



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

start = time.time()
for i in range(100000): pfs = prime_factors(600851475143)

print(pfs)
print((time.time() - start))