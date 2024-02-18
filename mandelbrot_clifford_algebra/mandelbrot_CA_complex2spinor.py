'''
reference: https://clifford.readthedocs.io/en/latest/tutorials/InterfacingOtherMathSystems.html
'''
import clifford as cf
import numpy as np
import matplotlib.pyplot as plt
import time
import warnings
warnings.filterwarnings("ignore")
import galgebra
from sympy import symbols

layout, blades = cf.Cl(2) # instantiate a 2D- GA
locals().update(blades) # put all blades into local namespace

def c2s(z):
    '''convert a complex number to a spinor'''
    return z.real + z.imag*e12

def s2c(S):
    '''convert a spinor to a complex number'''
    S0 = float(S(0))
    S2 = float(-S|e12)
    return S0 + S2*1j

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
	re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
	im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
	return re[np.newaxis, :] + im[:, np.newaxis] * 1j

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
	c = c2s(complex_matrix(-2, 1,-1.5, 1.5, pixel_density=15))
	convert_stop_time = time.time()
	print("No of iterations: ", c.size)

	exec_start_time = time.time()
	members = get_members(c, num_iterations=30) 
	exec_stop_time = time.time()

	
	# members_coeff = members.value
	print("Spinor members: ",members)

	# reconvert_start_time = time.time()
	# members = s2c(members)
	# reconvert_stop_time = time.time()
	# print("Complex members: ",members)
	# print("Total no of members: ",members.shape)

	# print("Transformation Time: ",convert_stop_time - convert_start_time)
	# print("Execution Time: ",exec_stop_time - exec_start_time)
	# print("Inverse-Transformation Time: ",reconvert_stop_time - reconvert_start_time)

	# print(members_coeff[0:5,:])
	# print(members_coeff[0:5,1])
	# plt.scatter(members_coeff[:,1].flatten(),members_coeff[:,2].flatten(), color="black", marker=",", s=1)
	# plt.gca().set_aspect("equal")
	# plt.axis("off")
	# plt.tight_layout()
	# plt.show()

if __name__ == '__main__':
	main()
