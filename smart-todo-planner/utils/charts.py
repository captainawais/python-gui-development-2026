# ==========================
# IMPORTS
# ==========================

import matplotlib.pyplot as plt


# ==========================
# PROGRESS CHART
# ==========================

class ProgressChart:

    @staticmethod
    def show(data):

        plt.figure(figsize=(8,4))

        plt.plot(
            data,
            linewidth=3,
            marker="o"
        )

        plt.title("Weekly Habit Progress")

        plt.xlabel("Day")

        plt.ylabel("Completed Habits")

        plt.grid(True)

        plt.tight_layout()

        plt.show()