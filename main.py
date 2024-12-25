from modules.fractal_types.julia import Julia
from modules.fractal_types.mandelbrot import Mandelbrot
from modules.fractal_types.sierpinski import Sierpinski
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sv_ttk  # Importa el tema Sun Valley

def create_app():
    def generate_fractal():
        fractal_type = fractal_type_var.get()
        try:
            width = int(entry_width.get())
            height = int(entry_height.get())
            max_iter = int(entry_max_iter.get())

            if fractal_type == "mandelbrot":
                xmin = float(entry_xmin.get())
                xmax = float(entry_xmax.get())
                ymin = float(entry_ymin.get())
                ymax = float(entry_ymax.get())

                fractal = Mandelbrot(width, height, max_iter, xmin, xmax, ymin, ymax)
                data = fractal.generate()
                fractal.plot(data)

            elif fractal_type == "julia":
                xmin = float(entry_xmin.get())
                xmax = float(entry_xmax.get())
                ymin = float(entry_ymin.get())
                ymax = float(entry_ymax.get())
                c = complex(entry_c.get())

                fractal = Julia(width, height, max_iter, xmin, xmax, ymin, ymax, c)
                data = fractal.generate()
                fractal.plot(data)

            elif fractal_type == "sierpinski":
                depth = int(entry_depth.get())

                fractal = Sierpinski(width, height, max_iter, depth)
                fractal.generate()

            else:
                messagebox.showerror("Error", "Tipo de fractal no soportado.")

        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

    def toggle_fields(*args):
        fractal_type = fractal_type_var.get()
        if fractal_type == "julia":
            julia_frame.grid()  # Mostrar campos de Julia
            sierpinski_frame.grid_remove()  # Ocultar campos de Sierpinski
        elif fractal_type == "sierpinski":
            sierpinski_frame.grid()  # Mostrar campos de Sierpinski
            julia_frame.grid_remove()  # Ocultar campos de Julia
        else:
            julia_frame.grid_remove()
            sierpinski_frame.grid_remove()

    def enforce_proportions(*args):
        try:
            width = int(entry_width.get())
            height = int(entry_height.get())
            ratio = width / height
            entry_height.delete(0, tk.END)
            entry_height.insert(0, int(width / ratio))
        except ValueError:
            pass

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
    fractal_type_var.trace("w", toggle_fields)

    # Width and Height
    ttk.Label(main_frame, text="Ancho:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_width = ttk.Entry(main_frame)
    entry_width.insert(0, "1000")
    entry_width.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
    entry_width.bind("<KeyRelease>", enforce_proportions)

    ttk.Label(main_frame, text="Alto:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entry_height = ttk.Entry(main_frame)
    entry_height.insert(0, "1000")
    entry_height.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    # Iteraciones
    ttk.Label(main_frame, text="Iteraciones Máximas:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
    entry_max_iter = ttk.Entry(main_frame)
    entry_max_iter.insert(0, "200")
    entry_max_iter.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    # Mandelbrot and Julia specific fields
    ttk.Label(main_frame, text="Xmin:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
    entry_xmin = ttk.Entry(main_frame)
    entry_xmin.insert(0, "-2")
    entry_xmin.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    ttk.Label(main_frame, text="Xmax:").grid(row=5, column=0, padx=10, pady=10, sticky="w")
    entry_xmax = ttk.Entry(main_frame)
    entry_xmax.insert(0, "2")
    entry_xmax.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    ttk.Label(main_frame, text="Ymin:").grid(row=6, column=0, padx=10, pady=10, sticky="w")
    entry_ymin = ttk.Entry(main_frame)
    entry_ymin.insert(0, "-2")
    entry_ymin.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

    ttk.Label(main_frame, text="Ymax:").grid(row=7, column=0, padx=10, pady=10, sticky="w")
    entry_ymax = ttk.Entry(main_frame)
    entry_ymax.insert(0, "2")
    entry_ymax.grid(row=7, column=1, padx=10, pady=10, sticky="ew")

    # Julia-specific fields
    julia_frame = ttk.Frame(main_frame, padding=(10, 10))
    julia_frame.grid(row=8, column=0, columnspan=2, sticky="ew")
    ttk.Label(julia_frame, text="Constante (para Julia):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_c = ttk.Entry(julia_frame)
    entry_c.insert(0, "-0.7+0.27015j")
    entry_c.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    julia_frame.grid_remove()

    # Sierpinski-specific fields
    sierpinski_frame = ttk.Frame(main_frame, padding=(10, 10))
    sierpinski_frame.grid(row=9, column=0, columnspan=2, sticky="ew")
    ttk.Label(sierpinski_frame, text="Profundidad (para Sierpinski):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_depth = ttk.Entry(sierpinski_frame)
    entry_depth.insert(0, "6")
    entry_depth.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    sierpinski_frame.grid_remove()

    # Generate button
    generate_button = ttk.Button(main_frame, text="Generar Fractal", command=generate_fractal)
    generate_button.grid(row=10, column=0, columnspan=2, pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_app()
