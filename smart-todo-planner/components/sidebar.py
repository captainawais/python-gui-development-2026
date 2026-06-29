# ==========================
# IMPORTS
# ==========================

import tkinter as tk

# ==========================
# SIDEBAR
# ==========================


class Sidebar:

    # ==========================
    # INIT
    # ==========================

    def __init__(self, parent, dashboard):

        self.dashboard = dashboard

        self.buttons = []

        sidebar = tk.Frame(parent, bg="#111827", width=250)

        sidebar.pack(side="left", fill="y")

        sidebar.pack_propagate(False)

        # ==========================
        # LOGO
        # ==========================

        tk.Label(
            sidebar, text="✅", bg="#111827", fg="white", font=("Segoe UI", 30)
        ).pack(pady=(30, 10))

        tk.Label(
            sidebar,
            text="TechFact\nHabit Track",
            bg="#111827",
            fg="white",
            font=("Segoe UI", 18, "bold"),
            justify="center",
        ).pack(pady=(0, 35))

        # ==========================
        # MENU
        # ==========================

        menus = [
            ("🏠 Dashboard", self.dashboard.show_dashboard),
            ("✅ Habits", self.dashboard.show_habits),
            ("📅 Calendar", self.dashboard.show_calendar),
            ("📊 Statistics", self.dashboard.show_statistics),
            ("🔥 Streak", self.dashboard.show_streaks),
            ("⚙ Settings", self.dashboard.show_settings),
            ("ℹ About", self.dashboard.show_about),
        ]

        for text, command in menus:

            button = tk.Button(
                sidebar,
                text=text,
                anchor="w",
                bg="#111827",
                fg="white",
                activebackground="#2563EB",
                activeforeground="white",
                relief="flat",
                bd=0,
                padx=25,
                pady=12,
                cursor="hand2",
                font=("Segoe UI", 11),
                command=lambda c=command, b=text: self.change_page(c, b),
            )

            button.pack(fill="x", pady=2)

            self.buttons.append(button)

        # ==========================
        # ACTIVE BUTTON
        # ==========================

        self.highlight("🏠 Dashboard")

        # ==========================
        # FOOTER
        # ==========================

        footer = tk.Frame(sidebar, bg="#111827")

        footer.pack(side="bottom", fill="x", pady=20)

        tk.Label(
            footer, text="Version 2.0", bg="#111827", fg="#94A3B8", font=("Segoe UI", 9)
        ).pack()

        tk.Label(
            footer,
            text="TechFact Official",
            bg="#111827",
            fg="#64748B",
            font=("Segoe UI", 8),
        ).pack()

    # ==========================
    # CHANGE PAGE
    # ==========================

    def change_page(self, command, button_name):

        self.highlight(button_name)

        command()

    # ==========================
    # HIGHLIGHT BUTTON
    # ==========================

    def highlight(self, current):

        for button in self.buttons:

            if button["text"] == current:

                button.configure(bg="#2563EB", fg="white")

            else:

                button.configure(bg="#111827", fg="white")
