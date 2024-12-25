from ..fractal_base import Fractal
import numpy as np
import matplotlib.pyplot as plt

class Sierpinski(Fractal):
    def __init__(self, width, height, max_iter, depth):
        super().__init__(width, height, max_iter)
        self.depth = depth # Profundidad de la figura.

    def generate(self):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.axis('off')
        p1 = np.array([0, 0])
        p2 = np.array([1, 0])
        p3 = np.array([0.5, np.sqrt(3)/2])
        self._sierpinski_triangle(ax, p1, p2, p3, self.depth)
        plt.show()

    def _sierpinski_triangle(self, ax, p1, p2, p3, depth):
        if depth == 0:
            ax.fill([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], "black")
        else:
            mid1 = (p1 + p2) / 2
            mid2 = (p2 + p3) / 2
            mid3 = (p3 + p1) / 2
            self._sierpinski_triangle(ax, p1, mid1, mid3, depth-1)
            self._sierpinski_triangle(ax, mid1, p2, mid2, depth-1)
            self._sierpinski_triangle(ax, mid3, mid2, p3, depth-1)

    def plot(self, fractal):
        pass  # Automaticamente generado con MatplotLib.
