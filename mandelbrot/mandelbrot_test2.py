import time
import numpy as np
from mandelbrot import MandelbrotSet

mandelbrot_set = MandelbrotSet(max_iterations=30)


# def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
# 	re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
# 	im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
# 	return re[np.newaxis, :] + im[:, np.newaxis] * 1j
# start_time= time.time()
# c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=1024)
# width, height = c.shape[1],c.shape[0]

width, height = 1024,1024
scale = 0.0029296875 #0.0070
BLACK_AND_WHITE = "1"

from PIL import Image
image = Image.new(mode=BLACK_AND_WHITE, size=(width, height))
c_list = []

start_time= time.time()
for y in range(height):
	for x in range(width):
		c = scale * complex(x - width / 2, height / 2 - y)
		c_list.append(c)
		if c in mandelbrot_set:
			print("C = ",c)
		image.putpixel((x, y), c not in mandelbrot_set)

# for value in np.nditer(c):
# 	image.putpixel((x, y), c not in mandelbrot_set)
stop_time= time.time()
print("No of iterations: ", len(c_list))
print("Execution Time: ", stop_time-start_time)
image.show()
