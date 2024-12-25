from modules.fractal_types.julia import Julia
from modules.fractal_types.mandelbrot import Mandelbrot
from modules.fractal_types.sierpinski import Sierpinski
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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

    root = tk.Tk()
    root.title("Generador de Fractales")

    tk.Label(root, text="Tipo de Fractal:").grid(row=0, column=0, padx=5, pady=5)
    fractal_type_var = tk.StringVar(value="mandelbrot")
    fractal_menu = ttk.Combobox(root, textvariable=fractal_type_var, values=["mandelbrot", "julia", "sierpinski"])
    fractal_menu.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Ancho:").grid(row=1, column=0, padx=5, pady=5)
    entry_width = tk.Entry(root)
    entry_width.insert(0, "1000")
    entry_width.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(root, text="Alto:").grid(row=2, column=0, padx=5, pady=5)
    entry_height = tk.Entry(root)
    entry_height.insert(0, "1000")
    entry_height.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(root, text="Iteraciones Máximas:").grid(row=3, column=0, padx=5, pady=5)
    entry_max_iter = tk.Entry(root)
    entry_max_iter.insert(0, "200")
    entry_max_iter.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(root, text="Xmin:").grid(row=4, column=0, padx=5, pady=5)
    entry_xmin = tk.Entry(root)
    entry_xmin.insert(0, "-2")
    entry_xmin.grid(row=4, column=1, padx=5, pady=5)

    tk.Label(root, text="Xmax:").grid(row=5, column=0, padx=5, pady=5)
    entry_xmax = tk.Entry(root)
    entry_xmax.insert(0, "2")
    entry_xmax.grid(row=5, column=1, padx=5, pady=5)

    tk.Label(root, text="Ymin:").grid(row=6, column=0, padx=5, pady=5)
    entry_ymin = tk.Entry(root)
    entry_ymin.insert(0, "-2")
    entry_ymin.grid(row=6, column=1, padx=5, pady=5)

    tk.Label(root, text="Ymax:").grid(row=7, column=0, padx=5, pady=5)
    entry_ymax = tk.Entry(root)
    entry_ymax.insert(0, "2")
    entry_ymax.grid(row=7, column=1, padx=5, pady=5)

    tk.Label(root, text="Constante (para Julia):").grid(row=8, column=0, padx=5, pady=5)
    entry_c = tk.Entry(root)
    entry_c.insert(0, "-0.7+0.27015j")
    entry_c.grid(row=8, column=1, padx=5, pady=5)

    tk.Label(root, text="Profundidad (para Sierpinski):").grid(row=9, column=0, padx=5, pady=5)
    entry_depth = tk.Entry(root)
    entry_depth.insert(0, "6")
    entry_depth.grid(row=9, column=1, padx=5, pady=5)

    generate_button = tk.Button(root, text="Generar Fractal", command=generate_fractal)
    generate_button.grid(row=10, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_app()
