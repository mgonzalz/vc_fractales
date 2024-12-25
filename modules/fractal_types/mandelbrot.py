from ..fractal_base import Fractal
import numpy as np
import matplotlib.pyplot as plt

class Mandelbrot(Fractal):
    def __init__(self, width, height, max_iter, xmin, xmax, ymin, ymax):
        super().__init__(width, height, max_iter)
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def generate(self):
        x = np.linspace(self.xmin, self.xmax, self.width)
        y = np.linspace(self.ymin, self.ymax, self.height)
        fractal = np.zeros((self.height, self.width))

        for i in range(self.height):
            for j in range(self.width):
                c = x[j] + y[i] * 1j
                fractal[i, j] = self._mandelbrot(c)
        return fractal

    def _mandelbrot(self, c):
        z = 0
        n = 0
        while abs(z) <= 2 and n < self.max_iter:
            z = z * z + c
            n += 1
        return n

    def plot(self, fractal):
        plt.figure(figsize=(10, 10))
        plt.imshow(fractal, extent=(self.xmin, self.xmax, self.ymin, self.ymax), cmap="hot")
        plt.colorbar(label="Número de iteraciones")
        plt.title("Conjunto de Mandelbrot")
        plt.xlabel("Re (eje real)")
        plt.ylabel("Im (eje imaginario)")
        plt.show()
