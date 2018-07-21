import numpy as np

num =100

list_sumofsquares = np.sum(np.square(np.arange(1,num+1)))

list_squareofsum = np.square(np.sum((np.arange(1,num+1))))

print(list_squareofsum - list_sumofsquares)
