# ==========================
# IMPORTS
# ==========================

import tkinter as tk

from utils.storage import Storage

# ==========================
# HABIT TABLE
# ==========================


class HabitTable:

    # ==========================
    # INIT
    # ==========================

    def __init__(self, parent):

        self.parent = parent

        self.data = Storage.load()

        self.check_vars = []

        self.percent_labels = []

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

        # ==========================
        # MAIN CARD
        # ==========================

        self.card = tk.Frame(parent, bg="white", bd=1, relief="solid")

        self.card.pack(fill="x", padx=30, pady=25)

        # ==========================
        # TITLE
        # ==========================

        tk.Label(
            self.card,
            text="My Habits",
            bg="white",
            fg="#111827",
            font=("Segoe UI", 20, "bold"),
        ).pack(anchor="w", padx=20, pady=(20, 15))

        # ==========================
        # TABLE FRAME
        # ==========================

        self.table = tk.Frame(self.card, bg="white")

        self.table.pack(fill="x", padx=20, pady=(0, 15))

        self.create_header()

        self.create_rows()

        self.create_save_button()

        self.load_data()

    # ==========================
    # TABLE HEADER
    # ==========================

    def create_header(self):

        tk.Label(
            self.table,
            text="Habit",
            bg="white",
            fg="#111827",
            width=22,
            anchor="w",
            font=("Segoe UI", 10, "bold"),
        ).grid(row=0, column=0, padx=5, pady=8, sticky="w")

        for day in range(1, 8):

            tk.Label(
                self.table,
                text=str(day),
                bg="white",
                fg="#64748B",
                width=3,
                font=("Segoe UI", 9, "bold"),
            ).grid(row=0, column=day, padx=2)

        tk.Label(
            self.table,
            text="%",
            bg="white",
            fg="#2563EB",
            width=5,
            font=("Segoe UI", 10, "bold"),
        ).grid(row=0, column=8, padx=10)

    # ==========================
    # HABIT ROWS
    # ==========================

    def create_rows(self):

        for index, habit in enumerate(self.habits):

            tk.Label(
                self.table,
                text=habit,
                bg="white",
                fg="#111827",
                width=22,
                anchor="w",
                font=("Segoe UI", 10),
            ).grid(row=index + 1, column=0, sticky="w", pady=6)

            row_vars = []

            percent = tk.Label(
                self.table,
                text="0%",
                bg="white",
                fg="#16A34A",
                width=5,
                font=("Segoe UI", 10, "bold"),
            )

            percent.grid(row=index + 1, column=8, padx=10)

            self.percent_labels.append(percent)

            for day in range(7):

                var = tk.IntVar()

                row_vars.append(var)

                tk.Checkbutton(
                    self.table,
                    variable=var,
                    bg="white",
                    activebackground="white",
                    command=lambda r=index: self.update_progress(r),
                ).grid(row=index + 1, column=day + 1)

            self.check_vars.append(row_vars)

    # ==========================
    # SAVE BUTTON
    # ==========================

    def create_save_button(self):

        tk.Button(
            self.card,
            text="💾 Save Progress",
            bg="#16A34A",
            fg="white",
            activebackground="#15803D",
            activeforeground="white",
            font=("Segoe UI", 11, "bold"),
            width=22,
            relief="flat",
            cursor="hand2",
            command=self.save_data,
        ).pack(pady=(10, 20))

    # ==========================
    # UPDATE PROGRESS
    # ==========================

    def update_progress(self, row_index):

        vars = self.check_vars[row_index]

        completed = sum(var.get() for var in vars)

        percent = int((completed / len(vars)) * 100)

        self.percent_labels[row_index].config(text=f"{percent}%")

        # Auto Save
        self.save_data()

        # Refresh Dashboard
        self.refresh_dashboard()

    # ==========================
    # SAVE DATA
    # ==========================

    def save_data(self):

        data = Storage.load()

        data["habits"] = []

        for i, habit in enumerate(self.habits):

            days = [var.get() for var in self.check_vars[i]]

            data["habits"].append({"name": habit, "days": days})

            # ==========================
            # UPDATE REAL-TIME HISTORY
            # ==========================

            from datetime import datetime

            today = datetime.now().strftime("%Y-%m-%d")

            completed = 0

            total = 0

            for habit in data["habits"]:

                completed += sum(habit["days"])

                total += len(habit["days"])

            pending = total - completed

            success_rate = 0

            if total > 0:

                success_rate = round(completed / total * 100, 2)

            if "history" not in data:

                data["history"] = {}

            data["history"][today] = {
                "completed": completed,
                "pending": pending,
                "success_rate": success_rate,
                "total_habits": len(self.habits),
                "timestamp": today,
            }

            data["completed"] = completed

            data["pending"] = pending

            data["success_rate"] = success_rate

            data["total_habits"] = len(self.habits)

        # ==========================
        # WEEKLY PROGRESS
        # ==========================

        data["weekly_progress"] = [
            sum(habit["days"][day] for habit in data["habits"]) for day in range(7)
        ]

        Storage.save(data)

    # ==========================
    # LOAD DATA
    # ==========================

    def load_data(self):

        data = Storage.load()

        habits = data.get("habits", [])

        if not habits:

            return

        for i, habit in enumerate(habits):

            if i >= len(self.check_vars):

                break

            days = habit.get("days", [])

            for j, value in enumerate(days):

                if j >= len(self.check_vars[i]):

                    break

                self.check_vars[i][j].set(value)

            self.update_progress(i)

    # ==========================
    # REFRESH DASHBOARD
    # ==========================

    def refresh_dashboard(self):
        """
        Future Version

        Dashboard
        Statistics
        Progress Panel
        Calendar
        Streak

        will refresh automatically from here.
        """

        pass

    # ==========================
    # GET TOTAL COMPLETED
    # ==========================

    def get_completed(self):

        total = 0

        for row in self.check_vars:

            total += sum(var.get() for var in row)

        return total

    # ==========================
    # GET TOTAL PENDING
    # ==========================

    def get_pending(self):

        total = len(self.habits) * 7

        return total - self.get_completed()

    # ==========================
    # GET SUCCESS RATE
    # ==========================

    def get_success_rate(self):

        total = len(self.habits) * 7

        completed = self.get_completed()

        if total == 0:

            return 0

        return round((completed / total) * 100, 1)
