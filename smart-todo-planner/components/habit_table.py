# ==========================
# IMPORTS
# ==========================

import tkinter as tk
from utils.storage import Storage

# ==========================
# HABIT TABLE
# ==========================


class HabitTable:

    def __init__(self, parent):

        self.parent = parent

        self.check_vars = []

        # Load Saved Data

        self.data = Storage.load()

        self.habits = [
            "🌅 Wake Up",
            "💪 Workout",
            "🧘 Meditation",
            "📅 Planning",
            "💻 Coding",
            "📚 Reading",
            "💧 Drink Water",
            "🥗 Healthy Food",
            "🚶 Walking",
            "😴 Sleep Early",
        ]

        card = tk.Frame(parent, bg="white", bd=1, relief="solid")

        card.pack(padx=40, pady=30, fill="x")

        tk.Label(
            card,
            text="My Habits",
            bg="white",
            fg="#111827",
            font=("Segoe UI", 18, "bold"),
        ).pack(anchor="w", padx=20, pady=(20, 10))

        # ==========================
        # HEADER
        # ==========================

        header = tk.Frame(card, bg="white")

        header.pack(fill="x", padx=20, pady=(0, 10))

        tk.Label(
            header,
            text="Habit",
            bg="white",
            width=20,
            anchor="w",
            font=("Segoe UI", 10, "bold"),
        ).grid(row=0, column=0, sticky="w")

        for day in range(1, 8):

            tk.Label(
                header,
                text=str(day),
                bg="white",
                fg="#64748b",
                width=3,
                font=("Segoe UI", 9, "bold"),
            ).grid(row=0, column=day)

        tk.Label(
            header,
            text="%",
            bg="white",
            fg="#2563eb",
            width=5,
            font=("Segoe UI", 10, "bold"),
        ).grid(row=0, column=8, padx=10)

        # ==========================
        # HABITS
        # ==========================

        for habit in self.habits:

            row = tk.Frame(card, bg="white")

            row.pack(fill="x", padx=20, pady=5)

            tk.Label(
                row, text=habit, bg="white", width=20, anchor="w", font=("Segoe UI", 10)
            ).grid(row=0, column=0, sticky="w")

            vars = []

            percent = tk.Label(
                row,
                text="0%",
                bg="white",
                fg="#16a34a",
                width=5,
                font=("Segoe UI", 10, "bold"),
            )

            percent.grid(row=0, column=8, padx=10)

            for day in range(1, 8):

                var = tk.IntVar()

                vars.append(var)

                tk.Checkbutton(
                    row,
                    variable=var,
                    bg="white",
                    activebackground="white",
                    command=lambda v=vars, l=percent: self.update_progress(v, l),
                ).grid(row=0, column=day)

            self.check_vars.append(vars)

        tk.Button(
            card,
            text="💾 Save Progress",
            bg="#16A34A",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            width=20,
            command=self.save_data,
        ).pack(pady=20)

        # Load Previous Data

        self.load_data()

    # ==========================
    # UPDATE PROGRESS
    # ==========================

    def update_progress(self, vars, label):

        done = sum(v.get() for v in vars)

        percent = int(done / len(vars) * 100)

        label.config(text=f"{percent}%")

    # ==========================
    # SAVE DATA
    # ==========================

    def save_data(self):

        data = {"habits": []}

        for i, habit in enumerate(self.habits):

            row = []

            for var in self.check_vars[i]:

                row.append(var.get())

            data["habits"].append({"name": habit, "days": row})

        Storage.save(data)

    # ==========================
    # LOAD DATA
    # ==========================

    def load_data(self):

        data = Storage.load()

        if not data.get("habits"):

            return

        for i, habit in enumerate(data["habits"]):

            if i >= len(self.check_vars):

                break

            for j, value in enumerate(habit["days"]):

                if j >= len(self.check_vars[i]):

                    break

                self.check_vars[i][j].set(value)
