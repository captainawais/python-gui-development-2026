# ==========================
# IMPORTS
# ==========================

import tkinter as tk
from utils.charts import ProgressChart

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

            relief="solid",

            width=220,

            height=110

        )

        card.pack(

            side="left",

            padx=12,

            pady=10,

            fill="both",

            expand=True

        )

        card.pack_propagate(False)

        tk.Label(

            card,

            text=title,

            bg="white",

            fg="gray",

            font=("Segoe UI",11)

        ).pack(

            pady=(18,5)

        )

        tk.Label(

            card,

            text=value,

            bg="white",

            fg=color,

            font=("Segoe UI",24,"bold")

        ).pack()


# ==========================
# STATISTICS SECTION
# ==========================

class Statistics:

    def __init__(self, parent):

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
            "10",
            "#2563EB"
        )

        StatCard(
            cards,
            "✅ Completed",
            "0",
            "#16A34A"
        )

        StatCard(
            cards,
            "❌ Pending",
            "10",
            "#DC2626"
        )

        StatCard(
            cards,
            "📈 Success",
            "0%",
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

        sample_data = [
            2,
            4,
            5,
            7,
            8,
            6,
            9
        ]

        ProgressChart.show(sample_data)