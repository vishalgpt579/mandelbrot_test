import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import clifford as cf
layout, blades = cf.Cl(3)
locals().update(blades)
import warnings
warnings.filterwarnings('ignore')

def vector_set(xmin, xmax, ymin, ymax, zmin, zmax, pixel_density):
    # Define the ranges and intervals for x, y, and z axes
    # x_range = np.arange(xmin, xmax, 0.1)*e1
    # y_range = np.arange(ymin, ymax, 0.1)*e2
    # z_range = np.arange(zmin, zmax, 0.1)*e3
    x_range = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))*e1
    y_range = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))*e2
    z_range = np.linspace(zmin, zmax, int((ymax - ymin) * pixel_density))*e3

    # Create the mesh grid for x, y, and z axes
    X, Y, Z = np.meshgrid(x_range, y_range, z_range, indexing='ij')

    # Combine the mesh grids into a single 3D array
    coords_3d = np.stack((X+Y+Z), axis=-1)

    return coords_3d


def is_stable(c, num_iterations):
    X = 0*e1+0*e2+0*e3
    for _ in range(num_iterations):
        X = X*e1*X + c
    return abs(X) <= 4

def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]


def main():
    
    # c = -0.17578125*e1-1.0751953125*e2 #this point converges
    convert_start_time = time.time()
    c = vector_set(-2, 1,-1.5, 1.5,-1,2,pixel_density=15)
    convert_stop_time = time.time()
    print("No of iterations: ", c.size)
    # print(c)

    exec_start_time = time.time()
    mandelbrot_set  = get_members(c, num_iterations=30) 
    exec_stop_time = time.time()

    print("Transformation Overhead: ", convert_stop_time - convert_start_time)
    print("Execution Time: ",exec_stop_time - exec_start_time)
    members_coeff = np.asarray([vector.value for vector in mandelbrot_set])
    # print(members_coeff[0:5,:])
    # print(members_coeff)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(members_coeff[:,1].flatten(),members_coeff[:,2].flatten(),members_coeff[:,3].flatten(), c='b', marker='o')

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('3D Plot of Cube Points')
    plt.show()

if __name__ == '__main__':
    main()