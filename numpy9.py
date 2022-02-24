# universal functions in numpy  (ufunc)
import numpy as np

# create an array of sine values
a = np.array([0, np.pi/2, np.pi])
print ("Sine values of array elements:", np.sin(a))

# exponential values
a = np.array([0, 1, 2, 3])
print ("Exponent of array elements:", np.exp(a))

# square root of array values
print ("Square root of array elements:", np.sqrt(a))

# Trigonometric functions 

# create an array of angles
angles = np.array([0, 30, 45, 60, 90, 180])

# conversion of degree into radians using deg2rad function
radians = np.deg2rad(angles)

# sine of angles
print('Sine of angles in the array:')
sine_value = np.sin(radians)
print(np.sin(radians))

# inverse sine of sine values
print('Inverse Sine of sine values:')
print(np.rad2deg(np.arcsin(sine_value)))

# hyperbolic sine of angles
print('Sine hyperbolic of angles in the array:')
sineh_value = np.sinh(radians)
print(np.sinh(radians))

# inverse sine hyperbolic
print('Inverse Sine hyperbolic:')
print(np.sin(sineh_value))

# hypot function demonstration
base = 4
height = 3
print('hypotenuse of right triangle is:')
print(np.hypot(base, height))