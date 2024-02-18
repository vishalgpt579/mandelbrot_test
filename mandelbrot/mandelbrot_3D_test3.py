import numpy as np
import quaternion
import time
import warnings
warnings.filterwarnings('ignore')

# def sequence(c):
# 	z = np.quaternion(0, 0, 0, 0)
# 	while True:
# 		yield z
# 		z = np.add(z*z,c)
# c = np.random.rand
# for n, z in enumerate(sequence(c=c)):
# 	print(f"z({n}) = {z}")
# 	if n >= 9:
# 		break

def quaternion_set(xmin, xmax, ymin, ymax, zmin, zmax, pixel_density):
    x_range = np.arange(xmin, xmax, int((xmax - xmin) * pixel_density))
    y_range = np.arange(ymin, ymax, int((ymax - ymin) * pixel_density))
    z_range = np.arange(zmin, zmax, int((zmax - zmin) * pixel_density))
    
    # Create the mesh grid for x, y, and z axes
    X, Y, Z = np.meshgrid(x_range, y_range, z_range, indexing='ij')

    # Combine the mesh grids into a single 3D array
    coords_3d = np.stack((X, Y, Z), axis=-1)

    # Flatten the 3D array to visualize as points
    points = coords_3d.reshape((-1, 3))
    points = np.column_stack((np.zeros(points.shape[0]),points))
    print(points[0:5])
    quaternion_array = quaternion.from_float_array(points)
    print(quaternion_array[0:5])

    return quaternion_array


def is_stable(c, num_iterations):
    z = np.quaternion(0, 0, 0, 0)
    for _ in range(num_iterations):
        z = z*z + c
    return abs(z) <= 2

def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]

def main():
    
    # c = -0.17578125*e1-1.0751953125*e2 #this point converges
    convert_start_time = time.time()
    qs = quaternion_set(-2, 1,-1.5, 1.5,-1,2, pixel_density=15)
    convert_stop_time = time.time()
    print("No of iterations: ", qs.size)

    exec_start_time = time.time()
    members = get_members(qs, num_iterations=30) 
    exec_stop_time = time.time()

    print("Transformation Overhead: ", convert_stop_time - convert_start_time)
    print("Execution Time: ",exec_stop_time - exec_start_time)
    print("Mandelbrot set: ",members)
    # members_coeff = members.value
    # print(members_coeff[0:5,:])
    # print(members_coeff[0:5,1])
    # plt.scatter(members_coeff[:,1].flatten(),members_coeff[:,2].flatten(), color="black", marker=",", s=1)
    # plt.gca().set_aspect("equal")
    # plt.axis("off")
    # plt.tight_layout()
    # plt.show()

    # plt.scatter(points[:, 0], points[:, 1], points[:, 2], c='b', marker='o')

    # ax.set_xlabel('X-axis')
    # ax.set_ylabel('Y-axis')
    # ax.set_zlabel('Z-axis')
    # ax.set_title('3D Plot of Cube Points')


if __name__ == '__main__':
    main()

