import pandas as pd
import numpy as np
filename = 'project_euler_problem13_num.txt'

with open(filename, "r") as ins:
    array = []
    for line in ins:
        array.append(int(line))
array = np.array(array).flatten()


lit = str(array)
lit = lit.replace("\n", "")
lit = lit.replace(" ", "")
lit = lit[1:-1]
print(lit)

prod = []
for i in range(0, 5000, 50):
    prod.append(int(lit[i:i+50]))
    print(int(lit[i:i+50]))
print(np.sum(prod))