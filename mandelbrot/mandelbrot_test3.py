import numpy as np
import matplotlib.pyplot as plt
from numpy import newaxis
import warnings


def compute_mandelbrot(N_max, some_threshold, nx, ny):
    # A grid of c-values
    x = np.linspace(-2, 1, nx)
    y = np.linspace(-1.5, 1.5, ny)

    c = x[:, newaxis] + 1j * y[newaxis, :]

    # Mandelbrot iteration

    z = c
    
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        for j in range(N_max):
            z = z**2 + c
        mandelbrot_set = abs(z) < some_threshold

    return mandelbrot_set


mandelbrot_set = compute_mandelbrot(30, 50.0, 5250, 5250)

plt.imshow(mandelbrot_set.T, extent=[-2, 1, -1.5, 1.5])
plt.gray()
plt.show()