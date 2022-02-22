import numpy as np

print("array from set",np.array({12,54,68}))

print("array from list:",np.array([[1, 5, 8], [24, 35, 63]]))

print("array from tuple:", np.array((57,5)))

# intrinsic numpy array creation  objects (eg. arange, ones, zeros, etc.)
zeros = np.zeros((5,3))
print(zeros, zeros.dtype, zeros.shape)
ones = np.ones((4,3))
print(ones,ones.dtype)
      
rg = np.arange(10)           
print(rg, type(rg))

lspace = np.linspace(1,5,12)
print(lspace)

