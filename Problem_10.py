import numpy as np
def checkprime(num):
    for i in range(2,int(np.sqrt(num))+1):
        if num%i == 0:
            return False
    return True
prime =[]
for x in range(1,2000001):
    if checkprime(x):
        print(x)
        prime.append(x)

print(np.sum(prime)-1)