# ==========================
# IMPORTS
# ==========================

import tkinter as tk
from tkinter import ttk

from utils.dashboard_service import DashboardService

# ==========================
# PROGRESS PANEL
# ==========================


class ProgressPanel:

    # ==========================
    # INIT
    # ==========================

    def __init__(self, parent):

        self.summary = DashboardService.get_summary()

        card = tk.Frame(parent, bg="white", bd=1, relief="solid", padx=20, pady=20)

        card.pack(fill="x", padx=30, pady=20)

        # ==========================
        # TITLE
        # ==========================

        tk.Label(
            card,
            text="Today's Progress",
            bg="white",
            fg="#111827",
            font=("Segoe UI", 16, "bold"),
        ).pack(pady=(0, 20))

        # ==========================
        # STATS
        # ==========================

        self.add_item(
            card,
            "🔥 Current Streak",
            f"{self.summary['current_streak']} Days",
            "#2563EB",
        )

        self.add_item(
            card, "🏆 Best Streak", f"{self.summary['best_streak']} Days", "#16A34A"
        )

        self.add_item(
            card,
            "🎯 Today's Goal",
            f"{self.summary['completed']} / {self.summary['total_habits']}",
            "#F59E0B",
        )

        self.add_item(card, "✅ Completed", str(self.summary["completed"]), "#22C55E")

        self.add_item(card, "❌ Pending", str(self.summary["pending"]), "#EF4444")

        # ==========================
        # PROGRESS TITLE
        # ==========================

        tk.Label(
            card,
            text="Overall Progress",
            bg="white",
            fg="#374151",
            font=("Segoe UI", 11, "bold"),
        ).pack(pady=(25, 5))

        # ==========================
        # PROGRESS BAR
        # ==========================

        self.progress = ttk.Progressbar(
            card, orient="horizontal", mode="determinate", length=260
        )

        self.progress["maximum"] = 100

        self.progress["value"] = self.summary["success_rate"]

        self.progress.pack(pady=5)

        # ==========================
        # PERCENT LABEL
        # ==========================

        tk.Label(
            card,
            text=f"{self.summary['success_rate']}%",
            bg="white",
            fg="#2563EB",
            font=("Segoe UI", 12, "bold"),
        ).pack(pady=(8, 20))

    # ==========================
    # ADD ITEM
    # ==========================

    def add_item(self, parent, title, value, color):

        frame = tk.Frame(parent, bg="white")

        frame.pack(fill="x", pady=7)

        tk.Label(
            frame, text=title, bg="white", fg="#374151", font=("Segoe UI", 10)
        ).pack(side="left")

        tk.Label(
            frame, text=value, bg="white", fg=color, font=("Segoe UI", 10, "bold")
        ).pack(side="right")
