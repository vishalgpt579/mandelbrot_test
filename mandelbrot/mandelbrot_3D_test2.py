import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

# Define the ranges and intervals for x, y, and z axes
x_range = np.arange(-2, 1.5, 0.5)
y_range = np.arange(-1.5, 1.6, 0.5)
z_range = np.arange(-1, 2.5, 0.5)

# Create the mesh grid for x, y, and z axes
X, Y, Z = np.meshgrid(x_range, y_range, z_range, indexing='ij')

# Combine the mesh grids into a single 3D array
coords_3d = np.stack((X, Y, Z), axis=-1)

# Flatten the 3D array to visualize as points
points = coords_3d.reshape((-1, 3))

print("3D points ...")
print(points[0:5])
# # Plotting
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='b', marker='o')

# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')
# ax.set_title('3D Plot of Cube Points')

# plt.show()

import quaternion
points = np.column_stack((np.zeros(points.shape[0]),points))
quaternion_array = quaternion.from_float_array(points)

# Display the quaternion array
print("\nQuaternion representation of points:")
print(quaternion_array[0:5])


max_iterations = 30

def is_stable(c):
    z = np.quaternion(0,0,0,0)
    for iteration in range(max_iterations):
        z = z*z+c
    if abs(z) <= 4:
        True
    else:
        False

exec_start_time = time.time()
for point in quaternion_array:
    if is_stable(point):
        print(point)
exec_stop_time = time.time()

print("Execution Time: ",exec_stop_time - exec_start_time)