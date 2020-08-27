# Calculate pi using random numbers in a square

import numpy as np

# Calculate the distance from origin in the first quadrant
def coord():
    distance  = np.sqrt(np.random.rand() ** 2 + np.random.rand() ** 2)
    return distance

outside = 0
inside = 0

# Plot numbers in or outside of circle
for n in range(1000000):
    if coord() > 1:
        outside += 1
    else:
        inside += 1

# Get the relation between points inside and points in total, then multiply by 4 to get an approximation of pi
print(inside / (outside + inside) * 4)
