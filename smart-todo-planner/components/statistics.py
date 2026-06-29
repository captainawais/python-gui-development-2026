# ==========================
# IMPORTS
# ==========================

import tkinter as tk

from utils.charts import ProgressChart
from utils.dashboard_service import DashboardService


# ==========================
# STAT CARD
# ==========================

class StatCard:

    def __init__(

        self,

        parent,

        title,

        value,

        color

    ):

        card = tk.Frame(
            parent,
            bg="white",
            bd=1,
            relief="solid"
        )

        card.pack(
            side="left",
            expand=True,
            fill="x",
            padx=10,
            pady=10
        )

        tk.Label(
            card,
            text=title,
            bg="white",
            fg="#111827",
            font=("Segoe UI", 12, "bold")
        ).pack(
            pady=(20,5)
        )

        tk.Label(
            card,
            text=value,
            bg="white",
            fg=color,
            font=("Segoe UI", 20, "bold")
        ).pack(
            pady=(0,20)
        )
# ==========================
# STATISTICS SECTION
# ==========================

class Statistics:

    def __init__(self, parent):
        
        self.summary = DashboardService.get_summary()

        self.frame = tk.Frame(
            parent,
            bg="#F8FAFC"
        )

        self.frame.pack(
            fill="x",
            padx=30,
            pady=20
        )

        # ==========================
        # TOP CARDS
        # ==========================

        cards = tk.Frame(
            self.frame,
            bg="#F8FAFC"
        )

        cards.pack(
            fill="x"
        )

        StatCard(
            cards,
            "📋 Total Habits",
            str(self.summary["total_habits"]),
            "#2563EB"
        )

        StatCard(
            cards,
            "✅ Completed",
            str(self.summary["completed"]),
            "#16A34A"
        )

        StatCard(
            cards,
            "❌ Pending",
            str(self.summary["pending"]),
            "#DC2626"
        )

        StatCard(
            cards,
            "📈 Success",
            f"{self.summary['success_rate']}%",
            "#F59E0B"
        )

        # ==========================
        # CHART SECTION
        # ==========================

        chart_card = tk.Frame(
            self.frame,
            bg="white",
            bd=1,
            relief="solid"
        )

        chart_card.pack(
            fill="x",
            pady=25
        )

        tk.Label(
            chart_card,
            text="📊 Weekly Analytics",
            bg="white",
            fg="#111827",
            font=("Segoe UI", 16, "bold")
        ).pack(
            pady=(20,10)
        )

        tk.Label(
            chart_card,
            text="View your weekly habit completion graph.",
            bg="white",
            fg="gray",
            font=("Segoe UI",10)
        ).pack()

        tk.Button(
            chart_card,
            text="📈 Open Progress Chart",
            command=self.show_chart,
            bg="#2563EB",
            fg="white",
            font=("Segoe UI",11,"bold"),
            width=24,
            height=2,
            border=0
        ).pack(
            pady=20
        )

    # ==========================
    # SHOW CHART
    # ==========================

    def show_chart(self):

        data = DashboardService.get_summary()

        completed = data["completed"]

        chart_data = [

            completed,

            completed,

            completed,

            completed,

            completed,

            completed,

            completed

        ]

        ProgressChart.show()