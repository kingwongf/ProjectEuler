import numpy as np
a = [0]*16

a[1] = [75]
a[2] = [95, 64]
a[3] = [17, 47, 82]
a[4] = [18, 35, 87, 10]
a[5] = [20, 4, 82, 47, 65]
a[6] = [19, 1, 23, 75, 3, 34]
a[7] = [88, 2, 77, 73, 7, 63, 67]
a[8] = [99, 65, 4, 28, 6, 16, 70, 92]
a[9] = [41, 41, 26, 56, 83, 40, 80, 70, 33]
a[10] = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
a[11] = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
a[12] = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
a[13] = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
a[14] = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
a[15] = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]


# def parse(array):
#     if len(array) < 15:
#     #     nex_list =[]
#         hold = []
#
#     while len(array) > 1:
#         for ix in range(len(array[len(array)])-1):
#
#             if int(array[len(array)][ix]) > int(array[len(array)][ix+1]):
#
#                 hold.append(int(array[len(array)][ix]))
#             else:
#                 hold.append(int(array[len(array)][ix+1]))
#                 np.array(hold)
#         # print(hold)
#         print(hold + np.array(array[len(array)-1]))
#         hold = parse(hold + array[len(array)-1])
#     return hold


def parse(array):
    if len(array) == 1:
        return array
    if len(array) == 16:
        i = len(array[len(array)-1])
        print(i)
        hold =[]
    if len(array) < 16:
        i = len(array)
        # print(len(array[i]))
        hold = []

    for ix in range(i):
        if int(array[i][ix]) > int(array[i][ix+1]):
            hold.append(int(array[i][ix]))
        else:
            hold.append(int(array[i][ix+1]))
        # print(hold)
        print(hold + np.array(array[i-1]))
        hold = parse(hold + array[i-1])
    return hold

parse(a)
