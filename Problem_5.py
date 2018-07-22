import numpy as np
import time

start = time.time()
i = 2520

while np.sum(i%np.arange(1,21) ==0) != 20:
    i += 2520
else:
    print(i)

print((time.time() - start))