# ==========================
# IMPORTS
# ==========================

import tkinter as tk

from components.dashboard import Dashboard


# ==========================
# MAIN WINDOW
# ==========================

window = tk.Tk()

window.title(
    "TechFact Habit Track v1.0"
)

window.geometry(
    "1400x850"
)

window.configure(
    bg="#0F172A"
)

window.state("zoomed")

window.minsize(
    1200,
    700
)

window.bind(
    "<Escape>",
    lambda event: window.destroy()
)


# ==========================
# START DASHBOARD
# ==========================

Dashboard(
    window
)


# ==========================
# START APPLICATION
# ==========================

window.mainloop()