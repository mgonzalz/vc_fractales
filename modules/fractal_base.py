from abc import ABC, abstractmethod

class Fractal(ABC):
    def __init__(self, width, height, max_iter):
        self.width = width
        self.height = height
        self.max_iter = max_iter
    @abstractmethod
    def generate(self):
        pass
    @abstractmethod
    def plot(self, fractal):
        pass
