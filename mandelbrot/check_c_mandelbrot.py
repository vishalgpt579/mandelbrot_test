def fractal(n,c):
	if n==0:
		return 0
	else:
		return fractal(n-1,c)**2+c

def sequence(c):
	z = 0
	while True:
		yield z
		z = z**2 + c

def main():
	c = -1
	z = []
	for n,z in enumerate(sequence(c)):
		print(f"z({n}) = {z}")
		if n >=9:
			break

if __name__ == '__main__':
	main()