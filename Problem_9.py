import numpy as np



for a in range(0,999):
    for b in range(0,999):
        if a**2 + b**2 == (1000-a-b)**2 and 1000 - a - b > 0:
            print(a*b*(1000-a-b))
