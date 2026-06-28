# ==========================
# IMPORTS
# ==========================

import tkinter as tk


# ==========================
# FOOTER CLASS
# ==========================

class Footer:

    def __init__(self, parent):

        footer = tk.Frame(
            parent,
            bg="#0f172a"
        )

        footer.pack(
            side="bottom",
            fill="x",
            pady=10
        )

        tk.Label(
            footer,
            text="TechFact Habit Track • Version 1.0",
            bg="#0f172a",
            fg="#94a3b8",
            font=("Segoe UI", 9)
        ).pack()

        tk.Label(
            footer,
            text="© 2026 TechFact Official • Developed by Engr Awais Farooq",
            bg="#0f172a",
            fg="#64748b",
            font=("Segoe UI", 8)
        ).pack()