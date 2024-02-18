import clifford as cf
from PIL import Image
import time
import warnings
# import galgebra
# warnings.filterwarnings("ignore")

layout, blades = cf.Cl(2)
locals().update(blades)

max_iterations = 30

def stability(c):
    return escape_count(c) / max_iterations

def escape_count(c):
    X = 0*e1+0*e2
    for iteration in range(max_iterations):
        X = X*e1*X + c
        if abs(X) >= 4:
            return iteration
    return max_iterations

width, height = 512, 512
scale = 0.0075
GRAYSCALE = "L"


image = Image.new(mode=GRAYSCALE, size=(width, height))
exec_start_time = time.time()
for y in range(height):
	for x in range(width):
		c = scale * ((x - width / 2)*e1 + (height / 2 - y)*e2)
		instability = 1 - stability(c)
		image.putpixel((x, y), int(instability * 255))
exec_stop_time = time.time()

print("Execution Time: ",exec_stop_time - exec_start_time)
image.show()