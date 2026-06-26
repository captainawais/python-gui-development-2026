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
    "Smart Number Guessing Game v1.2"
)

window.geometry(
    "900x800"
)

window.configure(
    bg="#0f172a"
)

window.resizable(
    False,
    False
)


# ==========================
# START HOME SCREEN
# ==========================

HomeScreen(
    window
)


# ==========================
# FOOTER
# ==========================

footer = tk.Label(
    window,
    text="Powered by Tech Fact Official & Developed by Engr Awais Farooq",
    bg="#0f172a",
    fg="white",
    font=("Segoe UI", 10)
)

footer.pack(
    side="bottom",
    pady=10
)


# ==========================
# START APPLICATION
# ==========================

window.mainloop()