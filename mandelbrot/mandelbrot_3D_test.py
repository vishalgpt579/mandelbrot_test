import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the properties of the fractal
n = 8
size = 50
iterations = 30

# Create a blank 3D array for the fractal
fractal = np.zeros((size, size, size))

# Define the function for the Mandelbulb
def mandelbulb(x, y, z, n=8):
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arctan2(np.sqrt(x**2 + y**2), z)
    phi = np.arctan2(y, x)
    rn = r**n
    return rn * np.sin(n * theta) * np.cos(n * phi)

# Generate the fractal
for i in range(size):
    for j in range(size):
        for k in range(size):
            x = (i - size / 2) / (size / 4)
            y = (j - size / 2) / (size / 4)
            z = (k - size / 2) / (size / 4)
            a = x
            b = y
            c = z
            for _ in range(iterations):
                a, b, c = mandelbulb(a, b, c, n), mandelbulb(b, c, a, n), mandelbulb(c, a, b, n)
                if a**2 + b**2 + c**2 > 1000:
                    break
            else:
                fractal[i, j, k] = 1

# Plot the fractal
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(*np.where(fractal), color='k', s=1)
plt.show()
