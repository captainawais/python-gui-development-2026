# ==========================
# IMPORTS
# ==========================

import tkinter as tk

from components.habit_table import HabitTable


# ==========================
# HABITS PAGE
# ==========================


class HabitsPage:

    # ==========================
    # INIT
    # ==========================

    def __init__(self, parent):

        self.parent = parent

        # Page Title

        tk.Label(
            parent,
            text="Habits",
            bg="#F8FAFC",
            fg="#111827",
            font=("Segoe UI", 28, "bold"),
        ).pack(pady=(30, 5))

        # Subtitle

        tk.Label(
            parent,
            text="Manage your daily habits and track your progress in real time.",
            bg="#F8FAFC",
            fg="gray",
            font=("Segoe UI", 12),
        ).pack(pady=(0, 20))

        # Habit Table

        HabitTable(parent)

