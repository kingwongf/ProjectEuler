# def recursive_collatz(n):
#     if n in collatz_map:
#         return collatz_map[n]
#     if n % 2 == 0:
#         x = 1 + recursive_collatz(int(n / 2))
#     else:
#         x = 1 + recursive_collatz(int(3 * n + 1))
#     collatz_map[n] = x
#     return x
#
# largest_so_far = 1
# highest = 0
#
# collatz_map = {1:1}
# for i in range(1,1000000):
#     temp = recursive_collatz(i)
#     if temp > largest_so_far:
#         highest = i
#         largest_so_far = temp

# print(highest, largest_so_far)

import sys
sys.setrecursionlimit(1500)
def recursive_collatz(num):
    if num in collatz_map:
        return collatz_map[num]
    if num % 2 ==0:
        count = 1 + recursive_collatz(int(num/2))
    else:
        count = 1 + recursive_collatz(int(num*3 +1))
    collatz_map[num] = count
    return count

largest_count = 1
highest_number = 0

collatz_map = {1:1}

for t in range(0,1000000):
    current_count = recursive_collatz(t)
    if current_count > largest_count:
        highest = t
        largest_count = current_count

print(largest_count, highest_number)