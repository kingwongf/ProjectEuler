import numpy as np

def checkifprime(num):
    for i in range(2, int(np.sqrt(num))+1):
        if num%i ==0:
            return False
    return True

def nthPrime(num):
    count =0
    prime = 1

    while count < num:
        prime+=1
        if checkifprime(prime):
            count +=1
    return prime
print(nthPrime(10001))



