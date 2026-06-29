# ==========================
# IMPORTS
# ==========================

import tkinter as tk

from components.statistics import Statistics
from components.progress_panel import ProgressPanel
from utils.dashboard_service import DashboardService


# ==========================
# DASHBOARD PAGE
# ==========================


class DashboardPage:

    def __init__(self, parent):

        # ==========================
        # LOAD SUMMARY
        # ==========================

        summary = DashboardService.get_summary()

        tk.Label(
            parent,
            text="Dashboard",
            bg="#F8FAFC",
            fg="#111827",
            font=("Segoe UI", 28, "bold"),
        ).pack(pady=(30, 5))

        tk.Label(
            parent,
            text="Welcome to TechFact Habit Track 🚀",
            bg="#F8FAFC",
            fg="gray",
            font=("Segoe UI", 12),
        ).pack(pady=(0, 25))

        # Progress Summary

        ProgressPanel(parent)

        # Statistics

        Statistics(parent)


