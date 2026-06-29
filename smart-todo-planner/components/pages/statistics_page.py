# ==========================
# IMPORTS
# ==========================

import tkinter as tk

from components.statistics import Statistics


# ==========================
# STATISTICS PAGE
# ==========================


class StatisticsPage:

    # ==========================
    # INIT
    # ==========================

    def __init__(self, parent):

        # ==========================
        # PAGE TITLE
        # ==========================

        tk.Label(
            parent,
            text="Statistics",
            bg="#F8FAFC",
            fg="#111827",
            font=("Segoe UI", 28, "bold"),
        ).pack(pady=(30, 5))

        # ==========================
        # SUB TITLE
        # ==========================

        tk.Label(
            parent,
            text="Track your habit performance in real time 📊",
            bg="#F8FAFC",
            fg="gray",
            font=("Segoe UI", 12),
        ).pack(pady=(0, 25))

        # ==========================
        # STATISTICS COMPONENT
        # ==========================

        Statistics(parent)
