# basic operations on single array

import numpy as np

a = np.array([1, 2, 5, 3])
print("\n square of a: ",a*a,"\n exponential: ",a**a, "\n double: ",a+a,"\n Give zeros: " ,a-a,"\n Give ones: ", a/a)

# add 1 to every element
print ("Adding 1 to every element:", a+1)

# subtract 3 from each element
print ("Subtracting 3 from each element:", a-3)

# multiply each element by 10
print ("Multiplying or dividing each element by 10:", a*10, a/3)

# square each element
print ("Squaring each element:", a**2)
print(a)

# modify existing array
a *= 2
print ("Doubled each element of original array:", a)

# transpose of array
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])

print ("\nOriginal array:\n", a)
print ("Transpose of array:\n", a.T)
print(a.flatten())
# print ("Flat of array:\n", a.flat)
for item in a.flat:
    print(item)

# binary operators in Numpy


b = np.array([[1, 2],
			  [3, 4]])
c = np.array([[4, 3],
			  [2, 1]])

# add arrays
print ("Array sum and sub:\n", b + c, "\n",b-c)

# multiply arrays (elementwise multiplication)
print ("Array multiplication:\n",  b*c)

# matrix multiplication
print ("Matrix multiplication:\n", b.dot(c))


# Broadcasting

a = np.array([1.0, 2.0, 3.0])

# Example 1
b = 2.0
print(a * b)

# Example 2
c = [2.0, 2.0, 2.0]
print(a * c)
print(type(c))
