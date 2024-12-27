# Cuando se quiera añadir uno, se debe de poner en esta lista.
from app.fractal_ui.julia_ui import JuliaUI
from app.fractal_ui.mandelbrot_ui import MandelbrotUI
from app.fractal_ui.sierpinski_ui import SierpinskiUI

fractals = {
        "mandelbrot": MandelbrotUI(),
        "julia": JuliaUI(),
        "sierpinski": SierpinskiUI()
    }
