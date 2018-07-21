import numpy as np

num = 4000000
fib_list = []
a = 1
fib_list.append(a)
fib_list.append(a)


while fib_list[-1] <= num:
    fib_list.append(fib_list[-2] + fib_list[-1])

print(fib_list)

hold = []
for i in fib_list:
    if i%2 ==0 and i < num:
        hold.append(i)
print(np.sum(hold))