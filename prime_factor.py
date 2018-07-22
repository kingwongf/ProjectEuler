import numpy as np

def prime_factor(num):
    factors = [1]

    for i in range(2,int(num)):
        if num%i ==0 and i not in factors:
            factors.append(i)
            num = num/i
            prime_factor(num)
        else:
            return factors

print(prime_factor(44))