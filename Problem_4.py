import numpy as np

hold =[]
ans =[]
for i in range(100,1000):
    for j in range(100,1000):
        num = str(i*j)
        if num == num[::-1]:
            ans.append(i*j)
            hold.append([i,j])

print(max(ans), max(hold)[0]*max(hold)[1])