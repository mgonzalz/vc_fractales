import sv_ttk # Theme: https://github.com/rdbende/Sun-Valley-ttk-theme
import tkinter as tk
from tkinter import ttk, messagebox
from app.types_fractals import fractals


class FractalApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Generador de Fractales")
        # Logo path: app/assets/fractal_icon.ico
        logo_path = "app/assets/fractal_icon.ico"
        self.root.iconbitmap(logo_path)

        sv_ttk.set_theme("dark")
        self.fractal_uis = fractals

        self._initialize_ui()

    def _initialize_ui(self):
        main_frame = ttk.Frame(self.root, padding=(20, 20, 20, 20))
        main_frame.grid(row=0, column=0, sticky="nsew")

        # Fractal type selection.
        ttk.Label(main_frame, text="Tipo de Fractal:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.fractal_type_var = tk.StringVar(value="mandelbrot")
        fractal_menu = ttk.Combobox(main_frame, textvariable=self.fractal_type_var, values=list(self.fractal_uis.keys()), state="readonly")
        fractal_menu.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.fractal_type_var.trace("w", self._switch_fields)

        # Width and Height.
        ttk.Label(main_frame, text="Ancho:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_width = ttk.Entry(main_frame)
        self.entry_width.insert(0, "1000")
        self.entry_width.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        ttk.Label(main_frame, text="Alto:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_height = ttk.Entry(main_frame)
        self.entry_height.insert(0, "1000")
        self.entry_height.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        # Maximum Iterations.
        ttk.Label(main_frame, text="Iteraciones Máximas:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_max_iter = ttk.Entry(main_frame)
        self.entry_max_iter.insert(0, "200")
        self.entry_max_iter.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        # Placeholder for specific fields.
        self.specific_frame = ttk.Frame(main_frame)
        self.specific_frame.grid(row=4, column=0, columnspan=2, sticky="ew")

        # Generate button.
        generate_button = ttk.Button(main_frame, text="Generar Fractal", command=self._generate_fractal)
        generate_button.grid(row=10, column=0, columnspan=2, pady=20)

        # Initialize specific fields.
        self._switch_fields()

    def _generate_fractal(self):
        fractal_ui = self.fractal_uis[self.fractal_type_var.get()]
        try:
            width = int(self.entry_width.get())
            height = int(self.entry_height.get())
            max_iter = int(self.entry_max_iter.get())

            fractal = fractal_ui.get_fractal(width, height, max_iter)
            data = fractal.generate()
            fractal.plot(data)
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

    def _switch_fields(self, *args):
        for widget in self.specific_frame.winfo_children():
            widget.destroy()
        fractal_ui = self.fractal_uis[self.fractal_type_var.get()]
        fractal_ui.create_fields(self.specific_frame)

    def run(self):
        self.root.mainloop()
