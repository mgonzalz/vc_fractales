from tkinter import ttk

class BaseFractalUI:
    def create_common_fields(self, parent_frame):
        ttk.Label(parent_frame, text="Xmin:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.entry_xmin = ttk.Entry(parent_frame)
        self.entry_xmin.insert(0, "-2")
        self.entry_xmin.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

        ttk.Label(parent_frame, text="Xmax:").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.entry_xmax = ttk.Entry(parent_frame)
        self.entry_xmax.insert(0, "2")
        self.entry_xmax.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

        ttk.Label(parent_frame, text="Ymin:").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.entry_ymin = ttk.Entry(parent_frame)
        self.entry_ymin.insert(0, "-2")
        self.entry_ymin.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

        ttk.Label(parent_frame, text="Ymax:").grid(row=7, column=0, padx=10, pady=10, sticky="w")
        self.entry_ymax = ttk.Entry(parent_frame)
        self.entry_ymax.insert(0, "2")
        self.entry_ymax.grid(row=7, column=1, padx=10, pady=10, sticky="ew")

    def get_common_params(self):
        return {
            "xmin": float(self.entry_xmin.get()),
            "xmax": float(self.entry_xmax.get()),
            "ymin": float(self.entry_ymin.get()),
            "ymax": float(self.entry_ymax.get())
        }
