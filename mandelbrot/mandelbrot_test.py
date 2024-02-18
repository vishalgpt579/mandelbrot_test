import matplotlib.pyplot as plt
import numpy as np
import time
import warnings
warnings.filterwarnings("ignore")

'''
Reference https://realpython.com/mandelbrot-set-python/
'''


def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
	re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
	im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
	return re[np.newaxis, :] + im[:, np.newaxis] * 1j

def is_stable(c, num_iterations):
	z = 0
	for _ in range(num_iterations):
		z = z ** 2 + c
	return abs(z) <= 2

def get_members(c, num_iterations):
	mask = is_stable(c, num_iterations)
	return c[mask]

def main():
	
	convert_start_time = time.time()
	c = complex_matrix(-2, 1,-1.5, 1.5, pixel_density=512)
	convert_stop_time = time.time()
	print("No of iterations: ", c.size)

	start_time = time.time()
	members = get_members(c, num_iterations=30)
	stop_time = time.time()

	print("Transformation Overhead: ", convert_stop_time - convert_start_time)
	print("Execution Time: ",stop_time-start_time)
	print("members in mandelbrot set: ",members.shape)
	plt.scatter(members.real, members.imag, color="black", marker=",", s=1)
	plt.gca().set_aspect("equal")
	plt.axis("off")
	plt.tight_layout()
	plt.show()


if __name__ == '__main__':
	main()