# ==========================
# IMPORTS
# ==========================

import tkinter as tk

from components.calendar import CalendarView
from utils.dashboard_service import DashboardService


# ==========================
# CALENDAR PAGE
# ==========================


class CalendarPage:

    # ==========================
    # INIT
    # ==========================

    def __init__(self, parent):

        self.summary = DashboardService.get_summary()

        # ==========================
        # PAGE TITLE
        # ==========================

        tk.Label(
            parent,
            text="Calendar",
            bg="#F8FAFC",
            fg="#111827",
            font=("Segoe UI", 28, "bold"),
        ).pack(pady=(30, 5))

        tk.Label(
            parent,
            text="View your monthly habit activity in real time 📅",
            bg="#F8FAFC",
            fg="gray",
            font=("Segoe UI", 12),
        ).pack(pady=(0, 25))

        # ==========================
        # CALENDAR
        # ==========================

        CalendarView(parent)

        # ==========================
        # MONTH SUMMARY
        # ==========================

        card = tk.Frame(parent, bg="white", bd=1, relief="solid")

        card.pack(fill="x", padx=30, pady=20)

        tk.Label(
            card,
            text="Monthly Summary",
            bg="white",
            fg="#111827",
            font=("Segoe UI", 18, "bold"),
        ).pack(anchor="w", padx=20, pady=(20, 15))

        self.add_item(
            card, "📋 Total Habits", str(self.summary["total_habits"]), "#2563EB"
        )

        self.add_item(card, "✅ Completed", str(self.summary["completed"]), "#16A34A")

        self.add_item(card, "❌ Pending", str(self.summary["pending"]), "#DC2626")

        self.add_item(
            card, "📈 Success Rate", f"{self.summary['success_rate']}%", "#F59E0B"
        )

        self.add_item(
            card,
            "🔥 Current Streak",
            f"{self.summary['current_streak']} Days",
            "#2563EB",
        )

        self.add_item(
            card, "🏆 Best Streak", f"{self.summary['best_streak']} Days", "#16A34A"
        )

    # ==========================
    # ADD SUMMARY ITEM
    # ==========================

    def add_item(self, parent, title, value, color):

        row = tk.Frame(parent, bg="white")

        row.pack(fill="x", padx=20, pady=8)

        tk.Label(row, text=title, bg="white", fg="#374151", font=("Segoe UI", 11)).pack(
            side="left"
        )

        tk.Label(
            row, text=value, bg="white", fg=color, font=("Segoe UI", 11, "bold")
        ).pack(side="right")

    