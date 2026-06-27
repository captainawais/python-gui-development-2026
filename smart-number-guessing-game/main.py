# ==========================
# IMPORTS
# ==========================

import tkinter as tk

from components.home_screen import HomeScreen


# ==========================
# MAIN WINDOW
# ==========================

window = tk.Tk()

window.title(
    "Smart Number Guessing Game v2.0"
)

window.geometry(
    "1000x800"
)

window.configure(
    bg="#0f172a"
)

window.resizable(
    False,
    False
)

# Escape Key Exit

window.bind(
    "<Escape>",
    lambda event: window.destroy()
)


# ==========================
# START APPLICATION
# ==========================

HomeScreen(
    window
)

window.mainloop()