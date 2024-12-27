import sv_ttk  # Importa el tema Sun Valley
import tkinter as tk
from tkinter import ttk, messagebox
from app.fractal_ui.julia_ui import JuliaUI
from app.fractal_ui.mandelbrot_ui import MandelbrotUI
from app.fractal_ui.sierpinski_ui import SierpinskiUI

def create_app():
    def generate_fractal():
        fractal_ui = fractal_uis[fractal_type_var.get()]
        try:
            width = int(entry_width.get())
            height = int(entry_height.get())
            max_iter = int(entry_max_iter.get())

            fractal = fractal_ui.get_fractal(width, height, max_iter)
            data = fractal.generate()
            fractal.plot(data)
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

    def switch_fields(*args):
        for widget in specific_frame.winfo_children():
            widget.destroy()
        fractal_ui = fractal_uis[fractal_type_var.get()]
        fractal_ui.create_fields(specific_frame)

    root = tk.Tk()
    root.title("Generador de Fractales")

    # Aplicar el tema Sun Valley.
    sv_ttk.set_theme("dark")

    # Marco principal.
    main_frame = ttk.Frame(root, padding=(20, 20, 20, 20))
    main_frame.grid(row=0, column=0, sticky="nsew")

    # Fractal type.
    ttk.Label(main_frame, text="Tipo de Fractal:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    fractal_type_var = tk.StringVar(value="mandelbrot")
    fractal_menu = ttk.Combobox(main_frame, textvariable=fractal_type_var, values=["mandelbrot", "julia", "sierpinski"], state="readonly")
    fractal_menu.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    fractal_type_var.trace("w", switch_fields)

    # Width and Height
    ttk.Label(main_frame, text="Ancho:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_width = ttk.Entry(main_frame)
    entry_width.insert(0, "1000")
    entry_width.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    ttk.Label(main_frame, text="Alto:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entry_height = ttk.Entry(main_frame)
    entry_height.insert(0, "1000")
    entry_height.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    ttk.Label(main_frame, text="Iteraciones Máximas:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
    entry_max_iter = ttk.Entry(main_frame)
    entry_max_iter.insert(0, "200")
    entry_max_iter.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    # Specific fields placeholder
    specific_frame = ttk.Frame(main_frame)
    specific_frame.grid(row=4, column=0, columnspan=2, sticky="ew")

    # Initialize fields
    fractal_uis = {
        "mandelbrot": MandelbrotUI(),
        "julia": JuliaUI(),
        "sierpinski": SierpinskiUI()
    }
    switch_fields()

    # Generate button
    generate_button = ttk.Button(main_frame, text="Generar Fractal", command=generate_fractal)
    generate_button.grid(row=10, column=0, columnspan=2, pady=20)

    root.mainloop()
