'''
Escape-time Mandelbrot set
'''
import time
# import warnings
# warnings.filterwarnings("ignore")
from mandelbrot import MandelbrotSetEscape
mandelbrot_set = MandelbrotSetEscape(max_iterations=30)

width, height = 512, 512
scale = 0.0075
GRAYSCALE = "L"

from PIL import Image
image = Image.new(mode=GRAYSCALE, size=(width, height))
exec_start_time = time.time()
for y in range(height):
	for x in range(width):
		c = scale * complex(x - width / 2, height / 2 - y)
		instability = 1 - mandelbrot_set.stability(c)
		image.putpixel((x, y), int(instability * 255))
exec_stop_time = time.time()

print("Execution Time: ",exec_stop_time - exec_start_time)
image.show()
