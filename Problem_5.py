import numpy as np

i = 2520

while np.sum(i%np.arange(1,21) ==0) != 20:
    i += 2520
    print(i)
else:
    print(i)
