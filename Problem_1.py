import numpy as np

number = 1000
list =[]
for i in range(0,number):
    if i%3 ==0 or i%5==0:
        list.append(i)
print(np.sum(list))
