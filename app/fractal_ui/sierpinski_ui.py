from tkinter import ttk
from modules.fractal_types.sierpinski import Sierpinski
from app.fractal_ui.base import BaseFractalUI

class SierpinskiUI(BaseFractalUI):
    def create_fields(self, parent_frame):
        ttk.Label(parent_frame, text="Profundidad (para Sierpinski):").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.entry_depth = ttk.Entry(parent_frame)
        self.entry_depth.insert(0, "6")
        self.entry_depth.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    def get_fractal(self, width, height, max_iter):
        depth = int(self.entry_depth.get())
        return Sierpinski(width, height, max_iter, depth)
