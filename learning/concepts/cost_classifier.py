import numpy as np
import matplotlib.pyplot as plt

# Generate two arrays of 1000
#  random float values between 0 and 1
num1 = np.random.uniform(0,1, size = 100)
num2 = np.random.uniform(0,1, size = 100)


# Find the maximum value from the concatenated array
x = np.maximum(num1,num2)

# Compute the square root of num1
y = np.sqrt(num1)

# Plot y with an array of x values
#plt.xscale("log")
#plt.yscale("log")
plt.plot(np.full(100, x), y, marker = "o", linestyle='None', color='b', label='Dotted Line')
plt.xlabel("Max value (constant)")
plt.ylabel("Square Root of num1")
plt.title("Plot of sqrt(num1) vs max value")
plt.show()