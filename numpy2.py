# array creation techniques
import numpy as np

# Creating array from list with type float
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float')
print ("Array created using passed list:\n", a)

# Creating array from tuple
b = np.array((1 , 3, 2))
print ("\nArray created using passed tuple:\n", b)

# Creating a 3X4 array with all zeros
c = np.zeros((3, 4))
print ("\nAn array initialized with all zeros:\n", c)

# Create a constant value array of complex type
d = np.full((3, 3), 6, dtype = 'complex')
print ("\nAn array initialized with all 6s. Array type is complex:\n", d)

# Create an array with random values
e = np.random.random((2, 2))
print ("\nA random array:\n", e, type(e))

# Create a sequence of integers from 0 to 30 with steps of 5
f = np.arange(0, 30, 5)
print ("\nA sequential array with steps of 5:\n", f)

# the use of index arrays.
# Create a sequence of integers from 10 to 1 with a step of -2
g = np.arange(10, 1, -2)
print("\n A sequential array with a negative step: \n",g)

# Indexes are specified inside the np.array method.
newarr = g[np.array([3, 1, 2, 4 ])]
print("\n Elements at these indices are:\n",newarr)

# Create a sequence of 10 values in range 0 to 5
h = np.linspace(1, 5, 10)
print ("\nA sequential array with 10 values between 0 and 5:\n", h)

# NumPy array with elements from 1 to 9
x = np.arange(1,10)
print(x)
# Index values can be negative.
arr = x[np.array([2, 5, -1])]
print("\n Elements are : \n",arr)


# Reshaping 3X4 array to 2X2X3 array
arr = np.array([[1, 2, 3, 4],
				[5, 2, 4, 2],
				[1, 2, 0, 1]])

newarr = arr.reshape(3, 2, 2)

print ("\nOriginal array:\n", arr)
print ("Reshaped array:\n", newarr)

# Flatten array
arr = np.array([[1, 2, 3], [4, 5, 6]])
flarr = arr.flatten()

print ("\nOriginal array:\n", arr)
print ("Flattened array:\n", flarr)
