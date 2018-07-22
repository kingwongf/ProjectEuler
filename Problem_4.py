import numpy as np
import time

start = time.time()
hold =[]
ans =[]
for i in range(100,1000):
    for j in range(100,1000):
        num = str(i*j)
        if num == num[::-1]:
            ans.append(i*j)
            hold.append([i,j])

print(max(ans))
print((time.time() - start))