from app.fractal_ui.base import BaseFractalUI
from modules.fractal_types.mandelbrot import Mandelbrot

class MandelbrotUI(BaseFractalUI):
    def create_fields(self, parent_frame):
        self.create_common_fields(parent_frame)

    def get_fractal(self, width, height, max_iter):
        params = self.get_common_params()
        return Mandelbrot(width, height, max_iter, **params)
