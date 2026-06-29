# ==========================
# IMPORTS
# ==========================

import matplotlib.pyplot as plt

from utils.storage import Storage

# ==========================
# PROGRESS CHART
# ==========================


class ProgressChart:

    # ==========================
    # GET WEEKLY DATA
    # ==========================

    @staticmethod
    def get_weekly_progress():

        data = Storage.load()

        if "weekly_progress" in data:

            return data["weekly_progress"]

        habits = data.get("habits", [])

        weekly = [0, 0, 0, 0, 0, 0, 0]

        for habit in habits:

            days = habit.get("days", [])

            for i in range(min(len(days), 7)):

                weekly[i] += days[i]

        return weekly

    # ==========================
    # SHOW CHART
    # ==========================

    @staticmethod
    def show():

        weekly = ProgressChart.get_weekly_progress()

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        plt.figure(figsize=(8, 4))

        plt.plot(days, weekly, marker="o", linewidth=2)

        plt.title("Weekly Habit Progress")

        plt.xlabel("Days")

        plt.ylabel("Completed Habits")

        plt.grid(True, linestyle="--", alpha=0.5)

        plt.tight_layout()

        plt.show()
