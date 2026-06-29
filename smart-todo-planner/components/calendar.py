# ==========================
# IMPORTS
# ==========================

import tkinter as tk
import calendar
from datetime import datetime

from utils.storage import Storage

# ==========================
# CALENDAR VIEW
# ==========================


class CalendarView:

    def __init__(self, parent):

        self.data = Storage.load()

        self.history = self.data.get("history", {})

        today = datetime.now()

        self.year = today.year
        self.month = today.month
        self.today = today.day

        # ==========================
        # CARD
        # ==========================

        card = tk.Frame(parent, bg="white", bd=1, relief="solid")

        card.pack(fill="x", padx=30, pady=20)

        # ==========================
        # TITLE
        # ==========================

        tk.Label(
            card,
            text="📅 Monthly Habit Calendar",
            bg="white",
            fg="#111827",
            font=("Segoe UI", 16, "bold"),
        ).pack(pady=(20, 5))

        tk.Label(
            card,
            text=today.strftime("%B %Y"),
            bg="white",
            fg="gray",
            font=("Segoe UI", 11),
        ).pack(pady=(0, 20))

        # ==========================
        # TABLE
        # ==========================

        table = tk.Frame(card, bg="white")

        table.pack(pady=(0, 20))

        headers = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        for col, day in enumerate(headers):

            tk.Label(
                table,
                text=day,
                width=6,
                bg="white",
                fg="#2563EB",
                font=("Segoe UI", 10, "bold"),
            ).grid(row=0, column=col, padx=2, pady=5)

        month = calendar.monthcalendar(self.year, self.month)

        for row, week in enumerate(month, start=1):

            for col, day in enumerate(week):

                if day == 0:

                    tk.Label(table, text="", width=5, bg="white").grid(
                        row=row, column=col, padx=2, pady=2
                    )

                    continue

                date_key = f"{self.year}-{self.month:02d}-{day:02d}"

                bg = "white"
                fg = "#111827"

                # Today

                if day == self.today:

                    bg = "#2563EB"
                    fg = "white"

                # Completed Day

                if date_key in self.history:

                    if self.history[date_key]["success_rate"] > 0:

                        bg = "#22C55E"
                        fg = "white"

                tk.Button(
                    table,
                    text=str(day),
                    width=4,
                    height=2,
                    bg=bg,
                    fg=fg,
                    relief="groove",
                    bd=1,
                    cursor="hand2",
                ).grid(row=row, column=col, padx=3, pady=3)

        # ==========================
        # LEGEND
        # ==========================

        legend = tk.Frame(card, bg="white")

        legend.pack(pady=(10, 20))

        tk.Label(
            legend, text="🟩 Completed", bg="white", fg="#16A34A", font=("Segoe UI", 10)
        ).pack(side="left", padx=15)

        tk.Label(
            legend, text="🟦 Today", bg="white", fg="#2563EB", font=("Segoe UI", 10)
        ).pack(side="left", padx=15)

        tk.Label(
            legend, text="⬜ No Record", bg="white", fg="gray", font=("Segoe UI", 10)
        ).pack(side="left", padx=15)
