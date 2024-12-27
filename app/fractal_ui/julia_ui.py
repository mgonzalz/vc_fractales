from app.fractal_ui.base import BaseFractalUI
from modules.fractal_types.julia import Julia
from tkinter import ttk

class JuliaUI(BaseFractalUI):
    def create_fields(self, parent_frame):
        self.create_common_fields(parent_frame)
        ttk.Label(parent_frame, text="Constante (para Julia):").grid(row=8, column=0, padx=10, pady=10, sticky="w")
        self.entry_c = ttk.Entry(parent_frame)
        self.entry_c.insert(0, "-0.7+0.27015j")
        self.entry_c.grid(row=8, column=1, padx=10, pady=10, sticky="ew")

    def get_fractal(self, width, height, max_iter):
        params = self.get_common_params()
        params["c"] = complex(self.entry_c.get())
        return Julia(width, height, max_iter, **params)
