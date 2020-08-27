# Calculate pi using random numbers in a square

import numpy as np

def coord():
    distance  = np.random.rand() ** 2 + np.random.rand() ** 2
    return distance

outside = 0
inside = 0
at = 0

for n in range(1000000):
    if coord() > 1:
        outside += 1
    else:
        inside += 1

print(inside / (outside + inside) * 4)
print(at)
