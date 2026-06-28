# ==========================
# IMPORTS
# ==========================

import tkinter as tk


# ==========================
# SIDEBAR
# ==========================

class Sidebar:

    def __init__(self,parent):

        sidebar = tk.Frame(

            parent,

            bg="#111827",

            width=250

        )

        sidebar.pack(

            side="left",

            fill="y"

        )

        sidebar.pack_propagate(False)

        tk.Label(

            sidebar,

            text="✅",

            bg="#111827",

            fg="white",

            font=("Segoe UI",28)

        ).pack(
            pady=(30,10)
        )

        tk.Label(

            sidebar,

            text="TechFact\nHabit Track",

            bg="#111827",

            fg="white",

            font=("Segoe UI",18,"bold"),

            justify="center"

        ).pack(
            pady=(0,30)
        )

        menus=[

            "🏠 Dashboard",

            "✅ Habits",

            "📅 Calendar",

            "📊 Statistics",

            "🔥 Streaks",

            "⚙ Settings",

            "ℹ About"

        ]

        for item in menus:

            tk.Button(

                sidebar,

                text=item,

                anchor="w",

                bg="#111827",

                fg="white",

                activebackground="#1E293B",

                activeforeground="white",

                relief="flat",

                padx=20,

                font=("Segoe UI",11)

            ).pack(

                fill="x",

                pady=3
            )