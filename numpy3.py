# indexing in numpy
import numpy as np

# An exemplar array
arr = np.array([[-1, 2, 0, 4],
				[4, -0.5, 6, 0],
				[2.6, 0, 7, 8],
				[3, -7, 4, 2.0]])
print(arr.flatten())
# Slicing array
temp = arr[:4, :3]
# temp = arr[::2, ::3]
print ("Array with first 2 rows and alternate columns(0 and 2):\n", temp)

# Integer array indexing example
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]                             # ?????
print ("\nElements at indices (0, 3), (1, 2), (2, 1), (3, 0):\n", temp)

# boolean array indexing example
cond = arr >= 1 # cond is a boolean array
temp = arr[cond]
print ("\nElements greater than 0:\n", temp)
                                                                                             