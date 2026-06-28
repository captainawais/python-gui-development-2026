# ==========================
# IMPORTS
# ==========================

import tkinter as tk


# ==========================
# CALENDAR
# ==========================

class CalendarView:

    def __init__(self, parent):

        card = tk.Frame(
            parent,
            bg="white",
            bd=1,
            relief="solid"
        )

        card.pack(
            fill="x",
            padx=30,
            pady=20
        )

        tk.Label(
            card,
            text="📅 Monthly Habit Calendar",
            bg="white",
            fg="#111827",
            font=("Segoe UI",16,"bold")
        ).pack(
            pady=20
        )

        table = tk.Frame(
            card,
            bg="white"
        )

        table.pack(
            pady=10
        )

        headers = [
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"
        ]

        for col, day in enumerate(headers):

            tk.Label(
                table,
                text=day,
                bg="white",
                fg="#2563EB",
                width=6,
                font=("Segoe UI",10,"bold")
            ).grid(
                row=0,
                column=col,
                pady=5
            )

        day = 1

        for r in range(1,6):

            for c in range(7):

                if day <= 31:

                    tk.Button(
                        table,
                        text=str(day),
                        width=4,
                        height=2,
                        bg="white",
                        relief="groove"
                    ).grid(
                        row=r,
                        column=c,
                        padx=3,
                        pady=3
                    )

                    day += 1