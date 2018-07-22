

# def count(num):
#     for i in range(num):
#         for j in range(num):
#
#         S[1][1] = S[0][0] + S[1][0]
#

# import time
#
#
# def route_num(cube_size):
#     L = [1] * cube_size
#     for i in range(cube_size):
#         for j in range(i):
#             L[j] = L[j] + L[j - 1]
#         L[i] = 2 * L[i - 1]
#     return L[cube_size - 1]
#
#
# start = time.time()
# n = route_num(5)
# elapsed = (time.time() - start)
# print("%s found in %s seconds" % (n, elapsed))


list=[1]
for i in range(10):
    print(list)
    newlist=[]
    newlist.append(list[0])
    for i in range(len(list)-1):
        newlist.append(list[i]+list[i+1])
    newlist.append(list[-1])
    list=newlist

# L = [1]*20
#
# for i in range(20):
#     for j in range(i):
#         L[j] = L[j] + L[j-1]
#     L[]
