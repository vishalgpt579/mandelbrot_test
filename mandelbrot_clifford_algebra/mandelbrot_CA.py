import clifford as cf
import numpy as np
import matplotlib.pyplot as plt
import time
import warnings
warnings.filterwarnings("ignore")
import galgebra
from sympy import symbols

layout, blades = cf.Cl(2)
locals().update(blades)


def real_matrix(xmin, xmax, ymin, ymax, pixel_density):
	re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
	im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
	return re[np.newaxis, :] * e1 + im[:, np.newaxis] * e2

def is_stable(c, num_iterations):
	X = 0*e1+0*e2
	for _ in range(num_iterations):
		X = X*e1*X + c
	return abs(X) <= 4

def get_members(c, num_iterations):
	mask = is_stable(c, num_iterations)
	return c[mask]


def main():
	
	# c = -0.17578125*e1-1.0751953125*e2 #this point converges
	convert_start_time = time.time()
	c = real_matrix(-2, 1,-1.5, 1.5, pixel_density=512)
	convert_stop_time = time.time()
	print("No of iterations: ", c.size)

	exec_start_time = time.time()
	members = get_members(c, num_iterations=30) 
	exec_stop_time = time.time()

	print("Transformation Overhead: ", convert_stop_time - convert_start_time)
	print("Execution Time: ",exec_stop_time - exec_start_time)
	members_coeff = members.value
	# print(members_coeff[0:5,:])
	# print(members_coeff[0:5,1])
	plt.scatter(members_coeff[:,1].flatten(),members_coeff[:,2].flatten(), color="black", marker=",", s=1)
	plt.gca().set_aspect("equal")
	plt.axis("off")
	plt.tight_layout()
	plt.show()

if __name__ == '__main__':
	main()
