# ==========================
# IMPORTS
# ==========================

import tkinter as tk
from datetime import datetime

# ==========================
# FOOTER
# ==========================


class Footer:

    # ==========================
    # INIT
    # ==========================

    def __init__(self, parent):

        footer = tk.Frame(parent, bg="#0F172A", height=60)

        footer.pack(fill="x", padx=30, pady=(30, 0))

        footer.pack_propagate(False)

        year = datetime.now().year

        version = "2.0"

        # ==========================
        # APP NAME
        # ==========================

        tk.Label(
            footer,
            text=f"TechFact Habit Track • Version {version}",
            bg="#0F172A",
            fg="#CBD5E1",
            font=("Segoe UI", 10, "bold"),
        ).pack(pady=(10, 2))

        # ==========================
        # COPYRIGHT
        # ==========================

        tk.Label(
            footer,
            text=f"© {year} TechFact Official • Developed by Engr. Awais Farooq",
            bg="#0F172A",
            fg="#94A3B8",
            font=("Segoe UI", 9),
        ).pack()

        # ==========================
        # STATUS
        # ==========================

        tk.Label(
            footer,
            text="Python • Tkinter • JSON Storage • Real-Time Tracking",
            bg="#0F172A",
            fg="#64748B",
            font=("Segoe UI", 8),
        ).pack(pady=(2, 8))
