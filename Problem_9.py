import numpy as np
import time

start =time.time()


for a in range(1,999):
    for b in range(1,999):
        if a**2 + b**2 == (1000-a-b)**2 and 1000 - a - b > 0:
            print(a*b*(1000-a-b))
            print((time.time() - start))

