# Stacking: Several arrays can be stacked together along different axes.

import numpy as np

a = np.array([[1, 2],
			  [3, 4]])

b = np.array([[5, 6],
			  [7, 8]])

# vertical stacking
print("Vertical stacking:\n", np.vstack((a, b)))

# horizontal stacking
print("\nHorizontal stacking:\n", np.hstack((a, b)))

c = [5, 6]

# stacking columns
print("\nColumn stacking:\n", np.column_stack((a, c)))

# concatenation method
print("\nConcatenating to 2nd axis:\n", np.concatenate((a, b), 1))



# Splitting: 


d = np.array([[1, 3, 5, 7, 9, 11],
			  [2, 4, 6, 8, 10, 12]])
print("\n",type(d), d.shape)

# horizontal splitting
print("Splitting along horizontal axis into 2 parts:\n", np.hsplit(d, 3))

# vertical splitting
print("\nSplitting along vertical axis into 2 parts:\n", np.vsplit(d, 2))